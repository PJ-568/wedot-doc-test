allow_comments

:   False

# System requirements {#doc_system_requirements}

This page contains system requirements for the editor and exported
projects. These specifications are given for informative purposes only,
but they can be referred to if you\'re looking to build or upgrade a
system to use Godot on.

## Godot editor

These are the **minimum** specifications required to run the Godot
editor and work on a simple 2D or 3D project:

### Desktop or laptop PC - Minimum

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<tbody>
<tr>
<td><strong>CPU</strong></td>
<td><ul>
<li><strong>Windows:</strong> x86_32 CPU with SSE2 instructions, x86_64
CPU, ARMv8 CPU
<ul>
<li><em>Example: Intel Core 2 Duo E8200, AMD Athlon XE BE-2300,
Snapdragon X Elite</em></li>
</ul></li>
<li><strong>macOS:</strong> x86_64 or ARM CPU (Apple Silicon)
<ul>
<li><em>Example: Intel Core 2 Duo SU9400, Apple M1</em></li>
</ul></li>
<li><strong>Linux:</strong> x86_32 CPU with SSE2 instructions, x86_64
CPU, ARMv7 or ARMv8 CPU
<ul>
<li><em>Example: Intel Core 2 Duo E8200, AMD Athlon XE BE-2300,
Raspberry Pi 4</em></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td><strong>GPU</strong></td>
<td><ul>
<li><strong>Forward+ rendering method:</strong> Integrated graphics with
full Vulkan 1.0 support
<ul>
<li><em>Example: Intel HD Graphics 5500 (Broadwell), AMD Radeon R5
Graphics (Kaveri)</em></li>
</ul></li>
<li><strong>Mobile rendering method:</strong> Integrated graphics with
full Vulkan 1.0 support
<ul>
<li><em>Example: Intel HD Graphics 5500 (Broadwell), AMD Radeon R5
Graphics (Kaveri)</em></li>
</ul></li>
<li><strong>Compatibility rendering method:</strong> Integrated graphics
with full OpenGL 3.3 support
<ul>
<li><em>Example: Intel HD Graphics 2500 (Ivy Bridge), AMD Radeon R5
Graphics (Kaveri)</em></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td><strong>RAM</strong></td>
<td><ul>
<li><strong>Native editor:</strong> 4 GB</li>
<li><strong>Web editor:</strong> 8 GB</li>
</ul></td>
</tr>
<tr>
<td><strong>Storage</strong></td>
<td>200 MB (used for the executable, project files and cache). Exporting
projects requires downloading export templates separately (1.3 GB after
installation).</td>
</tr>
<tr>
<td><strong>Operating system</strong></td>
<td><ul>
<li><strong>Native editor:</strong> Windows 7, macOS 10.13
(Compatibility) or macOS 10.15 (Forward+/Mobile), Linux distribution
released after 2016</li>
<li><strong>Web editor:</strong> Firefox 79, Chrome 68, Edge 79, Safari
15.2, Opera 64</li>
</ul></td>
</tr>
</tbody>
</table>

> [!NOTE]
> Windows 7/8/8.1 are supported on a best-effort basis. These versions
> are not regularly tested and some features may be missing (such as
> colored
> `print_rich <class_@GlobalScope_method_print_rich>`{.interpreted-text
> role="ref"} console output). Support for Windows 7/8/8.1 may be
> removed in a
> `future Godot 4.x release <doc_release_policy>`{.interpreted-text
> role="ref"}.
>
> Vulkan drivers for these Windows versions are known to have issues
> with memory leaks. As a result, it\'s recommended to stick to the
> Compatibility rendering method when running Godot on a Windows version
> older than 10.

