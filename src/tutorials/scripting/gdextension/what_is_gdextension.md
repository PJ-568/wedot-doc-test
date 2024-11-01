# What is GDExtension? {#doc_what_is_gdextension}

## Introduction

**GDExtension** is a Godot-specific technology that lets the engine
interact with native [shared
libraries](https://en.wikipedia.org/wiki/Library_(computing)#Shared_libraries)
at run-time. You can use it to run native code without compiling it with
the engine.

> [!NOTE]
> GDExtension is *not* a scripting language and has no relation to
> `GDScript <doc_gdscript>`{.interpreted-text role="ref"}.

## Differences between GDExtension and C++ modules

You can use both GDExtension and
`C++ modules <doc_custom_modules_in_cpp>`{.interpreted-text role="ref"}
to run C or C++ code in a Godot project.

They also both allow you to integrate third-party libraries into Godot.
The one you should choose depends on your needs.

> [!WARNING]
> Our long-term goal is that GDExtensions targeting an earlier version
> of Godot will work in later minor versions, but not vice-versa. For
> example, a GDExtension targeting Godot 4.2 should work just fine in
> Godot 4.3, but one targeting Godot 4.3 won\'t work in Godot 4.2.
>
> However, GDExtension is currently *experimental*, which means that we
> may break compatibility in order to fix major bugs or include critical
> features. For example, GDExtensions created for Godot 4.0 aren\'t
> compatible with Godot 4.1 (see
> `updating_your_gdextension_for_godot_4_1`{.interpreted-text
> role="ref"}).

### Advantages of GDExtension

Unlike modules, GDExtension doesn\'t require compiling the engine\'s
source code, making it easier to distribute your work. It gives you
access to most of the API available to GDScript and C#, allowing you to
code game logic with full control regarding performance. It\'s ideal if
you need high-performance code you\'d like to distribute as an add-on in
the `asset library <doc_what_is_assetlib>`{.interpreted-text
role="ref"}.

Also:

- GDExtension is not limited to C and C++. Thanks to
  `third-party bindings
  <doc_what_is_gdnative_third_party_bindings>`{.interpreted-text
  role="ref"}, you can use it with many other languages.
- You can use the same compiled GDExtension library in the editor and
  exported project. With C++ modules, you have to recompile all the
  export templates you plan to use if you require its functionality at
  run-time.
- GDExtension only requires you to compile your library, not the whole
  engine. That\'s unlike C++ modules, which are statically compiled into
  the engine. Every time you change a module, you need to recompile the
  engine. Even with incremental builds, this process is slower than
  using GDExtension.

### Advantages of C++ modules

We recommend `C++ modules <doc_custom_modules_in_cpp>`{.interpreted-text
role="ref"} in cases where GDExtension isn\'t enough:

- C++ modules provide deeper integration into the engine. GDExtension\'s
  access is not as deep as static modules.
- You can use C++ modules to provide additional features in a project
  without carrying native library files around. This extends to exported
  projects.

> [!NOTE]
> If you notice that specific systems are not accessible via GDExtension
> but are via custom modules, feel free to open an issue on the
> [godot-cpp repository](https://github.com/godotengine/godot-cpp) to
> discuss implementation options for exposing the missing functionality.

## Supported languages

The Godot developers officially support the following language bindings
for GDExtension:

- C++ `(tutorial) <doc_gdextension_cpp_example>`{.interpreted-text
  role="ref"}

> [!NOTE]
> There are no plans to support additional languages with GDExtension
> officially. That said, the community offers several bindings for other
> languages (see below).

::: {#doc_what_is_gdnative_third_party_bindings}
The bindings below are developed and maintained by the community:
:::

- [D](https://github.com/godot-dlang/godot-dlang)
- [Go](https://github.com/grow-graphics/gd)
- [Haxe](https://hxgodot.github.io/)
- [Rust](https://github.com/godot-rust/gdext)
- [Swift](https://github.com/migueldeicaza/SwiftGodot)

> [!NOTE]
> Not all bindings mentioned here may be production-ready. Make sure to
> research options thoroughly before starting a project with one of
> those. Also, double-check whether the binding is compatible with the
> Godot version you\'re using.

## Version compatibility

GDExtension add-ons compiled for a given Godot version are only
guaranteed to work with the same minor release series. For example, a
GDExtension add-on compiled for Godot 4.0 will only work with Godot 4.0,
4.0.1, 4.0.2. In addition, GDExtension is not compatible with Godot 3.x.

GDExtension add-ons are also only compatible with engine builds that use
the level of floating-point precision the extension was compiled for.
This means that if you use an engine build with double-precision floats,
the extension must also be compiled for double-precision floats. See
`doc_large_world_coordinates`{.interpreted-text role="ref"} for details.
