# Compiling with .NET {#doc_compiling_with_dotnet}

## Requirements

- [.NET SDK 8.0+](https://dotnet.microsoft.com/download)

  You can use `dotnet --info` to check which .NET SDK versions are
  installed.

## Enable the .NET module {#enable-the-.net-module}

> [!NOTE]
> C# support for Godot has historically used the
> [Mono](https://www.mono-project.com/) runtime instead of the [.NET
> Runtime](https://github.com/dotnet/runtime) and internally many things
> are still named `mono` instead of `dotnet` or otherwise referred to as
> `mono`.

By default, the .NET module is disabled when building. To enable it, add
the option `module_mono_enabled=yes` to the SCons command line, while
otherwise following the instructions for building the desired Godot
binaries.

## Generate the glue

Parts of the sources of the managed libraries are generated from the
ClassDB. These source files must be generated before building the
managed libraries. They can be generated by any .NET-enabled Godot
editor binary by running it with the parameters
`--headless --generate-mono-glue` followed by the path to an output
directory. This path must be `modules/mono/glue` in the Godot directory:

``` shell
<godot_binary> --headless --generate-mono-glue modules/mono/glue
```

This command will tell Godot to generate the C# bindings for the Godot
API at `modules/mono/glue/GodotSharp/GodotSharp/Generated`, and the C#
bindings for the editor tools at
`modules/mono/glue/GodotSharp/GodotSharpEditor/Generated`. Once these
files are generated, you can build Godot\'s managed libraries for all
the desired targets without having to repeat this process.

`<godot_binary>` refers to the editor binary you compiled with the .NET
module enabled. Its exact name will differ based on your system and
configuration, but should be of the form
`bin/godot.<platform>.editor.<arch>.mono`, e.g.
`bin/godot.linuxbsd.editor.x86_64.mono` or
`bin/godot.windows.editor.x86_32.mono.exe`. Be especially aware of the
**.mono** suffix! If you\'ve previously compiled Godot without .NET
support, you might have similarly named binaries without this suffix.
These binaries can\'t be used to generate the .NET glue.

> [!NOTE]
> The glue sources must be regenerated every time the ClassDB-registered
> API changes. That is, for example, when a new method is registered to
> the scripting API or one of the parameters of such a method changes.
> Godot will print an error at startup if there is an API mismatch
> between ClassDB and the glue sources.

## Building the managed libraries

Once you have generated the .NET glue, you can build the managed
libraries with the `build_assemblies.py` script:

``` shell
./modules/mono/build_scripts/build_assemblies.py --godot-output-dir=./bin
```

If everything went well, the `GodotSharp` directory, containing the
managed libraries, should have been created in the `bin` directory.

> [!NOTE]
> By default, all development builds share a version number, which can
> cause some issues with caching of the NuGet packages. To solve this
> issue either use `GODOT_VERSION_STATUS` to give every build a unique
> version or delete `GodotNuGetFallbackFolder` after every build to
> clear the package cache.

Unlike \"classical\" Godot builds, when building with the .NET module
enabled (and depending on the target platform), a data directory may be
created both for the editor and for exported projects. This directory is
important for proper functioning and must be distributed together with
Godot. More details about this directory in
`Data directory<compiling_with_dotnet_data_directory>`{.interpreted-text
role="ref"}.

### Build Platform

Provide the `--godot-platform=<platform>` argument to control for which
platform specific the libraries are built. Omit this argument to build
for the current system.

This currently only controls the inclusion of the support for Visual
Studio as an external editor, the libraries are otherwise identical.

### NuGet packages

The API assemblies, source generators, and custom MSBuild project SDK
are distributed as NuGet packages. This is all transparent to the user,
but it can make things complicated during development.

In order to use Godot with a development version of those packages, a
local NuGet source must be created where MSBuild can find them.

First, pick a location for the local NuGet source. If you don\'t have a
preference, create an empty directory at one of these recommended
locations:

- On Windows, `C:\Users\<username>\MyLocalNugetSource`
- On Linux, \*BSD, etc., `~/MyLocalNugetSource`

This path is referred to later as `<my_local_source>`.

After picking a directory, run this .NET CLI command to configure NuGet
to use your local source:

``` shell
dotnet nuget add source <my_local_source> --name MyLocalNugetSource
```

When you run the `build_assemblies.py` script, pass `<my_local_source>`
to the `--push-nupkgs-local` option:

``` shell
./modules/mono/build_scripts/build_assemblies.py --godot-output-dir ./bin --push-nupkgs-local <my_local_source>
```

This option ensures the packages will be added to the specified local
NuGet source and that conflicting versions of the package are removed
from the NuGet cache. It\'s recommended to always use this option when
building the C# solutions during development to avoid mistakes.

### Building without depending on deprecated features (NO_DEPRECATED)

When building Godot without deprecated classes and functions, i.e. the
`deprecated=no` argument for scons, the managed libraries must also be
built without dependencies to deprecated code. This is done by passing
the `--no-deprecated` argument:

::

:   ./modules/mono/build_scripts/build_assemblies.py \--godot-output-dir
    ./bin \--push-nupkgs-local \<my_local_source\> \--no-deprecated

### Double Precision Support (REAL_T_IS_DOUBLE)

When building Godot with double precision support, i.e. the
`precision=double` argument for scons, the managed libraries must be
adjusted to match by passing the `--precision=double` argument:

``` shell
./modules/mono/build_scripts/build_assemblies.py --godot-output-dir ./bin --push-nupkgs-local <my_local_source> --precision=double
```

## Examples

### Example (Windows)

``` shell
# Build editor binary
scons platform=windows target=editor module_mono_enabled=yes
# Build export templates
scons platform=windows target=template_debug module_mono_enabled=yes
scons platform=windows target=template_release module_mono_enabled=yes

# Generate glue sources
bin/godot.windows.editor.x86_64.mono --headless --generate-mono-glue modules/mono/glue
# Build .NET assemblies
./modules/mono/build_scripts/build_assemblies.py --godot-output-dir=./bin --godot-platform=windows
```

### Example (Linux, \*BSD)

``` shell
# Build editor binary
scons platform=linuxbsd target=editor module_mono_enabled=yes
# Build export templates
scons platform=linuxbsd target=template_debug module_mono_enabled=yes
scons platform=linuxbsd target=template_release module_mono_enabled=yes

# Generate glue sources
bin/godot.linuxbsd.editor.x86_64.mono --headless --generate-mono-glue modules/mono/glue
# Generate binaries
./modules/mono/build_scripts/build_assemblies.py --godot-output-dir=./bin --godot-platform=linuxbsd
```

## Data directory {#compiling_with_dotnet_data_directory}

The data directory is a dependency for Godot binaries built with the
.NET module enabled. It contains important files for the correct
functioning of Godot. It must be distributed together with the Godot
executable.

### Editor

The name of the data directory for the Godot editor will always be
`GodotSharp`. This directory contains an `Api` subdirectory with the
Godot API assemblies and a `Tools` subdirectory with the tools required
by the editor, like the `GodotTools` assemblies and its dependencies.

On macOS, if the Godot editor is distributed as a bundle, the
`GodotSharp` directory may be placed in the
`<bundle_name>.app/Contents/Resources/` directory inside the bundle.

### Export templates

The data directory for exported projects is generated by the editor
during the export. It is named `data_<APPNAME>_<ARCH>`, where
`<APPNAME>` is the application name as specified in the project setting
`application/config/name` and `<ARCH>` is the current architecture of
the export.

In the case of multi-architecture exports multiple such data directories
will be generated.

## Command-line options

The following is the list of command-line options available when
building with the .NET module:

- **module_mono_enabled**=yes \| **no**
  - Build Godot with the .NET module enabled.