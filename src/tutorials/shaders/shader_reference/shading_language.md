# Shading language {#doc_shading_language}

## Introduction

Godot uses a shading language similar to GLSL ES 3.0. Most datatypes and
functions are supported, and the few remaining ones will likely be added
over time.

If you are already familiar with GLSL, the `Godot Shader Migration
Guide<doc_converting_glsl_to_godot_shaders>`{.interpreted-text
role="ref"} is a resource that will help you transition from regular
GLSL to Godot\'s shading language.

## Data types

Most GLSL ES 3.0 datatypes are supported:

| Type | Description |
|----|----|
| **void** | Void datatype, useful only for functions that return nothing. |
| **bool** | Boolean datatype, can only contain `true` or `false`. |
| **bvec2** | Two-component vector of booleans. |
| **bvec3** | Three-component vector of booleans. |
| **bvec4** | Four-component vector of booleans. |
| **int** | 32 bit signed scalar integer. |
| **ivec2** | Two-component vector of signed integers. |
| **ivec3** | Three-component vector of signed integers. |
| **ivec4** | Four-component vector of signed integers. |
| **uint** | Unsigned scalar integer; can\'t contain negative numbers. |
| **uvec2** | Two-component vector of unsigned integers. |
| **uvec3** | Three-component vector of unsigned integers. |
| **uvec4** | Four-component vector of unsigned integers. |
| **float** | 32 bit floating-point scalar. |
| **vec2** | Two-component vector of floating-point values. |
| **vec3** | Three-component vector of floating-point values. |
| **vec4** | Four-component vector of floating-point values. |
| **mat2** | 2x2 matrix, in column major order. |
| **mat3** | 3x3 matrix, in column major order. |
| **mat4** | 4x4 matrix, in column major order. |
| **sampler2D** | Sampler type for binding 2D textures, which are read as float. |
| **isampler2D** | Sampler type for binding 2D textures, which are read as signed integer. |
| **usampler2D** | Sampler type for binding 2D textures, which are read as unsigned integer. |
| **sampler2DArray** | Sampler type for binding 2D texture arrays, which are read as float. |
| **isampler2DArray** | Sampler type for binding 2D texture arrays, which are read as signed integer. |
| **usampler2DArray** | Sampler type for binding 2D texture arrays, which are read as unsigned integer. |
| **sampler3D** | Sampler type for binding 3D textures, which are read as float. |
| **isampler3D** | Sampler type for binding 3D textures, which are read as signed integer. |
| **usampler3D** | Sampler type for binding 3D textures, which are read as unsigned integer. |
| **samplerCube** | Sampler type for binding Cubemaps, which are read as float. |
| **samplerCubeArray** | Sampler type for binding Cubemap arrays, which are read as float. Only supported in Forward+ and Mobile, not Compatibility. |

> [!WARNING]
> Local variables are not initialized to a default value such as `0.0`.
> If you use a variable without assigning it first, it will contain
> whatever value was already present at that memory location, and
> unpredictable visual glitches will appear. However, uniforms and
> varyings are initialized to a default value.

### Comments

The shading language supports the same comment syntax as used in C# and
C++:

``` glsl
// Single-line comment.
int a = 2;  // Another single-line comment.

/*
Multi-line comment.
The comment ends when the ending delimiter is found
(here, it's on the line below).
*/
int b = 3;
```

Additionally, you can use documentation comments that are displayed in
the inspector when hovering a shader parameter. Documentation comments
are currently only supported when placed immediately above a `uniform`
declaration. These documentation comments only support the **multiline**
comment syntax and must use **two** leading asterisks (`/**`) instead of
just one (`/*`):

``` glsl
/**
 * This is a documentation comment.
 * These lines will appear in the inspector when hovering the shader parameter
 * named "Something".
 * You can use [b]BBCode[/b] [i]formatting[/i] in the comment.
 */
uniform int something = 1;
```

The asterisks on the follow-up lines are not required, but are
recommended as per the `doc_shaders_style_guide`{.interpreted-text
role="ref"}. These asterisks are automatically stripped by the
inspector, so they won\'t appear in the tooltip.

### Casting

Just like GLSL ES 3.0, implicit casting between scalars and vectors of
the same size but different type is not allowed. Casting of types of
different size is also not allowed. Conversion must be done explicitly
via constructors.

Example:

``` glsl
float a = 2; // invalid
float a = 2.0; // valid
float a = float(2); // valid
```

Default integer constants are signed, so casting is always needed to
convert to unsigned:

``` glsl
int a = 2; // valid
uint a = 2; // invalid
uint a = uint(2); // valid
```

### Members

Individual scalar members of vector types are accessed via the \"x\",
\"y\", \"z\" and \"w\" members. Alternatively, using \"r\", \"g\", \"b\"
and \"a\" also works and is equivalent. Use whatever fits best for your
needs.

For matrices, use the `m[column][row]` indexing syntax to access each
scalar, or `m[column]` to access a vector by column index. For example,
for accessing the y-component of the translation from a mat4 transform
matrix (4th column, 2nd line) you use `m[3][1]` or `m[3].y`.

### Constructing

Construction of vector types must always pass:

``` glsl
// The required amount of scalars
vec4 a = vec4(0.0, 1.0, 2.0, 3.0);
// Complementary vectors and/or scalars
vec4 a = vec4(vec2(0.0, 1.0), vec2(2.0, 3.0));
vec4 a = vec4(vec3(0.0, 1.0, 2.0), 3.0);
// A single scalar for the whole vector
vec4 a = vec4(0.0);
```

Construction of matrix types requires vectors of the same dimension as
the matrix, interpreted as columns. You can also build a diagonal matrix
using `matx(float)` syntax. Accordingly, `mat4(1.0)` is an identity
matrix.

``` glsl
mat2 m2 = mat2(vec2(1.0, 0.0), vec2(0.0, 1.0));
mat3 m3 = mat3(vec3(1.0, 0.0, 0.0), vec3(0.0, 1.0, 0.0), vec3(0.0, 0.0, 1.0));
mat4 identity = mat4(1.0);
```

Matrices can also be built from a matrix of another dimension. There are
two rules:

1\. If a larger matrix is constructed from a smaller matrix, the
additional rows and columns are set to the values they would have in an
identity matrix. 2. If a smaller matrix is constructed from a larger
matrix, the top, left submatrix of the larger matrix is used.

``` glsl
mat3 basis = mat3(MODEL_MATRIX);
mat4 m4 = mat4(basis);
mat2 m2 = mat2(m4);
```

### Swizzling

It is possible to obtain any combination of components in any order, as
long as the result is another vector type (or scalar). This is easier
shown than explained:

``` glsl
vec4 a = vec4(0.0, 1.0, 2.0, 3.0);
vec3 b = a.rgb; // Creates a vec3 with vec4 components.
vec3 b = a.ggg; // Also valid; creates a vec3 and fills it with a single vec4 component.
vec3 b = a.bgr; // "b" will be vec3(2.0, 1.0, 0.0).
vec3 b = a.xyz; // Also rgba, xyzw are equivalent.
vec3 b = a.stp; // And stpq (for texture coordinates).
float c = b.w; // Invalid, because "w" is not present in vec3 b.
vec3 c = b.xrt; // Invalid, mixing different styles is forbidden.
b.rrr = a.rgb; // Invalid, assignment with duplication.
b.bgr = a.rgb; // Valid assignment. "b"'s "blue" component will be "a"'s "red" and vice versa.
```

### Precision

It is possible to add precision modifiers to datatypes; use them for
uniforms, variables, arguments and varyings:

``` glsl
lowp vec4 a = vec4(0.0, 1.0, 2.0, 3.0); // low precision, usually 8 bits per component mapped to 0-1
mediump vec4 a = vec4(0.0, 1.0, 2.0, 3.0); // medium precision, usually 16 bits or half float
highp vec4 a = vec4(0.0, 1.0, 2.0, 3.0); // high precision, uses full float or integer range (32 bit default)
```

Using lower precision for some operations can speed up the math involved
(at the cost of less precision). This is rarely needed in the vertex
processor function (where full precision is needed most of the time),
but is often useful in the fragment processor.

