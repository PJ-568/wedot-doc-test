github_url

:   hide

# MovieWriter {#class_MovieWriter}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Abstract class for non-real-time video recording encoders.

::: {.rst-class}
classref-introduction-group
:::

## Description

Godot can record videos with non-real-time simulation. Like the
`--fixed-fps`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}, this forces the reported `delta` in
`Node._process<class_Node_private_method__process>`{.interpreted-text
role="ref"} functions to be identical across frames, regardless of how
long it actually took to render the frame. This can be used to record
high-quality videos with perfect frame pacing regardless of your
hardware\'s capabilities.

Godot has 2 built-in **MovieWriter**s:

- AVI container with MJPEG for video and uncompressed audio (`.avi` file
  extension). Lossy compression, medium file sizes, fast encoding. The
  lossy compression quality can be adjusted by changing
  `ProjectSettings.editor/movie_writer/mjpeg_quality<class_ProjectSettings_property_editor/movie_writer/mjpeg_quality>`{.interpreted-text
  role="ref"}. The resulting file can be viewed in most video players,
  but it must be converted to another format for viewing on the web or
  by Godot with
  `VideoStreamPlayer<class_VideoStreamPlayer>`{.interpreted-text
  role="ref"}. MJPEG does not support transparency. AVI output is
  currently limited to a file of 4 GB in size at most.
- PNG image sequence for video and WAV for audio (`.png` file
  extension). Lossless compression, large file sizes, slow encoding.
  Designed to be encoded to a video file with another tool such as
  [FFmpeg](https://ffmpeg.org/) after recording. Transparency is
  currently not supported, even if the root viewport is set to be
  transparent.

If you need to encode to a different format or pipe a stream through
third-party software, you can extend the **MovieWriter** class to create
your own movie writers. This should typically be done using GDExtension
for performance reasons.

\*\*Editor usage:\*\* A default movie file path can be specified in
`ProjectSettings.editor/movie_writer/movie_file<class_ProjectSettings_property_editor/movie_writer/movie_file>`{.interpreted-text
role="ref"}. Alternatively, for running single scenes, a `movie_file`
metadata can be added to the root node, specifying the path to a movie
file that will be used when recording that scene. Once a path is set,
click the video reel icon in the top-right corner of the editor to
enable Movie Maker mode, then run any scene as usual. The engine will
start recording as soon as the splash screen is finished, and it will
only stop recording when the engine quits. Click the video reel icon
again to disable Movie Maker mode. Note that toggling Movie Maker mode
does not affect project instances that are already running.

\*\*Note:\*\* MovieWriter is available for use in both the editor and
exported projects, but it is *not* designed for use by end users to
record videos while playing. Players wishing to record gameplay videos
should install tools such as [OBS Studio](https://obsproject.com/) or
[SimpleScreenRecorder](https://www.maartenbaert.be/simplescreenrecorder/)
instead.

::: {.rst-class}
classref-reftable-group
:::

## Methods

||
||
||
||
||
||
||
||
||

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_MovieWriter_private_method__get_audio_mix_rate}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_audio_mix_rate**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MovieWriter_private_method__get_audio_mix_rate>`{.interpreted-text
role="ref"}

Called when the audio sample rate used for recording the audio is
requested by the engine. The value returned must be specified in Hz.
Defaults to 48000 Hz if
`_get_audio_mix_rate<class_MovieWriter_private_method__get_audio_mix_rate>`{.interpreted-text
role="ref"} is not overridden.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MovieWriter_private_method__get_audio_speaker_mode}
::: {.rst-class}
classref-method
:::
::::

`SpeakerMode<enum_AudioServer_SpeakerMode>`{.interpreted-text
role="ref"} **\_get_audio_speaker_mode**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MovieWriter_private_method__get_audio_speaker_mode>`{.interpreted-text
role="ref"}

Called when the audio speaker mode used for recording the audio is
requested by the engine. This can affect the number of output channels
in the resulting audio file/stream. Defaults to
`AudioServer.SPEAKER_MODE_STEREO<class_AudioServer_constant_SPEAKER_MODE_STEREO>`{.interpreted-text
role="ref"} if
`_get_audio_speaker_mode<class_MovieWriter_private_method__get_audio_speaker_mode>`{.interpreted-text
role="ref"} is not overridden.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MovieWriter_private_method__handles_file}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_handles_file**(path: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MovieWriter_private_method__handles_file>`{.interpreted-text
role="ref"}

Called when the engine determines whether this **MovieWriter** is able
to handle the file at `path`. Must return `true` if this **MovieWriter**
is able to handle the given file path, `false` otherwise. Typically,
`_handles_file<class_MovieWriter_private_method__handles_file>`{.interpreted-text
role="ref"} is overridden as follows to allow the user to record a file
at any path with a given file extension:

    func _handles_file(path):
        # Allows specifying an output file with a `.mkv` file extension (case-insensitive),
        # either in the Project Settings or with the `--write-movie <path>` command line argument.
        return path.get_extension().to_lower() == "mkv"

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MovieWriter_private_method__write_begin}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_write_begin**(movie_size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, fps:
`int<class_int>`{.interpreted-text role="ref"}, base_path:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MovieWriter_private_method__write_begin>`{.interpreted-text
role="ref"}

Called once before the engine starts writing video and audio data.
`movie_size` is the width and height of the video to save. `fps` is the
number of frames per second specified in the project settings or using
the `--fixed-fps <fps>`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MovieWriter_private_method__write_end}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_write_end**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MovieWriter_private_method__write_end>`{.interpreted-text
role="ref"}

Called when the engine finishes writing. This occurs when the engine
quits by pressing the window manager\'s close button, or when
`SceneTree.quit<class_SceneTree_method_quit>`{.interpreted-text
role="ref"} is called.

\*\*Note:\*\* Pressing `Ctrl + C`{.interpreted-text role="kbd"} on the
terminal running the editor/project does *not* result in
`_write_end<class_MovieWriter_private_method__write_end>`{.interpreted-text
role="ref"} being called.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MovieWriter_private_method__write_frame}
::: {.rst-class}
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_write_frame**(frame_image: `Image<class_Image>`{.interpreted-text
role="ref"}, audio_frame_block: `const void*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MovieWriter_private_method__write_frame>`{.interpreted-text
role="ref"}

Called at the end of every rendered frame. The `frame_image` and
`audio_frame_block` function arguments should be written to.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MovieWriter_method_add_writer}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_writer**(writer:
`MovieWriter<class_MovieWriter>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_MovieWriter_method_add_writer>`{.interpreted-text
role="ref"}

Adds a writer to be usable by the engine. The supported file extensions
can be set by overriding
`_handles_file<class_MovieWriter_private_method__handles_file>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`add_writer<class_MovieWriter_method_add_writer>`{.interpreted-text
role="ref"} must be called early enough in the engine initialization to
work, as movie writing is designed to start at the same time as the rest
of the engine.