### Mobile device (smartphone/tablet) - Minimum

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<tbody>
<tr>
<td><strong>CPU</strong></td>
<td><ul>
<li><p><strong>Android:</strong> SoC with any 32-bit or 64-bit ARM or
x86 CPU</p>
<blockquote>
<ul>
<li><em>Example: Qualcomm Snapdragon 430, Samsung Exynos 5 Octa
5430</em></li>
</ul>
</blockquote></li>
<li><p><strong>iOS:</strong> <em>Cannot run the editor</em></p></li>
</ul></td>
</tr>
<tr>
<td><strong>GPU</strong></td>
<td><ul>
<li><strong>Forward+ rendering method:</strong> SoC featuring GPU with
full Vulkan 1.0 support
<ul>
<li><em>Example: Qualcomm Adreno 505, Mali-G71 MP2</em></li>
</ul></li>
<li><strong>Mobile rendering method:</strong> SoC featuring GPU with
full Vulkan 1.0 support
<ul>
<li><em>Example: Qualcomm Adreno 505, Mali-G71 MP2</em></li>
</ul></li>
<li><strong>Compatibility rendering method:</strong> SoC featuring GPU
with full OpenGL ES 3.0 support
<ul>
<li><em>Example: Qualcomm Adreno 306, Mali-T628 MP6</em></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td><strong>RAM</strong></td>
<td><ul>
<li><strong>Native editor:</strong> 3 GB</li>
<li><strong>Web editor:</strong> 6 GB</li>
</ul></td>
</tr>
<tr>
<td><strong>Storage</strong></td>
<td>200 MB (used for the executable, project files and cache). Exporting
projects requires downloading export templates separately (1.3 GB after
installation).</td>
</tr>
<tr>
<td><strong>Operating system</strong></td>
<td><ul>
<li><strong>Native editor:</strong> Android 6.0 (Compatibility) or
Android 9.0 (Forward+/Mobile)</li>
<li><strong>Web editor:</strong> Firefox 79, Chrome 88, Edge 79, Safari
15.2, Opera 64, Samsung Internet 15</li>
</ul></td>
</tr>
</tbody>
</table>

These are the **recommended** specifications to get a smooth experience
with the Godot editor on a simple 2D or 3D project:

### Desktop or laptop PC - Recommended

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr>
<td><strong>CPU</strong></td>
<td><ul>
<li><strong>Windows:</strong> x86_64 CPU with SSE4.2 instructions, with
4 physical cores or more, ARMv8 CPU
<ul>
<li><em>Example: Intel Core i5-6600K, AMD Ryzen 5 1600, Snapdragon X
Elite</em></li>
</ul></li>
<li><strong>macOS:</strong> x86_64 or ARM CPU (Apple Silicon)
<ul>
<li><em>Example: Intel Core i5-8500, Apple M1</em></li>
</ul></li>
<li><strong>Linux:</strong> x86_32 CPU with SSE2 instructions, x86_64
CPU, ARMv7 or ARMv8 CPU
<ul>
<li><em>Example: Intel Core i5-6600K, AMD Ryzen 5 1600, Raspberry Pi 5
with overclocking</em></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td><strong>GPU</strong></td>
<td><ul>
<li><strong>Forward+ rendering method:</strong> Dedicated graphics with
full Vulkan 1.2 support
<ul>
<li><em>Example: NVIDIA GeForce GTX 1050 (Pascal), AMD Radeon RX 460
(GCN 4.0)</em></li>
</ul></li>
<li><strong>Mobile rendering method:</strong> Dedicated graphics with
full Vulkan 1.2 support
<ul>
<li><em>Example: NVIDIA GeForce GTX 1050 (Pascal), AMD Radeon RX 460
(GCN 4.0)</em></li>
</ul></li>
<li><strong>Compatibility rendering method:</strong> Dedicated graphics
with full OpenGL 4.6 support
<ul>
<li><em>Example: NVIDIA GeForce GTX 650 (Kepler), AMD Radeon HD 7750
(GCN 1.0)</em></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td><strong>RAM</strong></td>
<td><ul>
<li><strong>Native editor:</strong> 8 GB</li>
<li><strong>Web editor:</strong> 12 GB</li>
</ul></td>
</tr>
<tr>
<td><strong>Storage</strong></td>
<td>1.5 GB (used for the executable, project files, all export templates
and cache)</td>
</tr>
<tr>
<td><strong>Operating system</strong></td>
<td><ul>
<li><strong>Native editor:</strong> Windows 10, macOS 10.15, Linux
distribution released after 2020</li>
<li><strong>Web editor:</strong> Latest version of Firefox, Chrome,
Edge, Safari, Opera</li>
</ul></td>
</tr>
</tbody>
</table>

