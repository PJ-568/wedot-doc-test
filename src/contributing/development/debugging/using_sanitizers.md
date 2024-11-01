# Using sanitizers {#doc_using_sanitizers}

## What are sanitizers?

Sanitizers are static instrumentation tools that help find bugs that
traditional debuggers usually cannot catch. This is particularly useful
when combined with `doc_unit_testing`{.interpreted-text role="ref"} in
continuous integration.

Sanitizers can be used on Windows, macOS and Linux by using the Clang
(LLVM), GCC or Visual Studio compilers.
`Certain platforms <doc_using_sanitizers_platform_specific_sanitizers>`{.interpreted-text
role="ref"} may also have their own sanitizers available. In situations
where a single sanitizer is provided by several different compilers,
remember that their output and behavior will differ slightly.

## Using sanitizers on Godot

Sanitizers **require** recompiling the binary. This means you cannot use
official Godot binaries to run sanitizers.

When `compiling <toc-devel-compiling>`{.interpreted-text role="ref"}
with any of the sanitizers enabled, the resulting binary will have the
`.san` suffix added to its name to distinguish it from a binary without
sanitizers.

There is a performance impact as many additional runtime checks need to
be performed. Memory utilization will also increase. It is possible to
enable certain combinations of multiple sanitizers in a single build.
Beware of the performance impact when using multiple sanitizers at once
though, as the resulting binary may be excessively slow.

Certain options can be passed to sanitizers without having to recompile
the binary using environment variables.

## Address sanitizer (ASAN) {#doc_using_sanitizers_address_sanitizer}

- Available in Clang and GCC.
- **Supported platforms:** Linux, macOS, Windows (Visual Studio), Web
- [Clang ASAN
  documentation](https://clang.llvm.org/docs/AddressSanitizer.html)

The address sanitizer is generally the most frequently used sanitizer.
It can diagnose issues such as buffer overruns and out-of-bounds access.
If the engine crashes with a message such as `free(): invalid pointer`,
this is typically the result of a buffer overrun. (This message is
printed by the C runtime, not Godot.)

In certain situations (such as detecting uninitialized memory reads),
the address sanitizer doesn\'t suffice. The
`doc_using_sanitizers_memory_sanitizer`{.interpreted-text role="ref"}
should be used instead.

It is also possible to detect use-after-return situations by specifying
the `ASAN_OPTIONS=detect_stack_use_after_return=1` environment variable
before *running* Godot (not when compiling it). This increases the
address sanitizer\'s runtime overhead, so only enable this feature when
you actually need it.

To enable the address sanitizer in a Godot build, pass the
`use_asan=yes` SCons option when compiling. Enabling ASAN generally
makes the resulting binary about 2× slower.

> [!WARNING]
> Due to a [design
> decision](https://stackoverflow.com/questions/36971902/why-cant-clang-enable-all-sanitizers/),
> the address, memory and thread sanitizers are mutually exclusive. This
> means you can only use one of those sanitizers in a given binary.

## Leak sanitizer (LSAN)

- Available in Clang and GCC.
- **Supported platforms:** Linux, Web
- [Clang LSAN
  documentation](https://clang.llvm.org/docs/LeakSanitizer.html)

The leak sanitizer can detect memory leaks, which are situations where
memory that is no longer in use is never freed by the running program.
This can potentially lead to out-of-memory situations if the program
runs for long enough. Since Godot may run on
`dedicated servers <doc_exporting_for_dedicated_servers>`{.interpreted-text
role="ref"} for months or even years without a restart, it\'s important
to fix memory leaks when they occur.

To enable the leak sanitizer in a Godot build, pass the `use_lsan=yes`
SCons option when compiling. Enabling LSAN only has a small performance
overhead, but the program will be much slower to exit as leak detection
occurs when the program exits.

## Memory sanitizer (MSAN) {#doc_using_sanitizers_memory_sanitizer}

- Available in Clang only, not GCC.
- **Supported platforms:** Linux
- [Clang MSAN
  documentation](https://clang.llvm.org/docs/MemorySanitizer.html)

The memory sanitizer complements the
`doc_using_sanitizers_address_sanitizer`{.interpreted-text role="ref"}.
Unlike the address sanitizer, the memory sanitizer can detect
uninitialized memory reads.

To enable the memory sanitizer in a Godot build, pass the `use_msan=yes`
SCons option when compiling. Enabling MSAN generally makes the resulting
binary about 3× slower.

> [!WARNING]
> Due to a [design
> decision](https://stackoverflow.com/questions/36971902/why-cant-clang-enable-all-sanitizers/),
> the address, memory and thread sanitizers are mutually exclusive. This
> means you can only use one of those sanitizers in a given binary.

## Thread sanitizer (TSAN)

- Available in Clang and GCC.
- **Supported platforms:** Linux, macOS
- [Clang TSAN
  documentation](https://clang.llvm.org/docs/ThreadSanitizer.html)

The thread sanitizer is used to track down race conditions related to
multithreading. A race condition is when multiple threads try to modify
the same data at the same time. Since thread scheduling can be ordered
in any fashion by the operating system, this leads to incorrect behavior
that only occurs occasionally (and can be difficult to track as a
result). To prevent a race condition, you need to add a lock to ensure
only one thread can access the shared data at a given time.

To enable the thread sanitizer in a Godot build, pass the `use_tsan=yes`
SCons option when compiling. Enabling TSAN generally makes the resulting
binary 10× slower, while also multiplying memory usage by an
approximately 8× factor.

> [!WARNING]
> Due to a [design
> decision](https://stackoverflow.com/questions/36971902/why-cant-clang-enable-all-sanitizers/),
> the address, memory and thread sanitizers are mutually exclusive. This
> means you can only use one of those sanitizers in a given binary.

## Undefined behavior sanitizer (UBSAN)

- Available in Clang and GCC.
- **Supported platforms:** Linux, macOS, Web
- [Clang UBSAN
  documentation](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html)

The undefined behavior sanitizer is used to track down situations where
the program exhibits random and unpredictable behavior. This is due to
C/C++ code that is accepted by the compiler, but is not *correct*.
Compiling with a different set of optimizations can also change the
observed results of undefined behavior.

To enable the undefined behavior sanitizer in a Godot build, pass the
`use_ubsan=yes` SCons option when compiling. Enabling UBSAN only has a
small performance overhead.

## Platform-specific sanitizers {#doc_using_sanitizers_platform_specific_sanitizers}

### Web

When `compiling for the Web <doc_compiling_for_web>`{.interpreted-text
role="ref"}, there are 2 additional sanitizer SCons options available:

- `use_assertions=yes` enables runtime Emscripten assertions, which can
  catch various issues.
- `use_safe_heap=yes` enables [Emscripten\'s SAFE_HEAP
  sanitizer](https://emscripten.org/docs/debugging/Sanitizers.html). It
  provides similar functionality to ASAN, but it focuses on issues that
  are specific to WebAssembly. `SAFE_HEAP` is not guaranteed to be
  compatible with ASAN and UBSAN in the same binary, so you may have to
  build it separately.
