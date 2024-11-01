# Exporting for the Web {#doc_exporting_for_web}

::: {.seealso}
This page describes how to export a Godot project to HTML5. If you\'re
looking to compile editor or export template binaries from source
instead, read `doc_compiling_for_web`{.interpreted-text role="ref"}.
:::

HTML5 export allows publishing games made in Godot Engine to the
browser. This requires support for
[WebAssembly](https://webassembly.org/),
[WebGL](https://www.khronos.org/webgl/) and
[SharedArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer)
in the user\'s browser.

:::: {.attention}
::: {.title}
Attention
:::

Projects written in C# using Godot 4 currently cannot be exported to the
web. To use C# on web platforms, use Godot 3 instead.
::::

> [!TIP]
> Use the browser-integrated developer console, usually opened with
> `F12`{.interpreted-text role="kbd"}
> (`Cmd + Option + I`{.interpreted-text role="kbd"} on macOS), to view
> **debug information** like JavaScript, engine, and WebGL errors.

:::: {.attention}
::: {.title}
Attention
:::

Godot 4\'s HTML5 exports currently cannot run on macOS and iOS due to
upstream bugs with SharedArrayBuffer and WebGL 2.0. We recommend using
`macOS <doc_exporting_for_macos>`{.interpreted-text role="ref"} and
`iOS <doc_exporting_for_ios>`{.interpreted-text role="ref"} native
export functionality instead, as it will also result in better
performance.

Godot 3\'s HTML5 exports are more compatible with various browsers in
general, especially when using the GLES2 rendering backend (which only
requires WebGL 1.0).
::::

## Export file name

We do suggest users to export their Web projects with `index.html` as
the file name. `index.html` is usually the default file loaded by web
servers when accessing the parent directory, usually hiding the name of
that file.

:::: {.attention}
::: {.title}
Attention
:::

The Godot 4 Web export expects some files to be named the same name as
the one set in the initial export. Some issues could occur if some
exported files are renamed, including the main HTML file.
::::

## WebGL version

Godot 4.0 and later can only target WebGL 2.0 (using the Compatibility
rendering method). There is no stable way to run Vulkan applications on
the web yet.

See [Can I use WebGL 2.0](https://caniuse.com/webgl2) for a list of
browser versions supporting WebGL 2.0. Note that Safari has several
issues with WebGL 2.0 support that other browsers don\'t have, so we
recommend using a Chromium-based browser or Firefox if possible.

## Export options {#doc_javascript_export_options}

If a runnable web export template is available, a button appears between
the *Stop scene* and *Play edited Scene* buttons in the editor to
quickly open the game in the default browser for testing.

If your project uses GDExtension **Extension Support** needs to be
enabled.

If you plan to use
`VRAM compression <doc_importing_images>`{.interpreted-text role="ref"}
make sure that **Vram Texture Compression** is enabled for the targeted
platforms (enabling both **For Desktop** and **For Mobile** will result
in a bigger, but more compatible export).

If a path to a **Custom HTML shell** file is given, it will be used
instead of the default HTML page. See
`doc_customizing_html5_shell`{.interpreted-text role="ref"}.

**Head Include** is appended into the `<head>` element of the generated
HTML page. This allows to, for example, load webfonts and third-party
JavaScript APIs, include CSS, or run JavaScript code.

> [!IMPORTANT]
> Each project must generate their own HTML file. On export, several
> text placeholders are replaced in the generated HTML file specifically
> for the given export options. Any direct modifications to that HTML
> file will be lost in future exports. To customize the generated file,
> use the **Custom HTML shell** option.

## Limitations

For security and privacy reasons, many features that work effortlessly
on native platforms are more complicated on the web platform. Following
is a list of limitations you should be aware of when porting a Godot
game to the web.

::::: {#doc_javascript_secure_contexts}
> [!IMPORTANT]
> Browser vendors are making more and more functionalities only
> available in [secure
> contexts](https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts),
> this means that such features are only be available if the web page is
> served via a secure HTTPS connection (localhost is usually exempt from
> such requirement).
:::::

### Using cookies for data persistence

Users must **allow cookies** (specifically IndexedDB) if persistence of
the `user://` file system is desired. When playing a game presented in
an `iframe`, **third-party** cookies must also be enabled.
Incognito/private browsing mode also prevents persistence.

The method `OS.is_userfs_persistent()` can be used to check if the
`user://` file system is persistent, but can give false positives in
some cases.

### Background processing

The project will be paused by the browser when the tab is no longer the
active tab in the user\'s browser. This means functions such as
`_process()` and `_physics_process()` will no longer run until the tab
is made active again by the user (by switching back to the tab). This
can cause networked games to disconnect if the user switches tabs for a
long duration.

This limitation does not apply to unfocused browser *windows*.
Therefore, on the user\'s side, this can be worked around by running the
project in a separate *window* instead of a separate tab.

### Full screen and mouse capture

Browsers do not allow arbitrarily **entering full screen**. The same
goes for **capturing the cursor**. Instead, these actions have to occur
as a response to a JavaScript input event. In Godot, this means entering
full screen from within a pressed input event callback such as `_input`
or `_unhandled_input`. Querying the `class_Input`{.interpreted-text
role="ref"} singleton is not sufficient, the relevant input event must
currently be active.

For the same reason, the full screen project setting doesn\'t work
unless the engine is started from within a valid input event handler.
This requires
`customization of the HTML page <doc_customizing_html5_shell>`{.interpreted-text
role="ref"}.

### Audio

Some browsers restrict autoplay for audio on websites. The easiest way
around this limitation is to request the player to click, tap or press a
key/button to enable audio, for instance when displaying a splash screen
at the start of your game.

::: {.seealso}
Google offers additional information about their [Web Audio autoplay
policies](https://sites.google.com/a/chromium.org/dev/audio-video/autoplay).

Apple\'s Safari team also posted additional information about their
[Auto-Play Policy Changes for
macOS](https://webkit.org/blog/7734/auto-play-policy-changes-for-macos/).
:::

> [!WARNING]
> Access to microphone requires a
> `secure context <doc_javascript_secure_contexts>`{.interpreted-text
> role="ref"}.

### Networking

Low level networking is not implemented due to lacking support in
browsers.

Currently, only `HTTP client <doc_http_client_class>`{.interpreted-text
role="ref"}, `HTTP requests <doc_http_request_class>`{.interpreted-text
role="ref"}, `WebSocket (client) <doc_websocket>`{.interpreted-text
role="ref"} and `WebRTC <doc_webrtc>`{.interpreted-text role="ref"} are
supported.

The HTTP classes also have several restrictions on the HTML5 platform:

> - Accessing or changing the `StreamPeer` is not possible
> - Threaded/Blocking mode is not available
> - Cannot progress more than once per frame, so polling in a loop will
>   freeze
> - No chunked responses
> - Host verification cannot be disabled
> - Subject to [same-origin
>   policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)

### Clipboard

Clipboard synchronization between engine and the operating system
requires a browser supporting the [Clipboard
API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API),
additionally, due to the API asynchronous nature might not be reliable
when accessed from GDScript.

> [!WARNING]
> Requires a
> `secure context <doc_javascript_secure_contexts>`{.interpreted-text
> role="ref"}.

### Gamepads

Gamepads will not be detected until one of their button is pressed.
Gamepads might have the wrong mapping depending on the
browser/OS/gamepad combination, sadly the [Gamepad
API](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API)
does not provide a reliable way to detect the gamepad information
necessary to remap them based on model/vendor/OS due to privacy
considerations.

> [!WARNING]
> Requires a
> `secure context <doc_javascript_secure_contexts>`{.interpreted-text
> role="ref"}.

### Boot splash is not displayed

The default HTML page does not display the boot splash while loading.
However, the image is exported as a PNG file, so
`custom HTML pages <doc_customizing_html5_shell>`{.interpreted-text
role="ref"} can display it.

## Serving the files {#doc_exporting_for_web_serving_the_files}

Exporting for the web generates several files to be served from a web
server, including a default HTML page for presentation. A custom HTML
file can be used, see `doc_customizing_html5_shell`{.interpreted-text
role="ref"}.

> [!WARNING]
> To ensure low audio latency and the ability to use
> `class_Thread`{.interpreted-text role="ref"} in web exports, Godot 4
> web exports always use
> [SharedArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer).
> This requires a
> `secure context <doc_javascript_secure_contexts>`{.interpreted-text
> role="ref"}, while also requiring the following CORS headers to be set
> when serving the files:
>
>     Cross-Origin-Opener-Policy: same-origin
>     Cross-Origin-Embedder-Policy: require-corp
>
> If you don\'t control the web server or are unable to add response
> headers, use
> [coi-serviceworker](https://github.com/gzuidhof/coi-serviceworker) as
> a workaround.
>
> If the client doesn\'t receive the required response headers, **the
> project will not run**.

The generated `.html` file can be used as `DirectoryIndex` in Apache
servers and can be renamed to e.g. `index.html` at any time. Its name is
never depended on by default.

The HTML page draws the game at maximum size within the browser window.
This way, it can be inserted into an `<iframe>` with the game\'s size,
as is common on most web game hosting sites.

The other exported files are served as they are, next to the `.html`
file, names unchanged. The `.wasm` file is a binary WebAssembly module
implementing the engine. The `.pck` file is the Godot main pack
containing your game. The `.js` file contains start-up code and is used
by the `.html` file to access the engine. The `.png` file contains the
boot splash image. It is not used in the default HTML page, but is
included for
`custom HTML pages <doc_customizing_html5_shell>`{.interpreted-text
role="ref"}.

The `.pck` file is binary, usually delivered with the MIME-type
`application/octet-stream`{.interpreted-text role="mimetype"}. The
`.wasm` file is delivered as `application/wasm`{.interpreted-text
role="mimetype"}.

> [!WARNING]
> Delivering the WebAssembly module (`.wasm`) with a MIME-type other
> than `application/wasm`{.interpreted-text role="mimetype"} can prevent
> some start-up optimizations.

Delivering the files with server-side compression is recommended
especially for the `.pck` and `.wasm` files, which are usually large in
size. The WebAssembly module compresses particularly well, down to
around a quarter of its original size with gzip compression. Consider
using Brotli precompression if supported on your web server for further
file size savings.

**Hosts that provide on-the-fly compression:** GitHub Pages (gzip)

**Hosts that don\'t provide on-the-fly compression:** itch.io, GitLab
Pages ([supports manual gzip
precompression](https://webd97.de/post/gitlab-pages-compression/))

> [!TIP]
> The Godot repository includes a [Python script to host a local web
> server](https://raw.githubusercontent.com/godotengine/godot/master/platform/web/serve.py).
> This script is intended for testing the web editor, but it can also be
> used to test exported projects.
>
> Save the linked script to a file called `serve.py`, move this file to
> the folder containing the exported project\'s `index.html`, then run
> the following command in a command prompt within the same folder:
>
>     # You may need to replace `python` with `python3` on some platforms.
>     python serve.py --root .
>
> On Windows, you can open a command prompt in the current folder by
> holding `Shift`{.interpreted-text role="kbd"} and right-clicking on
> empty space in Windows Explorer, then choosing **Open PowerShell
> window here**.
>
> This will serve the contents of the current folder and open the
> default web browser automatically.
>
> Note that for production use cases, this Python-based web server
> should not be used. Instead, you should use an established web server
> such as Apache or nginx.

## Interacting with the browser and JavaScript

See the `dedicated page <doc_web_javascript_bridge>`{.interpreted-text
role="ref"} on how to interact with JavaScript and access some unique
Web browser features.

## Environment variables

You can use the following environment variables to set export options
outside of the editor. During the export process, these override the
values that you set in the export menu.

| Export option               | Environment variable          |
|-----------------------------|-------------------------------|
| Encryption / Encryption Key | `GODOT_SCRIPT_ENCRYPTION_KEY` |

HTML5 export environment variables