### Mobile device (smartphone/tablet) - Recommended

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<tbody>
<tr>
<td><strong>CPU</strong></td>
<td><ul>
<li><strong>Android:</strong> SoC with 64-bit ARM or x86 CPU, with 3
"performance" cores or more
<ul>
<li><em>Example: Qualcomm Snapdragon 845, Samsung Exynos 9810</em></li>
</ul></li>
<li><strong>iOS:</strong> <em>Cannot run the editor</em></li>
</ul></td>
</tr>
<tr>
<td><strong>GPU</strong></td>
<td><ul>
<li><strong>Forward+ rendering method:</strong> SoC featuring GPU with
full Vulkan 1.2 support
<ul>
<li><em>Example: Qualcomm Adreno 630, Mali-G72 MP18</em></li>
</ul></li>
<li><strong>Mobile rendering method:</strong> SoC featuring GPU with
full Vulkan 1.2 support
<ul>
<li><em>Example: Qualcomm Adreno 630, Mali-G72 MP18</em></li>
</ul></li>
<li><strong>Compatibility rendering method:</strong> SoC featuring GPU
with full OpenGL ES 3.2 support
<ul>
<li><em>Example: Qualcomm Adreno 630, Mali-G72 MP18</em></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td><strong>RAM</strong></td>
<td><ul>
<li><strong>Native editor:</strong> 6 GB</li>
<li><strong>Web editor:</strong> 8 GB</li>
</ul></td>
</tr>
<tr>
<td><strong>Storage</strong></td>
<td>1.5 GB (used for the executable, project files, all export templates
and cache)</td>
</tr>
<tr>
<td><strong>Operating system</strong></td>
<td><ul>
<li><strong>Native editor:</strong> Android 9.0</li>
<li><strong>Web editor:</strong> Latest version of Firefox, Chrome,
Edge, Safari, Opera, Samsung Internet</li>
</ul></td>
</tr>
</tbody>
</table>

## Exported Godot project