Some architectures (mainly mobile) can benefit significantly from this,
but there are downsides such as the additional overhead of conversion
between precisions. Refer to the documentation of the target
architecture for further information. In many cases, mobile drivers
cause inconsistent or unexpected behavior and it is best to avoid
specifying precision unless necessary.

## Arrays

Arrays are containers for multiple variables of a similar type.

### Local arrays

Local arrays are declared in functions. They can use all of the allowed
datatypes, except samplers. The array declaration follows a C-style
syntax: `[const] + [precision] + typename + identifier + [array size]`.

``` glsl
void fragment() {
    float arr[3];
}
```

They can be initialized at the beginning like:

``` glsl
float float_arr[3] = float[3] (1.0, 0.5, 0.0); // first constructor

int int_arr[3] = int[] (2, 1, 0); // second constructor

vec2 vec2_arr[3] = { vec2(1.0, 1.0), vec2(0.5, 0.5), vec2(0.0, 0.0) }; // third constructor

bool bool_arr[] = { true, true, false }; // fourth constructor - size is defined automatically from the element count
```

You can declare multiple arrays (even with different sizes) in one
expression:

``` glsl
float a[3] = float[3] (1.0, 0.5, 0.0),
b[2] = { 1.0, 0.5 },
c[] = { 0.7 },
d = 0.0,
e[5];
```

To access an array element, use the indexing syntax:

``` glsl
float arr[3];

arr[0] = 1.0; // setter

COLOR.r = arr[0]; // getter
```

Arrays also have a built-in function `.length()` (not to be confused
with the built-in `length()` function). It doesn\'t accept any
parameters and will return the array\'s size.

``` glsl
float arr[] = { 0.0, 1.0, 0.5, -1.0 };
for (int i = 0; i < arr.length(); i++) {
    // ...
}
```

> [!NOTE]
> If you use an index either below 0 or greater than array size - the
> shader will crash and break rendering. To prevent this, use
> `length()`, `if`, or `clamp()` functions to ensure the index is
> between 0 and the array\'s length. Always carefully test and check
> your code. If you pass a constant expression or a number, the editor
> will check its bounds to prevent this crash.

### Global arrays

You can declare arrays at global space like:

``` glsl
shader_type spatial;

const lowp vec3 v[1] = lowp vec3[1] ( vec3(0, 0, 1) );

void fragment() {
  ALBEDO = v[0];
}
```

> [!NOTE]
> Global arrays have to be declared as global constants, otherwise they
> can be declared the same as local arrays.

## Constants

Use the `const` keyword before the variable declaration to make that
variable immutable, which means that it cannot be modified. All basic
types, except samplers can be declared as constants. Accessing and using
a constant value is slightly faster than using a uniform. Constants must
be initialized at their declaration.

``` glsl
const vec2 a = vec2(0.0, 1.0);
vec2 b;

a = b; // invalid
b = a; // valid
```

Constants cannot be modified and additionally cannot have hints, but
multiple of them (if they have the same type) can be declared in a
single expression e.g

``` glsl
const vec2 V1 = vec2(1, 1), V2 = vec2(2, 2);
```

Similar to variables, arrays can also be declared with `const`.

``` glsl
const float arr[] = { 1.0, 0.5, 0.0 };

arr[0] = 1.0; // invalid

COLOR.r = arr[0]; // valid
```

Constants can be declared both globally (outside of any function) or
locally (inside a function). Global constants are useful when you want
to have access to a value throughout your shader that does not need to
be modified. Like uniforms, global constants are shared between all
shader stages, but they are not accessible outside of the shader.

``` glsl
shader_type spatial;

const float GOLDEN_RATIO = 1.618033988749894;
```

Constants of the `float` type must be initialized using `.` notation
after the decimal part or by using the scientific notation. The optional
`f` post-suffix is also supported.

``` glsl
float a = 1.0;
float b = 1.0f; // same, using suffix for clarity
float c = 1e-1; // gives 0.1 by using the scientific notation
```

Constants of the `uint` (unsigned int) type must have a `u` suffix to
differentiate them from signed integers. Alternatively, this can be done
by using the `uint(x)` built-in conversion function.

``` glsl
uint a = 1u;
uint b = uint(1);
```

## Structs

Structs are compound types which can be used for better abstraction of
shader code. You can declare them at the global scope like:

``` glsl
struct PointLight {
    vec3 position;
    vec3 color;
    float intensity;
};
```

After declaration, you can instantiate and initialize them like:

``` glsl
void fragment()
{
    PointLight light;
    light.position = vec3(0.0);
    light.color = vec3(1.0, 0.0, 0.0);
    light.intensity = 0.5;
}
```

Or use struct constructor for same purpose:

``` glsl
PointLight light = PointLight(vec3(0.0), vec3(1.0, 0.0, 0.0), 0.5);
```

Structs may contain other struct or array, you can also instance them as
global constant:

``` glsl
shader_type spatial;

...

struct Scene {
    PointLight lights[2];
};

const Scene scene = Scene(PointLight[2](PointLight(vec3(0.0, 0.0, 0.0), vec3(1.0, 0.0, 0.0), 1.0), PointLight(vec3(0.0, 0.0, 0.0), vec3(1.0, 0.0, 0.0), 1.0)));

void fragment()
{
    ALBEDO = scene.lights[0].color;
}
```

You can also pass them to functions:

``` glsl
shader_type canvas_item;

...

Scene construct_scene(PointLight light1, PointLight light2) {
    return Scene({light1, light2});
}

void fragment()
{
    COLOR.rgb = construct_scene(PointLight(vec3(0.0, 0.0, 0.0), vec3(1.0, 0.0, 0.0), 1.0), PointLight(vec3(0.0, 0.0, 0.0), vec3(1.0, 0.0, 1.0), 1.0)).lights[0].color;
}
```

## Operators

Godot shading language supports the same set of operators as GLSL ES
3.0. Below is the list of them in precedence order:

|             |                        |                      |
|-------------|------------------------|----------------------|
| Precedence  | Class                  | Operator             |
| 1 (highest) | parenthetical grouping | **()**               |
| 2           | unary                  | **+, -, !, \~**      |
| 3           | multiplicative         | **/, \*, %**         |
| 4           | additive               | **+, -**             |
| 5           | bit-wise shift         | **\<\<, \>\>**       |
| 6           | relational             | **\<, \>, \<=, \>=** |
| 7           | equality               | **==, !=**           |
| 8           | bit-wise AND           | **&**                |
| 9           | bit-wise exclusive OR  | **\^**               |
| 10          | bit-wise inclusive OR  | **\|**               |
| 11          | logical AND            | **&&**               |
| 12 (lowest) | logical inclusive OR   | **\|\|**             |

## Flow control

Godot Shading language supports the most common types of flow control:

``` glsl
// `if` and `else`.
if (cond) {

} else {

}

// Ternary operator.
// This is an expression that behaves like `if`/`else` and returns the value.
// If `cond` evaluates to `true`, `result` will be `9`.
// Otherwise, `result` will be `5`.
int result = cond ? 9 : 5;

// `switch`.
switch (i) { // `i` should be a signed integer expression.
    case -1:
        break;
    case 0:
        return; // `break` or `return` to avoid running the next `case`.
    case 1: // Fallthrough (no `break` or `return`): will run the next `case`.
    case 2:
        break;
    //...
    default: // Only run if no `case` above matches. Optional.
        break;
}

// `for` loop. Best used when the number of elements to iterate on
// is known in advance.
for (int i = 0; i < 10; i++) {

}

// `while` loop. Best used when the number of elements to iterate on
// is not known in advance.
while (cond) {

}

// `do while`. Like `while`, but always runs at least once even if `cond`
// never evaluates to `true`.
do {

} while (cond);
```

Keep in mind that in modern GPUs, an infinite loop can exist and can
freeze your application (including editor). Godot can\'t protect you
from this, so be careful not to make this mistake!

Also, when comparing floating-point values against a number, make sure
to compare them against a *range* instead of an exact number.

