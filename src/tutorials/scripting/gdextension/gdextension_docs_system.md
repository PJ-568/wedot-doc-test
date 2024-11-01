# GDExtension documentation system {#doc_gdextension_docs_system}

> [!NOTE]
> Adding documentation for GDExtensions is only possible for Godot 4.3
> and later. The support can be integrated into your project regardless
> because the snippet will check if you use the appropriate godot-cpp
> version. If you set the `compatability_minimum` to 4.2 and you load a
> project with the extension through a 4.2 editor, the documentation
> page for that class will be empty. The extension itself will still
> work.

The GDExtension documentation system works in a similar manner to the
built-in engine documentation. It uses a series of XML files (one per
class) to document the exposed constructors, properties, methods,
constants, signals, and theme items of each class.

> [!NOTE]
> We are assuming you are using the project files explained in the
> `GDExtension C++ Example <doc_gdextension_cpp_example>`{.interpreted-text
> role="ref"} with the following structure:

``` none
gdextension_cpp_example/  # GDExtension directory
|
+--demo/                  # game example/demo to test the extension
|   |
|   +--main.tscn
|   |
|   +--bin/
|       |
|       +--gdexample.gdextension
|
+--godot-cpp/             # C++ bindings
|
+--src/                   # source code of the extension we are building
|   |
|   +--register_types.cpp
|   +--register_types.h
|   +--gdexample.cpp
|   +--gdexample.h
```

Inside the Godot demo project directory of your GDExtension directory,
run the following terminal command:

``` none
# Replace "godot" with the full path to a Godot editor binary
# if Godot is not installed in your `PATH`.
godot --doctool ../ --gdextension-docs
```

This command calls upon the Godot editor binary to generate
documentation via the `--doctool` and `--gdextension-docs` commands. The
`../` addition is to let Godot know where the GDExtension SConstruct
file is located. By calling this command, Godot generates a
`doc_classes` directory inside the project directory in which it
generates XML files for the GDExtension classes. Those files can then be
edited to add information about member variables, methods, signals, and
more.

To add the now edited documentation to the GDExtension and let the
editor load it, you need to add the following lines to your SConstruct
file:

``` py
if env["target"] in ["editor", "template_debug"]:
try:
    doc_data = env.GodotCPPDocData("src/gen/doc_data.gen.cpp", source=Glob("doc_classes/*.xml"))
    sources.append(doc_data)
except AttributeError:
    print("Not including class reference as we're targeting a pre-4.3 baseline.")
```

The if-statement checks if we are compiling the GDExtension library with
the `editor` and `template_debug` flags. SCons then tries to load all
the XML files inside the `doc_classes` directory and appends them to the
`sources` variable which already includes all the source files of your
extension. If it fails it means we are currently trying to compile the
library when the `godot_cpp` is set to a version before 4.3.

After loading the extension in a 4.3 Godot editor or later and open the
documentation of your extension class either by
`Ctrl + Click`{.interpreted-text role="kbd"} in the script editor or the
Editor help dialog you will see something like this:

![image](img/gdextension_docs_generation.webp)

## Documentation styling

To style specific parts of text you can use BBCode tags similarly to how
they can be used in
`RichTextLabels <doc_bbcode_in_richtextlabel>`{.interpreted-text
role="ref"}. You can set text as bold, italic, underlined, colored,
codeblocks etc. by embedding them in tags like this:

``` none
[b]this text will be shown as bold[/b]
```

Currently they supported tags for the GDExtension documentation system
are:

<table>
<colgroup>
<col style="width: 60%" />
<col style="width: 40%" />
</colgroup>
<tbody>
<tr>
<td>Tag</td>
<td>Example</td>
</tr>
<tr>
<td><div class="line-block"><strong>b</strong><br />
Makes <code>{text}</code> use the bold (or bold italics) font of
<code>RichTextLabel</code>.</div></td>
<td><code>[b]{text}[/b]</code></td>
</tr>
<tr>
<td><div class="line-block"><strong>i</strong><br />
Makes <code>{text}</code> use the italics (or bold italics) font of
<code>RichTextLabel</code>.</div></td>
<td><code>[i]{text}[/i]</code></td>
</tr>
<tr>
<td><div class="line-block"><strong>u</strong><br />
Makes <code>{text}</code> underlined.</div></td>
<td><code>[u]{text}[/u]</code></td>
</tr>
<tr>
<td><div class="line-block"><strong>s</strong><br />
Makes <code>{text}</code> strikethrough.</div></td>
<td><code>[s]{text}[/s]</code></td>
</tr>
<tr>
<td><div class="line-block"><strong>kbd</strong><br />
Makes <code>{text}</code> use a grey beveled background, indicating a
keyboard shortcut.</div></td>
<td><code>[kbd]{text}[/kbd]</code></td>
</tr>
<tr>
<td><div class="line-block"><strong>code</strong><br />
Makes inline <code>{text}</code> use the mono font and styles the text
color and background like code.</div></td>
<td><code>[code]{text}[/code]</code></td>
</tr>
<tr>
<td><div class="line-block"><strong>codeblocks</strong><br />
Makes multiline <code>{text}</code> use the mono font and styles the
text color and background like code.<br />
The addition of the <code>[gdscript]</code> tag highlights the GDScript
specific syntax.</div></td>
<td><div class="line-block"><code>[codeblocks]</code><br />
<code>[gdscript]</code><br />
<code>{text}</code><br />
<code>[/gdscript]</code><br />
<code>[/codeblocks]</code></div></td>
</tr>
<tr>
<td><div class="line-block"><strong>center</strong><br />
Makes <code>{text}</code> horizontally centered.<br />
Same as <code>[p align=center]</code>.</div></td>
<td><code>[center]{text}[/center]</code></td>
</tr>
<tr>
<td><div class="line-block"><strong>url</strong><br />
Creates a hyperlink (underlined and clickable text). Can contain
optional <code>{text}</code> or display <code>{link}</code> as
is.</div></td>
<td><div class="line-block"><code>[url]{link}[/url]</code><br />
<code>[url={link}]{text}[/url]</code></div></td>
</tr>
<tr>
<td><div class="line-block"><strong>img</strong><br />
Inserts an image from the <code>{path}</code> (can be any valid <code
class="interpreted-text" role="ref">class_Texture2D</code>
resource).<br />
If <code>{width}</code> is provided, the image will try to fit that
width maintaining the aspect ratio.<br />
If both <code>{width}</code> and <code>{height}</code> are provided, the
image will be scaled to that size.<br />
Add <code>%</code> to the end of <code>{width}</code> or
<code>{height}</code> value to specify it as percentages of the control
width instead of pixels.<br />
If <code>{valign}</code> configuration is provided, the image will try
to align to the surrounding text, see <code class="interpreted-text"
role="ref">doc_bbcode_in_richtextlabel_image_and_table_alignment</code>.<br />
Supports configuration options, see <code class="interpreted-text"
role="ref">doc_bbcode_in_richtextlabel_image_options</code>.</div></td>
<td><div class="line-block"><code>[img]{path}[/img]</code><br />
<code>[img={width}]{path}[/img]</code><br />
<code>[img={width}x{height}]{path}[/img]</code><br />
<code>[img={valign}]{path}[/img]</code><br />
<code>[img {options}]{path}[/img]</code></div></td>
</tr>
<tr>
<td><div class="line-block"><strong>color</strong><br />
Changes the color of <code>{text}</code>. Color must be provided by a
common name (see <code class="interpreted-text"
role="ref">doc_bbcode_in_richtextlabel_named_colors</code>) or using the
HEX format (e.g. <code>#ff00ff</code>, see <code
class="interpreted-text"
role="ref">doc_bbcode_in_richtextlabel_hex_colors</code>).</div></td>
<td><code>[color={code/name}]{text}[/color]</code></td>
</tr>
</tbody>
</table>

## Publishing documentation online

You may want to publish an online reference for your GDExtension,
similar to this website. The most important step is to build
reStructuredText (`.rst`) files from your XML class reference:

``` bash
# You need a version.py file, so download it first.
curl -sSLO https://raw.githubusercontent.com/godotengine/godot/refs/heads/master/version.py

# Edit version.py according to your project before proceeding.
# Then, run the rst generator. You'll need to have Python installed for this command to work.
curl -sSL https://raw.githubusercontent.com/godotengine/godot/master/doc/tools/make_rst.py | python3 - -o "docs/classes" -l "en" doc_classes
```

Your `.rst` files will now be available in `docs/classes/`. From here,
you can use any documentation builder that supports reStructuredText
syntax to create a website from them.

[godot-docs](https://github.com/godotengine/godot-docs) uses
[Sphinx](https://www.sphinx-doc.org/en/master/). You can use the
repository as a basis to build your own documentation system. The
following guide describes the basic steps, but they are not exhaustive:
You will need a bit of personal insight to make it work.

1.  Add [godot-docs](https://github.com/godotengine/godot-docs) as a
    submodule to your `docs/` folder.
2.  Copy over its `conf.py`, `index.rst`, `.readthedocs.yaml` files into
    `/docs/`. You may later decide to copy over and edit more of
    godot-docs\' files, like `_templates/layout.html`.
3.  Modify these files according to your project. This mostly involves
    adjusting paths to point to the `godot-docs` subfolder, as well as
    strings to reflect it\'s your project rather than Godot you\'re
    building the docs for.
4.  Create an account on [readthedocs.org](http://readthedocs.org).
    Import your project, and modify its base `.readthedocs.yaml` file
    path to `/docs/.readthedocs.yaml`.

Once you have completed all these steps, your documentation should be
available at `<repo-name>.readthedocs.io`.