> [!WARNING]
> The requirements below are a baseline for a **simple** 2D or 3D
> project, with basic scripting and few visual flourishes. CPU, GPU, RAM
> and storage requirements will heavily vary depending on your
> project\'s scope, its rendering method, viewport resolution and
> graphics settings chosen. Other programs running on the system while
> the project is running will also compete for resources, including RAM
> and video RAM.
>
> It is strongly recommended to do your own testing on low-end hardware
> to make sure your project runs at the desired speed. To provide
> scalability for low-end hardware, you will also need to introduce a
> [graphics options
> menu](https://github.com/godotengine/godot-demo-projects/tree/master/3d/graphics_settings)
> to your project.

These are the **minimum** specifications required to run a simple 2D or
3D project exported with Godot:

### Desktop or laptop PC - Minimum

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<tbody>
<tr>
<td><strong>CPU</strong></td>
<td><ul>
<li><strong>Windows:</strong> x86_32 CPU with SSE2 instructions, any
x86_64 CPU, ARMv8 CPU</li>
</ul>
<blockquote>
<ul>
<li><em>Example: Intel Core 2 Duo E8200, AMD Athlon XE BE-2300,
Snapdragon X Elite</em></li>
</ul>
</blockquote>
<ul>
<li><strong>macOS:</strong> x86_64 or ARM CPU (Apple Silicon)</li>
</ul>
<blockquote>
<ul>
<li><em>Example: Intel Core 2 Duo SU9400, Apple M1</em></li>
</ul>
</blockquote>
<ul>
<li><strong>Linux:</strong> x86_32 CPU with SSE2 instructions, x86_64
CPU, ARMv7 or ARMv8 CPU</li>
</ul>
<blockquote>
<ul>
<li><em>Example: Intel Core 2 Duo E8200, AMD Athlon XE BE-2300,
Raspberry Pi 4</em></li>
</ul>
</blockquote></td>
</tr>
<tr>
<td><strong>GPU</strong></td>
<td><ul>
<li><strong>Forward+ rendering method:</strong> Integrated graphics with
full Vulkan 1.0 support
<ul>
<li><em>Example: Intel HD Graphics 5500 (Broadwell), AMD Radeon R5
Graphics (Kaveri)</em></li>
</ul></li>
<li><strong>Mobile rendering method:</strong> Integrated graphics with
full Vulkan 1.0 support
<ul>
<li><em>Example: Intel HD Graphics 5500 (Broadwell), AMD Radeon R5
Graphics (Kaveri)</em></li>
</ul></li>
<li><strong>Compatibility rendering method:</strong> Integrated graphics
with full OpenGL 3.3 support
<ul>
<li><em>Example: Intel HD Graphics 2500 (Ivy Bridge), AMD Radeon R5
Graphics (Kaveri)</em></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td><strong>RAM</strong></td>
<td><ul>
<li><strong>For native exports:</strong> 2 GB</li>
<li><strong>For web exports:</strong> 4 GB</li>
</ul></td>
</tr>
<tr>
<td><strong>Storage</strong></td>
<td>150 MB (used for the executable, project files and cache)</td>
</tr>
<tr>
<td><strong>Operating system</strong></td>
<td><ul>
<li><strong>For native exports:</strong> Windows 7, macOS 10.13
(Compatibility) or macOS 10.15 (Forward+/Mobile), Linux distribution
released after 2016</li>
<li><strong>For web exports:</strong> Firefox 79, Chrome 68, Edge 79,
Safari 15.2, Opera 64</li>
</ul></td>
</tr>
</tbody>
</table>

> [!NOTE]
> Windows 7/8/8.1 are supported on a best-effort basis. These versions
> are not regularly tested and some features may be missing (such as
> colored
> `print_rich <class_@GlobalScope_method_print_rich>`{.interpreted-text
> role="ref"} console output). Support for Windows 7/8/8.1 may be
> removed in a
> `future Godot 4.x release <doc_release_policy>`{.interpreted-text
> role="ref"}.
>
> Vulkan drivers for these Windows versions are known to have issues
> with memory leaks. As a result, it\'s recommended to stick to the
> Compatibility rendering method when running Godot on a Windows version
> older than 10.

### Mobile device (smartphone/tablet) - Minimum

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<tbody>
<tr>
<td><strong>CPU</strong></td>
<td><ul>
<li><strong>Android:</strong> SoC with any 32-bit or 64-bit ARM or x86
CPU
<ul>
<li><em>Example: Qualcomm Snapdragon 430, Samsung Exynos 5 Octa
5430</em></li>
</ul></li>
<li><strong>iOS:</strong> SoC with any 64-bit ARM CPU
<ul>
<li><em>Example: Apple A7 (iPhone 5S)</em></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td><strong>GPU</strong></td>
<td><ul>
<li><strong>Forward+ rendering method:</strong> SoC featuring GPU with
full Vulkan 1.0 support
<ul>
<li><em>Example: Qualcomm Adreno 505, Mali-G71 MP2, Apple A12 (iPhone
XR/XS)</em></li>
</ul></li>
<li><strong>Mobile rendering method:</strong> SoC featuring GPU with
full Vulkan 1.0 support
<ul>
<li><em>Example: Qualcomm Adreno 505, Mali-G71 MP2, Apple A12 (iPhone
XR/XS)</em></li>
</ul></li>
<li><strong>Compatibility rendering method:</strong> SoC featuring GPU
with full OpenGL ES 3.0 support
<ul>
<li><em>Example: Qualcomm Adreno 306, Mali-T628 MP6, Apple A7 (iPhone
5S)</em></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td><strong>RAM</strong></td>
<td><ul>
<li><strong>For native exports:</strong> 1 GB</li>
<li><strong>For web exports:</strong> 2 GB</li>
</ul></td>
</tr>
<tr>
<td><strong>Storage</strong></td>
<td>150 MB (used for the executable, project files and cache)</td>
</tr>
<tr>
<td><strong>Operating system</strong></td>
<td><ul>
<li><strong>For native exports:</strong> Android 6.0 (Compatibility) or
Android 9.0 (Forward+/Mobile), iOS 12.0</li>
<li><strong>For web exports:</strong> Firefox 79, Chrome 88, Edge 79,
Safari 15.2, Opera 64, Samsung Internet 15</li>
</ul></td>
</tr>
</tbody>
</table>

These are the **recommended** specifications to get a smooth experience
with a simple 2D or 3D project exported with Godot:

### Desktop or laptop PC - Recommended

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<tbody>
<tr>
<td><strong>CPU</strong></td>
<td><ul>
<li><strong>Windows:</strong> x86_64 CPU with SSE4.2 instructions, with
4 physical cores or more, ARMv8 CPU</li>
</ul>
<blockquote>
<ul>
<li><em>Example: Intel Core i5-6600K, AMD Ryzen 5 1600, Snapdragon X
Elite</em></li>
</ul>
</blockquote>
<ul>
<li><strong>macOS:</strong> x86_64 or ARM CPU (Apple Silicon)</li>
</ul>
<blockquote>
<ul>
<li><em>Example: Intel Core i5-8500, Apple M1</em></li>
</ul>
</blockquote>
<ul>
<li><strong>Linux:</strong> x86_32 CPU with SSE2 instructions, x86_64
CPU, ARMv7 or ARMv8 CPU</li>
</ul>
<blockquote>
<ul>
<li><em>Example: Intel Core i5-6600K, AMD Ryzen 5 1600, Raspberry Pi 5
with overclocking</em></li>
</ul>
</blockquote></td>
</tr>
<tr>
<td><strong>GPU</strong></td>
<td><ul>
<li><strong>Forward+ rendering method:</strong> Dedicated graphics with
full Vulkan 1.2 support
<ul>
<li><em>Example: NVIDIA GeForce GTX 1050 (Pascal), AMD Radeon RX 460
(GCN 4.0)</em></li>
</ul></li>
<li><strong>Mobile rendering method:</strong> Dedicated graphics with
full Vulkan 1.2 support
<ul>
<li><em>Example: NVIDIA GeForce GTX 1050 (Pascal), AMD Radeon RX 460
(GCN 4.0)</em></li>
</ul></li>
<li><strong>Compatibility rendering method:</strong> Dedicated graphics
with full OpenGL 4.6 support
<ul>
<li><em>Example: NVIDIA GeForce GTX 650 (Kepler), AMD Radeon HD 7750
(GCN 1.0)</em></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td><strong>RAM</strong></td>
<td><ul>
<li><strong>For native exports:</strong> 4 GB</li>
<li><strong>For web exports:</strong> 8 GB</li>
</ul></td>
</tr>
<tr>
<td><strong>Storage</strong></td>
<td>150 MB (used for the executable, project files and cache)</td>
</tr>
<tr>
<td><strong>Operating system</strong></td>
<td><ul>
<li><strong>For native exports:</strong> Windows 10, macOS 10.15, Linux
distribution released after 2020</li>
<li><strong>For web exports:</strong> Latest version of Firefox, Chrome,
Edge, Safari, Opera</li>
</ul></td>
</tr>
</tbody>
</table>

### Mobile device (smartphone/tablet) - Recommended

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<tbody>
<tr>
<td><strong>CPU</strong></td>
<td><ul>
<li><strong>Android:</strong> SoC with 64-bit ARM or x86 CPU, with 3
"performance" cores or more
<ul>
<li><em>Example: Qualcomm Snapdragon 845, Samsung Exynos 9810</em></li>
</ul></li>
<li><strong>iOS:</strong> SoC with 64-bit ARM CPU
<ul>
<li><em>Example: Apple A14 (iPhone 12)</em></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td><strong>GPU</strong></td>
<td><ul>
<li><strong>Forward+ rendering method:</strong> SoC featuring GPU with
full Vulkan 1.2 support
<ul>
<li><em>Example: Qualcomm Adreno 630, Mali-G72 MP18, Apple A14 (iPhone
12)</em></li>
</ul></li>
<li><strong>Mobile rendering method:</strong> SoC featuring GPU with
full Vulkan 1.2 support
<ul>
<li><em>Example: Qualcomm Adreno 630, Mali-G72 MP18, Apple A14 (iPhone
12)</em></li>
</ul></li>
<li><strong>Compatibility rendering method:</strong> SoC featuring GPU
with full OpenGL ES 3.2 support
<ul>
<li><em>Example: Qualcomm Adreno 630, Mali-G72 MP18, Apple A14 (iPhone
12)</em></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td><strong>RAM</strong></td>
<td><ul>
<li><strong>For native exports:</strong> 2 GB</li>
<li><strong>For web exports:</strong> 4 GB</li>
</ul></td>
</tr>
<tr>
<td><strong>Storage</strong></td>
<td>150 MB (used for the executable, project files and cache)</td>
</tr>
<tr>
<td><strong>Operating system</strong></td>
<td><ul>
<li><strong>For native exports:</strong> Android 9.0 or iOS 14.1</li>
<li><strong>For web exports:</strong> Latest version of Firefox, Chrome,
Edge, Safari, Opera, Samsung Internet</li>
</ul></td>
</tr>
</tbody>
</table>

> [!NOTE]
> Godot doesn\'t use OpenGL/OpenGL ES extensions introduced after OpenGL
> 3.3/OpenGL ES 3.0, but GPUs supporting newer OpenGL/OpenGL ES versions
> generally have fewer driver issues.