A comparison like `if (value == 0.3)` may not evaluate to `true`.
Floating-point math is often approximate and can defy expectations. It
can also behave differently depending on the hardware.

**Don\'t** do this.

``` glsl
float value = 0.1 + 0.2;

// May not evaluate to `true`!
if (value == 0.3) {
    // ...
}
```

Instead, always perform a range comparison with an epsilon value. The
larger the floating-point number (and the less precise the
floating-point number), the larger the epsilon value should be.

``` glsl
const float EPSILON = 0.0001;
if (value >= 0.3 - EPSILON && value <= 0.3 + EPSILON) {
    // ...
}
```

See [floating-point-gui.de](https://floating-point-gui.de/) for more
information.

## Discarding

Fragment, light, and custom functions (called from fragment or light)
can use the `discard` keyword. If used, the fragment is discarded and
nothing is written.

Beware that `discard` has a performance cost when used, as it will
prevent the depth prepass from being effective on any surfaces using the
shader. Also, a discarded pixel still needs to be rendered in the vertex
shader, which means a shader that uses `discard` on all of its pixels is
still more expensive to render compared to not rendering any object in
the first place.

## Functions

It is possible to define functions in a Godot shader. They use the
following syntax:

``` glsl
ret_type func_name(args) {
    return ret_type; // if returning a value
}

// a more specific example:

int sum2(int a, int b) {
    return a + b;
}
```

You can only use functions that have been defined above (higher in the
editor) the function from which you are calling them. Redefining a
function that has already been defined above (or is a built-in function
name) will cause an error.

Function arguments can have special qualifiers:

- **in**: Means the argument is only for reading (default).
- **out**: Means the argument is only for writing.
- **inout**: Means the argument is fully passed via reference.
- **const**: Means the argument is a constant and cannot be changed, may
  be combined with **in** qualifier.

Example below:

``` glsl
void sum2(int a, int b, inout int result) {
    result = a + b;
}
```

Function overloading is supported. You can define multiple functions
with the same name, but different arguments. Note that [implicit
casting](#casting) in overloaded function calls is not allowed, such as
from `int` to `float` (`1` to `1.0`).

``` glsl
vec3 get_color(int t) {
    return vec3(1, 0, 0); // Red color.
}
vec3 get_color(float t) {
    return vec3(0, 1, 0); // Green color.
}
void fragment() {
    vec3 red = get_color(1);
    vec3 green = get_color(1.0);
}
```

## Varyings {#doc_shading_language_varyings}

To send data from the vertex to the fragment (or light) processor
function, *varyings* are used. They are set for every primitive vertex
in the *vertex processor*, and the value is interpolated for every pixel
in the *fragment processor*.

``` glsl
shader_type spatial;

varying vec3 some_color;

void vertex() {
    some_color = NORMAL; // Make the normal the color.
}

void fragment() {
    ALBEDO = some_color;
}

void light() {
    DIFFUSE_LIGHT = some_color * 100; // optionally
}
```

Varying can also be an array:

``` glsl
shader_type spatial;

varying float var_arr[3];

void vertex() {
    var_arr[0] = 1.0;
    var_arr[1] = 0.0;
}

void fragment() {
    ALBEDO = vec3(var_arr[0], var_arr[1], var_arr[2]); // red color
}
```

It\'s also possible to send data from *fragment* to *light* processors
using *varying* keyword. To do so you can assign it in the *fragment*
and later use it in the *light* function.

``` glsl
shader_type spatial;

varying vec3 some_light;

void fragment() {
    some_light = ALBEDO * 100.0; // Make a shining light.
}

void light() {
    DIFFUSE_LIGHT = some_light;
}
```

Note that varying may not be assigned in custom functions or a *light
processor* function like:

``` glsl
shader_type spatial;

varying float test;

void foo() {
    test = 0.0; // Error.
}

void vertex() {
    test = 0.0;
}

void light() {
    test = 0.0; // Error too.
}
```

This limitation was introduced to prevent incorrect usage before
initialization.

## Interpolation qualifiers

Certain values are interpolated during the shading pipeline. You can
modify how these interpolations are done by using *interpolation
qualifiers*.

``` glsl
shader_type spatial;

varying flat vec3 our_color;

void vertex() {
    our_color = COLOR.rgb;
}

void fragment() {
    ALBEDO = our_color;
}
```

There are two possible interpolation qualifiers:

| Qualifier | Description |
|----|----|
| **flat** | The value is not interpolated. |
| **smooth** | The value is interpolated in a perspective-correct fashion. This is the default. |

## Uniforms

Passing values to shaders is possible. These are global to the whole
shader and are called *uniforms*. When a shader is later assigned to a
material, the uniforms will appear as editable parameters in it.
Uniforms can\'t be written from within the shader. Any GLSL type except
for `void` can be a uniform.

``` glsl
shader_type spatial;

uniform float some_value;

uniform vec3 colors[3];
```

You can set uniforms in the editor in the material. Or you can set them
through GDScript:

``` gdscript
material.set_shader_parameter("some_value", some_value)

material.set_shader_parameter("colors", [Vector3(1, 0, 0), Vector3(0, 1, 0), Vector3(0, 0, 1)])
```

> [!NOTE]
> The first argument to `set_shader_parameter` is the name of the
> uniform in the shader. It must match *exactly* to the name of the
> uniform in the shader or else it will not be recognized.

> [!NOTE]
> There is a limit to the total size of shader uniforms that you can use
> in a single shader. On most desktop platforms, this limit is `65536`
> bytes, or 4096 `vec4` uniforms. On mobile platforms, the limit is
> typically `16384` bytes, or 1024 `vec4` uniforms. Vector uniforms
> smaller than a `vec4`, such as `vec2` or `vec3`, are padded to the
> size of a `vec4`. Scalar uniforms such as `int` or `float` are not
> padded, and `bool` is padded to the size of an `int`.
>
> Arrays count as the total size of their contents. If you need a
> uniform array that is larger than this limit, consider packing the
> data into a texture instead, since the *contents* of a texture do not
> count towards this limit, only the size of the sampler uniform.

### Uniform hints

Godot provides optional uniform hints to make the compiler understand
what the uniform is used for, and how the editor should allow users to
modify it.

``` glsl
shader_type spatial;

uniform vec4 color : source_color;
uniform float amount : hint_range(0, 1);
uniform vec4 other_color : source_color = vec4(1.0); // Default values go after the hint.
uniform sampler2D image : source_color;
```

::: {.admonition}
Source Color

Any texture which contains *sRGB color data* requires a `source_color`
hint in order to be correctly sampled. This is because Godot renders in
linear color space, but some textures contain sRGB color data. If this
hint is not used, the texture will appear washed out.

Albedo and color textures should typically have a `source_color` hint.
Normal, roughness, metallic, and height textures typically do not need a
`source_color` hint.

Using `source_color` hint is required in the Forward+ and Mobile
renderers, and in `canvas_item` shaders when
`HDR 2D<class_ProjectSettings_property_rendering/viewport/hdr_2d>`{.interpreted-text
role="ref"} is enabled. The `source_color` hint is optional for the
Compatibility renderer, and for `canvas_item` shaders if `HDR 2D` is
disabled. However, it is recommended to always use the `source_color`
hint, because it works even if you change renderers or disable `HDR 2D`.
:::

Full list of uniform hints below:

| Type | Hint | Description |
|----|----|----|
| **vec3, vec4** | source_color | Used as color. |
| **int, float** | hint_range(min, max\[, step\]) | Restricted to values in a range (with min/max/step). |
| **sampler2D** | source_color | Used as albedo color. |
| **sampler2D** | hint_normal | Used as normalmap. |
| **sampler2D** | hint_default_white | As value or albedo color, default to opaque white. |
| **sampler2D** | hint_default_black | As value or albedo color, default to opaque black. |
| **sampler2D** | hint_default_transparent | As value or albedo color, default to transparent black. |
| **sampler2D** | hint_anisotropy | As flowmap, default to right. |
| **sampler2D** | hint_roughness\[\_r, \_g, \_b, \_a, \_normal, \_gray\] | Used for roughness limiter on import (attempts reducing specular aliasing). `_normal` is a normal map that guides the roughness limiter, with roughness increasing in areas that have high-frequency detail. |
| **sampler2D** | filter\[\_nearest, \_linear\]\[\_mipmap\]\[\_anisotropic\] | Enabled specified texture filtering. |
| **sampler2D** | repeat\[\_enable, \_disable\] | Enabled texture repeating. |
| **sampler2D** | hint_screen_texture | Texture is the screen texture. |
| **sampler2D** | hint_depth_texture | Texture is the depth texture. |
| **sampler2D** | hint_normal_roughness_texture | Texture is the normal roughness texture (only supported in Forward+). |

GDScript uses different variable types than GLSL does, so when passing
variables from GDScript to shaders, Godot converts the type
automatically. Below is a table of the corresponding types:

<table style="width:99%;">
<colgroup>
<col style="width: 20%" />
<col style="width: 23%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr>
<th>GLSL type</th>
<th>GDScript type</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>bool</strong></td>
<td><strong>bool</strong></td>
<td></td>
</tr>
<tr>
<td><strong>bvec2</strong></td>
<td><strong>int</strong></td>
<td><p>Bitwise packed int where bit 0 (LSB) corresponds to x.</p>
<p>For example, a bvec2 of (bx, by) could be created in the following
way:</p>
<pre class="gdscript"><code>bvec2_input: int = (int(bx)) | (int(by) &lt;&lt; 1)</code></pre></td>
</tr>
<tr>
<td><strong>bvec3</strong></td>
<td><strong>int</strong></td>
<td>Bitwise packed int where bit 0 (LSB) corresponds to x.</td>
</tr>
<tr>
<td><strong>bvec4</strong></td>
<td><strong>int</strong></td>
<td>Bitwise packed int where bit 0 (LSB) corresponds to x.</td>
</tr>
<tr>
<td><strong>int</strong></td>
<td><strong>int</strong></td>
<td></td>
</tr>
<tr>
<td><strong>ivec2</strong></td>
<td><strong>Vector2i</strong></td>
<td></td>
</tr>
<tr>
<td><strong>ivec3</strong></td>
<td><strong>Vector3i</strong></td>
<td></td>
</tr>
<tr>
<td><strong>ivec4</strong></td>
<td><strong>Vector4i</strong></td>
<td></td>
</tr>
<tr>
<td><strong>uint</strong></td>
<td><strong>int</strong></td>
<td></td>
</tr>
<tr>
<td><strong>uvec2</strong></td>
<td><strong>Vector2i</strong></td>
<td></td>
</tr>
<tr>
<td><strong>uvec3</strong></td>
<td><strong>Vector3i</strong></td>
<td></td>
</tr>
<tr>
<td><strong>uvec4</strong></td>
<td><strong>Vector4i</strong></td>
<td></td>
</tr>
<tr>
<td><strong>float</strong></td>
<td><strong>float</strong></td>
<td></td>
</tr>
<tr>
<td><strong>vec2</strong></td>
<td><strong>Vector2</strong></td>
<td></td>
</tr>
<tr>
<td><strong>vec3</strong></td>
<td><strong>Vector3</strong>, <strong>Color</strong></td>
<td>When Color is used, it will be interpreted as (r, g, b).</td>
</tr>
<tr>
<td><strong>vec4</strong></td>
<td><strong>Vector4</strong>, <strong>Color</strong>,
<strong>Rect2</strong>, <strong>Plane</strong>,
<strong>Quaternion</strong></td>
<td><p>When Color is used, it will be interpreted as (r, g, b, a).</p>
<p>When Rect2 is used, it will be interpreted as (position.x,
position.y, size.x, size.y).</p>
<p>When Plane is used it will be interpreted as (normal.x, normal.y,
normal.z, d).</p></td>
</tr>
<tr>
<td><strong>mat2</strong></td>
<td><strong>Transform2D</strong></td>
<td></td>
</tr>
<tr>
<td><strong>mat3</strong></td>
<td><strong>Basis</strong></td>
<td></td>
</tr>
<tr>
<td><strong>mat4</strong></td>
<td><strong>Projection</strong>, <strong>Transform3D</strong></td>
<td>When a Transform3D is used, the w Vector is set to the
identity.</td>
</tr>
<tr>
<td><strong>sampler2D</strong></td>
<td><strong>Texture2D</strong></td>
<td></td>
</tr>
<tr>
<td><strong>isampler2D</strong></td>
<td><strong>Texture2D</strong></td>
<td></td>
</tr>
<tr>
<td><strong>usampler2D</strong></td>
<td><strong>Texture2D</strong></td>
<td></td>
</tr>
<tr>
<td><strong>sampler2DArray</strong></td>
<td><strong>Texture2DArray</strong></td>
<td></td>
</tr>
<tr>
<td><strong>isampler2DArray</strong></td>
<td><strong>Texture2DArray</strong></td>
<td></td>
</tr>
<tr>
<td><strong>usampler2DArray</strong></td>
<td><strong>Texture2DArray</strong></td>
<td></td>
</tr>
<tr>
<td><strong>sampler3D</strong></td>
<td><strong>Texture3D</strong></td>
<td></td>
</tr>
<tr>
<td><strong>isampler3D</strong></td>
<td><strong>Texture3D</strong></td>
<td></td>
</tr>
<tr>
<td><strong>usampler3D</strong></td>
<td><strong>Texture3D</strong></td>
<td></td>
</tr>
<tr>
<td><strong>samplerCube</strong></td>
<td><strong>Cubemap</strong></td>
<td>See <code class="interpreted-text"
role="ref">doc_importing_images_changing_import_type</code> for
instructions on importing cubemaps for use in Godot.</td>
</tr>
<tr>
<td><strong>samplerCubeArray</strong></td>
<td><strong>CubemapArray</strong></td>
<td>Only supported in Forward+ and Mobile, not Compatibility.</td>
</tr>
</tbody>
</table>

> [!NOTE]
> Be careful when setting shader uniforms from GDScript, no error will
> be thrown if the type does not match. Your shader will just exhibit
> undefined behavior.

> [!WARNING]
> As with the last note, no error will be thrown if the typing does not
> match while setting a shader uniform, this unintuitively includes
> setting a (GDscript) 64 bit int/float into a Godot shader language
> int/float (32 bit). This may lead to unintentional consequences in
> cases where high precision is required.

Uniforms can also be assigned default values:

``` glsl
shader_type spatial;

uniform vec4 some_vector = vec4(0.0);
uniform vec4 some_color : source_color = vec4(1.0);
```

Note that when adding a default value and a hint, the default value goes
after the hint.

If you need to make multiple uniforms to be grouped in the specific
category of an inspector, you can use a [group_uniform]{.title-ref}
keyword like:

``` glsl
group_uniforms MyGroup;
uniform sampler2D test;
```

You can close the group by using:

``` glsl
group_uniforms;
```

The syntax also supports subgroups (it\'s not mandatory to declare the
base group before this):

``` glsl
group_uniforms MyGroup.MySubgroup;
```

### Global uniforms {#doc_shading_language_global_uniforms}

Sometimes, you want to modify a parameter in many different shaders at
once. With a regular uniform, this takes a lot of work as all these
shaders need to be tracked and the uniform needs to be set for each of
them. Global uniforms allow you to create and update uniforms that will
be available in all shaders, in every shader type (`canvas_item`,
`spatial`, `particles`, `sky` and `fog`).

Global uniforms are especially useful for environmental effects that
affect many objects in a scene, like having foliage bend when the player
is nearby, or having objects move with the wind.

To create a global uniform, open the **Project Settings** then go to the
**Shader Globals** tab. Specify a name for the uniform (case-sensitive)
and a type, then click **Add** in the top-right corner of the dialog.
You can then edit the value assigned to the uniform by clicking the
value in the list of uniforms:

<figure class="align-center">
<img src="img/shading_language_adding_global_uniforms.webp"
alt="img/shading_language_adding_global_uniforms.webp" />
<figcaption>Adding a global uniform in the Shader Globals tab of the
Project Settings</figcaption>
</figure>

After creating a global uniform, you can use it in a shader as follows:

``` glsl
shader_type canvas_item;

global uniform vec4 my_color;

void fragment() {
    COLOR = my_color.rgb;
}
```

Note that the global uniform *must* exist in the Project Settings at the
time the shader is saved, or compilation will fail. While you can assign
a default value using `global uniform vec4 my_color = ...` in the shader
code, it will be ignored as the global uniform must always be defined in
the Project Settings anyway.

To change the value of a global uniform at run-time, use the
`RenderingServer.global_shader_parameter_set <class_RenderingServer_method_global_shader_parameter_set>`{.interpreted-text
role="ref"} method in a script:

``` gdscript
RenderingServer.global_shader_parameter_set("my_color", Color(0.3, 0.6, 1.0))
```

Assigning global uniform values can be done as many times as desired
without impacting performance, as setting data doesn\'t require
synchronization between the CPU and GPU.

You can also add or remove global uniforms at run-time:

``` gdscript
RenderingServer.global_shader_parameter_add("my_color", RenderingServer.GLOBAL_VAR_TYPE_COLOR, Color(0.3, 0.6, 1.0))
RenderingServer.global_shader_parameter_remove("my_color")
```

Adding or removing global uniforms at run-time has a performance cost,
although it\'s not as pronounced compared to getting global uniform
values from a script (see the warning below).

> [!WARNING]
> While you *can* query the value of a global uniform at run-time in a
> script using
> `RenderingServer.global_shader_parameter_get("uniform_name")`, this
> has a large performance penalty as the rendering thread needs to
> synchronize with the calling thread.
>
> Therefore, it\'s not recommended to read global shader uniform values
> continuously in a script. If you need to read values in a script after
> setting them, consider creating an
> `autoload <doc_singletons_autoload>`{.interpreted-text role="ref"}
> where you store the values you need to query at the same time you\'re
> setting them as global uniforms.

### Per-instance uniforms {#doc_shading_language_per_instance_uniforms}

> [!NOTE]
> Per-instance uniforms are only available in `spatial` (3D) shaders.

Sometimes, you want to modify a parameter on each node using the
material. As an example, in a forest full of trees, when you want each
tree to have a slightly different color that is editable by hand.
Without per-instance uniforms, this requires creating a unique material
for each tree (each with a slightly different hue). This makes material
management more complex, and also has a performance overhead due to the
scene requiring more unique material instances. Vertex colors could also
be used here, but they\'d require creating unique copies of the mesh for
each different color, which also has a performance overhead.

Per-instance uniforms are set on each GeometryInstance3D, rather than on
each Material instance. Take this into account when working with meshes
that have multiple materials assigned to them, or MultiMesh setups.

``` glsl
shader_type spatial;

// Provide a hint to edit as a color. Optionally, a default value can be provided.
// If no default value is provided, the type's default is used (e.g. opaque black for colors).
instance uniform vec4 my_color : source_color = vec4(1.0, 0.5, 0.0, 1.0);

void fragment() {
    ALBEDO = my_color.rgb;
}
```

After saving the shader, you can change the per-instance uniform\'s
value using the inspector:

<figure class="align-center">
<img src="img/shading_language_per_instance_uniforms_inspector.webp"
alt="img/shading_language_per_instance_uniforms_inspector.webp" />
<figcaption>Setting a per-instance uniform's value in the
GeometryInstance3D section of the inspector</figcaption>
</figure>

Per-instance uniform values can also be set at run-time using
`set_instance_shader_parameter <class_GeometryInstance3D_method_set_instance_shader_parameter>`{.interpreted-text
role="ref"} method on a node that inherits from
`class_GeometryInstance3D`{.interpreted-text role="ref"}:

``` gdscript
$MeshInstance3D.set_instance_shader_parameter("my_color", Color(0.3, 0.6, 1.0))
```

When using per-instance uniforms, there are some restrictions you should
be aware of:

- **Per-instance uniforms do not support textures**, only regular scalar
  and vector types. As a workaround, you can pass a texture array as a
  regular uniform, then pass the index of the texture to be drawn using
  a per-instance uniform.
- There is a practical maximum limit of 16 instance uniforms per shader.
- If your mesh uses multiple materials, the parameters for the first
  mesh material found will \"win\" over the subsequent ones, unless they
  have the same name, index *and* type. In this case, all parameters are
  affected correctly.
- If you run into the above situation, you can avoid clashes by manually
  specifying the index (0-15) of the instance uniform by using the
  `instance_index` hint:

``` glsl
instance uniform vec4 my_color : source_color, instance_index(5);
```

## Built-in variables

A large number of built-in variables are available, like `UV`, `COLOR`
and `VERTEX`. What variables are available depends on the type of shader
(`spatial`, `canvas_item` or `particle`) and the function used
(`vertex`, `fragment` or `light`). For a list of the built-in variables
that are available, please see the corresponding pages:

- `Spatial shaders <doc_spatial_shader>`{.interpreted-text role="ref"}
- `Canvas item shaders <doc_canvas_item_shader>`{.interpreted-text
  role="ref"}
- `Particle shaders <doc_particle_shader>`{.interpreted-text role="ref"}
- `Sky shaders <doc_sky_shader>`{.interpreted-text role="ref"}
- `Fog shaders <doc_fog_shader>`{.interpreted-text role="ref"}

## Built-in functions

A large number of built-in functions are supported, conforming to GLSL
ES 3.0. When vec_type (float), vec_int_type, vec_uint_type,
vec_bool_type nomenclature is used, it can be scalar or vector.

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr>
<th>Function</th>
<th>Description / Return value</th>
</tr>
</thead>
<tbody>
<tr>
<td>vec_type <strong>radians</strong> (vec_type degrees)</td>
<td>Convert degrees to radians.</td>
</tr>
<tr>
<td>vec_type <strong>degrees</strong> (vec_type radians)</td>
<td>Convert radians to degrees.</td>
</tr>
<tr>
<td>vec_type <strong>sin</strong> (vec_type x)</td>
<td>Sine.</td>
</tr>
<tr>
<td>vec_type <strong>cos</strong> (vec_type x)</td>
<td>Cosine.</td>
</tr>
<tr>
<td>vec_type <strong>tan</strong> (vec_type x)</td>
<td>Tangent.</td>
</tr>
<tr>
<td>vec_type <strong>asin</strong> (vec_type x)</td>
<td>Arcsine.</td>
</tr>
<tr>
<td>vec_type <strong>acos</strong> (vec_type x)</td>
<td>Arccosine.</td>
</tr>
<tr>
<td>vec_type <strong>atan</strong> (vec_type y_over_x)</td>
<td>Arctangent.</td>
</tr>
<tr>
<td>vec_type <strong>atan</strong> (vec_type y, vec_type x)</td>
<td>Arctangent.</td>
</tr>
<tr>
<td>vec_type <strong>sinh</strong> (vec_type x)</td>
<td>Hyperbolic sine.</td>
</tr>
<tr>
<td>vec_type <strong>cosh</strong> (vec_type x)</td>
<td>Hyperbolic cosine.</td>
</tr>
<tr>
<td>vec_type <strong>tanh</strong> (vec_type x)</td>
<td>Hyperbolic tangent.</td>
</tr>
<tr>
<td>vec_type <strong>asinh</strong> (vec_type x)</td>
<td>Inverse hyperbolic sine.</td>
</tr>
<tr>
<td>vec_type <strong>acosh</strong> (vec_type x)</td>
<td>Inverse hyperbolic cosine.</td>
</tr>
<tr>
<td>vec_type <strong>atanh</strong> (vec_type x)</td>
<td>Inverse hyperbolic tangent.</td>
</tr>
<tr>
<td>vec_type <strong>pow</strong> (vec_type x, vec_type y)</td>
<td>Power (undefined if <code>x</code> &lt; 0 or if <code>x</code> == 0
and <code>y</code> &lt;= 0).</td>
</tr>
<tr>
<td>vec_type <strong>exp</strong> (vec_type x)</td>
<td>Base-e exponential.</td>
</tr>
<tr>
<td>vec_type <strong>exp2</strong> (vec_type x)</td>
<td>Base-2 exponential.</td>
</tr>
<tr>
<td>vec_type <strong>log</strong> (vec_type x)</td>
<td>Natural logarithm.</td>
</tr>
<tr>
<td>vec_type <strong>log2</strong> (vec_type x)</td>
<td>Base-2 logarithm.</td>
</tr>
<tr>
<td>vec_type <strong>sqrt</strong> (vec_type x)</td>
<td>Square root.</td>
</tr>
<tr>
<td>vec_type <strong>inversesqrt</strong> (vec_type x)</td>
<td>Inverse square root.</td>
</tr>
<tr>
<td><p>vec_type <strong>abs</strong> (vec_type x)</p>
<p>ivec_type <strong>abs</strong> (ivec_type x)</p></td>
<td>Absolute value (returns positive value if negative).</td>
</tr>
<tr>
<td><p>vec_type <strong>sign</strong> (vec_type x)</p>
<p>ivec_type <strong>sign</strong> (ivec_type x)</p></td>
<td>Sign (returns <code>1.0</code> if positive, <code>-1.0</code> if
negative, <code>0.0</code> if zero).</td>
</tr>
<tr>
<td>vec_type <strong>floor</strong> (vec_type x)</td>
<td>Round to the integer below.</td>
</tr>
<tr>
<td>vec_type <strong>round</strong> (vec_type x)</td>
<td>Round to the nearest integer.</td>
</tr>
<tr>
<td>vec_type <strong>roundEven</strong> (vec_type x)</td>
<td>Round to the nearest even integer.</td>
</tr>
<tr>
<td>vec_type <strong>trunc</strong> (vec_type x)</td>
<td>Truncation.</td>
</tr>
<tr>
<td>vec_type <strong>ceil</strong> (vec_type x)</td>
<td>Round to the integer above.</td>
</tr>
<tr>
<td>vec_type <strong>fract</strong> (vec_type x)</td>
<td>Fractional (returns <code>x - floor(x)</code>).</td>
</tr>
<tr>
<td><p>vec_type <strong>mod</strong> (vec_type x, vec_type y)</p>
<p>vec_type <strong>mod</strong> (vec_type x, float y)</p></td>
<td>Modulo (division remainder).</td>
</tr>
<tr>
<td>vec_type <strong>modf</strong> (vec_type x, out vec_type i)</td>
<td>Fractional of <code>x</code>, with <code>i</code> as integer
part.</td>
</tr>
<tr>
<td>vec_type <strong>min</strong> (vec_type a, vec_type b)</td>
<td>Lowest value between <code>a</code> and <code>b</code>.</td>
</tr>
<tr>
<td>vec_type <strong>max</strong> (vec_type a, vec_type b)</td>
<td>Highest value between <code>a</code> and <code>b</code>.</td>
</tr>
<tr>
<td>vec_type <strong>clamp</strong> (vec_type x, vec_type min, vec_type
max)</td>
<td>Clamp <code>x</code> between <code>min</code> and <code>max</code>
(inclusive).</td>
</tr>
<tr>
<td><p>float <strong>mix</strong> (float a, float b, float c)</p>
<p>vec_type <strong>mix</strong> (vec_type a, vec_type b, float c)</p>
<p>vec_type <strong>mix</strong> (vec_type a, vec_type b, bvec_type
c)</p></td>
<td>Linear interpolate between <code>a</code> and <code>b</code> by
<code>c</code>.</td>
</tr>
<tr>
<td>vec_type <strong>fma</strong> (vec_type a, vec_type b, vec_type
c)</td>
<td>Performs a fused multiply-add operation: <code>(a * b + c)</code>
(faster than doing it manually).</td>
</tr>
<tr>
<td>vec_type <strong>step</strong> (vec_type a, vec_type b)</td>
<td><code>b[i] &lt; a[i] ? 0.0 : 1.0</code>.</td>
</tr>
<tr>
<td>vec_type <strong>step</strong> (float a, vec_type b)</td>
<td><code>b[i] &lt; a ? 0.0 : 1.0</code>.</td>
</tr>
<tr>
<td><p>vec_type <strong>smoothstep</strong> (vec_type a, vec_type b,
vec_type c)</p>
<p>vec_type <strong>smoothstep</strong> (float a, float b, vec_type
c)</p></td>
<td>Hermite interpolate between <code>a</code> and <code>b</code> by
<code>c</code>.</td>
</tr>
<tr>
<td>bvec_type <strong>isnan</strong> (vec_type x)</td>
<td>Returns <code>true</code> if scalar or vector component is
<code>NaN</code>.</td>
</tr>
<tr>
<td>bvec_type <strong>isinf</strong> (vec_type x)</td>
<td>Returns <code>true</code> if scalar or vector component is
<code>INF</code>.</td>
</tr>
<tr>
<td>ivec_type <strong>floatBitsToInt</strong> (vec_type x)</td>
<td>Float-&gt;Int bit copying, no conversion.</td>
</tr>
<tr>
<td>uvec_type <strong>floatBitsToUint</strong> (vec_type x)</td>
<td>Float-&gt;UInt bit copying, no conversion.</td>
</tr>
<tr>
<td>vec_type <strong>intBitsToFloat</strong> (ivec_type x)</td>
<td>Int-&gt;Float bit copying, no conversion.</td>
</tr>
<tr>
<td>vec_type <strong>uintBitsToFloat</strong> (uvec_type x)</td>
<td>UInt-&gt;Float bit copying, no conversion.</td>
</tr>
<tr>
<td>float <strong>length</strong> (vec_type x)</td>
<td>Vector length.</td>
</tr>
<tr>
<td>float <strong>distance</strong> (vec_type a, vec_type b)</td>
<td>Distance between vectors i.e <code>length(a - b)</code>.</td>
</tr>
<tr>
<td>float <strong>dot</strong> (vec_type a, vec_type b)</td>
<td>Dot product.</td>
</tr>
<tr>
<td>vec3 <strong>cross</strong> (vec3 a, vec3 b)</td>
<td>Cross product.</td>
</tr>
<tr>
<td>vec_type <strong>normalize</strong> (vec_type x)</td>
<td>Normalize to unit length.</td>
</tr>
<tr>
<td>vec3 <strong>reflect</strong> (vec3 I, vec3 N)</td>
<td>Reflect.</td>
</tr>
<tr>
<td>vec3 <strong>refract</strong> (vec3 I, vec3 N, float eta)</td>
<td>Refract.</td>
</tr>
<tr>
<td>vec_type <strong>faceforward</strong> (vec_type N, vec_type I,
vec_type Nref)</td>
<td>If <code>dot(Nref, I)</code> &lt; 0, return <code>N</code>,
otherwise <code>-N</code>.</td>
</tr>
<tr>
<td>mat_type <strong>matrixCompMult</strong> (mat_type x, mat_type
y)</td>
<td>Matrix component multiplication.</td>
</tr>
<tr>
<td>mat_type <strong>outerProduct</strong> (vec_type column, vec_type
row)</td>
<td>Matrix outer product.</td>
</tr>
<tr>
<td>mat_type <strong>transpose</strong> (mat_type m)</td>
<td>Transpose matrix.</td>
</tr>
<tr>
<td>float <strong>determinant</strong> (mat_type m)</td>
<td>Matrix determinant.</td>
</tr>
<tr>
<td>mat_type <strong>inverse</strong> (mat_type m)</td>
<td>Inverse matrix.</td>
</tr>
<tr>
<td>bvec_type <strong>lessThan</strong> (vec_type x, vec_type y)</td>
<td>Bool vector comparison on &lt; int/uint/float vectors.</td>
</tr>
<tr>
<td>bvec_type <strong>greaterThan</strong> (vec_type x, vec_type y)</td>
<td>Bool vector comparison on &gt; int/uint/float vectors.</td>
</tr>
<tr>
<td>bvec_type <strong>lessThanEqual</strong> (vec_type x, vec_type
y)</td>
<td>Bool vector comparison on &lt;= int/uint/float vectors.</td>
</tr>
<tr>
<td>bvec_type <strong>greaterThanEqual</strong> (vec_type x, vec_type
y)</td>
<td>Bool vector comparison on &gt;= int/uint/float vectors.</td>
</tr>
<tr>
<td>bvec_type <strong>equal</strong> (vec_type x, vec_type y)</td>
<td>Bool vector comparison on == int/uint/float vectors.</td>
</tr>
<tr>
<td>bvec_type <strong>notEqual</strong> (vec_type x, vec_type y)</td>
<td>Bool vector comparison on != int/uint/float vectors.</td>
</tr>
<tr>
<td>bool <strong>any</strong> (bvec_type x)</td>
<td><code>true</code> if any component is <code>true</code>,
<code>false</code> otherwise.</td>
</tr>
<tr>
<td>bool <strong>all</strong> (bvec_type x)</td>
<td><code>true</code> if all components are <code>true</code>,
<code>false</code> otherwise.</td>
</tr>
<tr>
<td>bvec_type <strong>not</strong> (bvec_type x)</td>
<td>Invert boolean vector.</td>
</tr>
<tr>
<td><p>ivec2 <strong>textureSize</strong> (gsampler2D s, int lod)</p>
<p>ivec3 <strong>textureSize</strong> (gsampler2DArray s, int lod)</p>
<p>ivec3 <strong>textureSize</strong> (gsampler3D s, int lod)</p>
<p>ivec2 <strong>textureSize</strong> (samplerCube s, int lod)</p>
<p>ivec2 <strong>textureSize</strong> (samplerCubeArray s, int
lod)</p></td>
<td><p>Get the size of a texture.</p>
<p>The LOD defines which mipmap level is used. An LOD value of
<code>0</code> will use the full resolution texture.</p></td>
</tr>
<tr>
<td><p>vec2 <strong>textureQueryLod</strong> (gsampler2D s, vec2 p)</p>
<p>vec3 <strong>textureQueryLod</strong> (gsampler2DArray s, vec2 p)</p>
<p>vec2 <strong>textureQueryLod</strong> (gsampler3D s, vec3 p)</p>
<p>vec2 <strong>textureQueryLod</strong> (samplerCube s, vec3
p)</p></td>
<td>Compute the level-of-detail that would be used to sample from a
texture. The <code>x</code> component of the resulted value is the
mipmap array that would be accessed. The <code>y</code> component is
computed level-of-detail relative to the base level (regardless of the
mipmap levels of the texture).</td>
</tr>
<tr>
<td><p>int <strong>textureQueryLevels</strong> (gsampler2D s)</p>
<p>int <strong>textureQueryLevels</strong> (gsampler2DArray s)</p>
<p>int <strong>textureQueryLevels</strong> (gsampler3D s)</p>
<p>int <strong>textureQueryLevels</strong> (samplerCube s)</p></td>
<td><p>Get the number of accessible mipmap levels of a texture.</p>
<p>If the texture is unassigned to a sampler, <code>1</code> is returned
(Godot always internally assigns a texture even to an empty
sampler).</p></td>
</tr>
<tr>
<td><p>gvec4_type <strong>texture</strong> (gsampler2D s, vec2 p [,
float bias])</p>
<p>gvec4_type <strong>texture</strong> (gsampler2DArray s, vec3 p [,
float bias])</p>
<p>gvec4_type <strong>texture</strong> (gsampler3D s, vec3 p [, float
bias])</p>
<p>vec4 <strong>texture</strong> (samplerCube s, vec3 p [, float
bias])</p>
<p>vec4 <strong>texture</strong> (samplerCubeArray s, vec4 p [, float
bias])</p></td>
<td>Perform a texture read.</td>
</tr>
<tr>
<td><p>gvec4_type <strong>textureProj</strong> (gsampler2D s, vec3 p [,
float bias])</p>
<p>gvec4_type <strong>textureProj</strong> (gsampler2D s, vec4 p [,
float bias])</p>
<p>gvec4_type <strong>textureProj</strong> (gsampler3D s, vec4 p [,
float bias])</p></td>
<td>Perform a texture read with projection.</td>
</tr>
<tr>
<td><p>gvec4_type <strong>textureLod</strong> (gsampler2D s, vec2 p,
float lod)</p>
<p>gvec4_type <strong>textureLod</strong> (gsampler2DArray s, vec3 p,
float lod)</p>
<p>gvec4_type <strong>textureLod</strong> (gsampler3D s, vec3 p, float
lod)</p>
<p>vec4 <strong>textureLod</strong> (samplerCube s, vec3 p, float
lod)</p>
<p>vec4 <strong>textureLod</strong> (samplerCubeArray s, vec4 p, float
lod)</p></td>
<td><p>Perform a texture read at custom mipmap.</p>
<p>The LOD defines which mipmap level is used. An LOD value of
<code>0.0</code> will use the full resolution texture. If the texture
lacks mipmaps, all LOD values will act like <code>0.0</code>.</p></td>
</tr>
<tr>
<td><p>gvec4_type <strong>textureProjLod</strong> (gsampler2D s, vec3 p,
float lod)</p>
<p>gvec4_type <strong>textureProjLod</strong> (gsampler2D s, vec4 p,
float lod)</p>
<p>gvec4_type <strong>textureProjLod</strong> (gsampler3D s, vec4 p,
float lod)</p></td>
<td><p>Performs a texture read with projection/LOD.</p>
<p>The LOD defines which mipmap level is used. An LOD value of
<code>0.0</code> will use the full resolution texture. If the texture
lacks mipmaps, all LOD values will act like <code>0.0</code>.</p></td>
</tr>
<tr>
<td><p>gvec4_type <strong>textureGrad</strong> (gsampler2D s, vec2 p,
vec2 dPdx, vec2 dPdy)</p>
<p>gvec4_type <strong>textureGrad</strong> (gsampler2DArray s, vec3 p,
vec2 dPdx, vec2 dPdy)</p>
<p>gvec4_type <strong>textureGrad</strong> (gsampler3D s, vec3 p, vec2
dPdx, vec2 dPdy)</p>
<p>vec4 <strong>textureGrad</strong> (samplerCube s, vec3 p, vec3 dPdx,
vec3 dPdy)</p>
<p>vec4 <strong>textureGrad</strong> (samplerCubeArray s, vec3 p, vec3
dPdx, vec3 dPdy)</p></td>
<td>Performs a texture read with explicit gradients.</td>
</tr>
<tr>
<td><p>gvec4_type <strong>textureProjGrad</strong> (gsampler2D s, vec3
p, vec2 dPdx, vec2 dPdy)</p>
<p>gvec4_type <strong>textureProjGrad</strong> (gsampler2D s, vec4 p,
vec2 dPdx, vec2 dPdy)</p>
<p>gvec4_type <strong>textureProjGrad</strong> (gsampler3D s, vec4 p,
vec3 dPdx, vec3 dPdy)</p></td>
<td>Performs a texture read with projection/LOD and with explicit
gradients.</td>
</tr>
<tr>
<td><p>gvec4_type <strong>texelFetch</strong> (gsampler2D s, ivec2 p,
int lod)</p>
<p>gvec4_type <strong>texelFetch</strong> (gsampler2DArray s, ivec3 p,
int lod)</p>
<p>gvec4_type <strong>texelFetch</strong> (gsampler3D s, ivec3 p, int
lod)</p></td>
<td><p>Fetches a single texel using integer coordinates.</p>
<p>The LOD defines which mipmap level is used. An LOD value of
<code>0</code> will use the full resolution texture.</p></td>
</tr>
<tr>
<td><p>gvec4_type <strong>textureGather</strong> (gsampler2D s, vec2 p
[, int comps])</p>
<p>gvec4_type <strong>textureGather</strong> (gsampler2DArray s, vec3 p
[, int comps])</p>
<p>vec4 <strong>textureGather</strong> (samplerCube s, vec3 p [, int
comps])</p></td>
<td>Gathers four texels from a texture. Use <code>comps</code> within
range of 0..3 to define which component (x, y, z, w) is returned. If
<code>comps</code> is not provided: 0 (or x-component) is used.</td>
</tr>
<tr>
<td>vec_type <strong>dFdx</strong> (vec_type p)</td>
<td>Derivative in <code>x</code> using local differencing. Internally,
can use either <code>dFdxCoarse</code> or <code>dFdxFine</code>, but the
decision for which to use is made by the GPU driver.</td>
</tr>
<tr>
<td>vec_type <strong>dFdxCoarse</strong> (vec_type p)</td>
<td>Calculates derivative with respect to <code>x</code> window
coordinate using local differencing based on the value of <code>p</code>
for the current fragment neighbour(s), and will possibly, but not
necessarily, include the value for the current fragment. This function
is not available on <code>gl_compatibility</code> profile.</td>
</tr>
<tr>
<td>vec_type <strong>dFdxFine</strong> (vec_type p)</td>
<td>Calculates derivative with respect to <code>x</code> window
coordinate using local differencing based on the value of <code>p</code>
for the current fragment and its immediate neighbour(s). This function
is not available on <code>gl_compatibility</code> profile.</td>
</tr>
<tr>
<td>vec_type <strong>dFdy</strong> (vec_type p)</td>
<td>Derivative in <code>y</code> using local differencing. Internally,
can use either <code>dFdyCoarse</code> or <code>dFdyFine</code>, but the
decision for which to use is made by the GPU driver.</td>
</tr>
<tr>
<td>vec_type <strong>dFdyCoarse</strong> (vec_type p)</td>
<td>Calculates derivative with respect to <code>y</code> window
coordinate using local differencing based on the value of <code>p</code>
for the current fragment neighbour(s), and will possibly, but not
necessarily, include the value for the current fragment. This function
is not available on <code>gl_compatibility</code> profile.</td>
</tr>
<tr>
<td>vec_type <strong>dFdyFine</strong> (vec_type p)</td>
<td>Calculates derivative with respect to <code>y</code> window
coordinate using local differencing based on the value of <code>p</code>
for the current fragment and its immediate neighbour(s). This function
is not available on <code>gl_compatibility</code> profile.</td>
</tr>
<tr>
<td>vec_type <strong>fwidth</strong> (vec_type p)</td>
<td>Sum of absolute derivative in <code>x</code> and <code>y</code>.
This is the equivalent of using
<code>abs(dFdx(p)) + abs(dFdy(p))</code>.</td>
</tr>
<tr>
<td>vec_type <strong>fwidthCoarse</strong> (vec_type p)</td>
<td>Sum of absolute derivative in <code>x</code> and <code>y</code>.
This is the equivalent of using
<code>abs(dFdxCoarse(p)) + abs(dFdyCoarse(p))</code>. This function is
not available on <code>gl_compatibility</code> profile.</td>
</tr>
<tr>
<td>vec_type <strong>fwidthFine</strong> (vec_type p)</td>
<td>Sum of absolute derivative in <code>x</code> and <code>y</code>.
This is the equivalent of using
<code>abs(dFdxFine(p)) + abs(dFdyFine(p))</code>. This function is not
available on <code>gl_compatibility</code> profile.</td>
</tr>
<tr>
<td><p>uint <strong>packHalf2x16</strong> (vec2 v)</p>
<p>vec2 <strong>unpackHalf2x16</strong> (uint v)</p></td>
<td>Convert two 32-bit floating-point numbers into 16-bit and pack them
into a 32-bit unsigned integer and vice-versa.</td>
</tr>
<tr>
<td><p>uint <strong>packUnorm2x16</strong> (vec2 v)</p>
<p>vec2 <strong>unpackUnorm2x16</strong> (uint v)</p></td>
<td>Convert two 32-bit floating-point numbers (clamped within 0..1
range) into 16-bit and pack them into a 32-bit unsigned integer and
vice-versa.</td>
</tr>
<tr>
<td><p>uint <strong>packSnorm2x16</strong> (vec2 v)</p>
<p>vec2 <strong>unpackSnorm2x16</strong> (uint v)</p></td>
<td>Convert two 32-bit floating-point numbers (clamped within -1..1
range) into 16-bit and pack them into a 32-bit unsigned integer and
vice-versa.</td>
</tr>
<tr>
<td><p>uint <strong>packUnorm4x8</strong> (vec4 v)</p>
<p>vec4 <strong>unpackUnorm4x8</strong> (uint v)</p></td>
<td>Convert four 32-bit floating-point numbers (clamped within 0..1
range) into 8-bit and pack them into a 32-bit unsigned integer and
vice-versa.</td>
</tr>
<tr>
<td><p>uint <strong>packSnorm4x8</strong> (vec4 v)</p>
<p>vec4 <strong>unpackSnorm4x8</strong> (uint v)</p></td>
<td>Convert four 32-bit floating-point numbers (clamped within -1..1
range) into 8-bit and pack them into a 32-bit unsigned integer and
vice-versa.</td>
</tr>
<tr>
<td><p>ivec_type <strong>bitfieldExtract</strong> (ivec_type value, int
offset, int bits)</p>
<p>uvec_type <strong>bitfieldExtract</strong> (uvec_type value, int
offset, int bits)</p></td>
<td>Extracts a range of bits from an integer.</td>
</tr>
<tr>
<td><p>ivec_type <strong>bitfieldInsert</strong> (ivec_type base,
ivec_type insert, int offset, int bits)</p>
<p>uvec_type <strong>bitfieldInsert</strong> (uvec_type base, uvec_type
insert, int offset, int bits)</p></td>
<td>Insert a range of bits into an integer.</td>
</tr>
<tr>
<td><p>ivec_type <strong>bitfieldReverse</strong> (ivec_type value)</p>
<p>uvec_type <strong>bitfieldReverse</strong> (uvec_type value)</p></td>
<td>Reverse the order of bits in an integer.</td>
</tr>
<tr>
<td><p>ivec_type <strong>bitCount</strong> (ivec_type value)</p>
<p>uvec_type <strong>bitCount</strong> (uvec_type value)</p></td>
<td>Counts the number of 1 bits in an integer.</td>
</tr>
<tr>
<td><p>ivec_type <strong>findLSB</strong> (ivec_type value)</p>
<p>uvec_type <strong>findLSB</strong> (uvec_type value)</p></td>
<td>Find the index of the least significant bit set to 1 in an
integer.</td>
</tr>
<tr>
<td><p>ivec_type <strong>findMSB</strong> (ivec_type value)</p>
<p>uvec_type <strong>findMSB</strong> (uvec_type value)</p></td>
<td>Find the index of the most significant bit set to 1 in an
integer.</td>
</tr>
<tr>
<td><p>void <strong>imulExtended</strong> (ivec_type x, ivec_type y, out
ivec_type msb, out ivec_type lsb)</p>
<p>void <strong>umulExtended</strong> (uvec_type x, uvec_type y, out
uvec_type msb, out uvec_type lsb)</p></td>
<td>Multiplies two 32-bit numbers and produce a 64-bit result.
<code>x</code> - the first number. <code>y</code> - the second number.
<code>msb</code> - will contain the most significant bits.
<code>lsb</code> - will contain the least significant bits.</td>
</tr>
<tr>
<td>uvec_type <strong>uaddCarry</strong> (uvec_type x, uvec_type y, out
uvec_type carry)</td>
<td>Adds two unsigned integers and generates carry.</td>
</tr>
<tr>
<td>uvec_type <strong>usubBorrow</strong> (uvec_type x, uvec_type y, out
uvec_type borrow)</td>
<td>Subtracts two unsigned integers and generates borrow.</td>
</tr>
<tr>
<td>vec_type <strong>ldexp</strong> (vec_type x, out ivec_type exp)</td>
<td><p>Assemble a floating-point number from a value and exponent.</p>
<p>If this product is too large to be represented in the floating-point
type the result is undefined.</p></td>
</tr>
<tr>
<td>vec_type <strong>frexp</strong> (vec_type x, out ivec_type exp)</td>
<td><p>Splits a floating-point number(<code>x</code>) into significand
(in the range of [0.5, 1.0]) and an integral exponent.</p>
<p>For <code>x</code> equals zero the significand and exponent are both
zero. For <code>x</code> of infinity or NaN, the results are
undefined.</p></td>
</tr>
</tbody>
</table>
