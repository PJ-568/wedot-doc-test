github_url

:   hide

# AudioStreamGenerator {#class_AudioStreamGenerator}

**Inherits:** `AudioStream<class_AudioStream>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

An audio stream with utilities for procedural sound generation.

::: {.rst-class}
classref-introduction-group
:::

## Description

**AudioStreamGenerator** is a type of audio stream that does not play
back sounds on its own; instead, it expects a script to generate audio
data for it. See also
`AudioStreamGeneratorPlayback<class_AudioStreamGeneratorPlayback>`{.interpreted-text
role="ref"}.

Here\'s a sample on how to use it to generate a sine wave:

::::: {.tabs}
::: {.code-tab}
gdscript

var playback \# Will hold the AudioStreamGeneratorPlayback. @onready var
sample_hz = \$AudioStreamPlayer.stream.mix_rate var pulse_hz = 440.0 \#
The frequency of the sound wave.

func \_ready():

:   \$AudioStreamPlayer.play() playback =
    \$AudioStreamPlayer.get_stream_playback() fill_buffer()

func fill_buffer():

:   var phase = 0.0 var increment = pulse_hz / sample_hz var
    frames_available = playback.get_frames_available()

    for i in range(frames_available):

    :   playback.push_frame(Vector2.ONE \* sin(phase \* TAU)) phase =
        fmod(phase + increment, 1.0)
:::

::: {.code-tab}
csharp

\[Export\] public AudioStreamPlayer Player { get; set; }

private AudioStreamGeneratorPlayback \_playback; // Will hold the
AudioStreamGeneratorPlayback. private float \_sampleHz; private float
\_pulseHz = 440.0f; // The frequency of the sound wave.

public override void \_Ready() { if (Player.Stream is
AudioStreamGenerator generator) // Type as a generator to access
MixRate. { \_sampleHz = generator.MixRate; Player.Play(); \_playback =
(AudioStreamGeneratorPlayback)Player.GetStreamPlayback(); FillBuffer();
} }

public void FillBuffer() { double phase = 0.0; float increment =
\_pulseHz / \_sampleHz; int framesAvailable =
\_playback.GetFramesAvailable();

> for (int i = 0; i \< framesAvailable; i++) {
> \_playback.PushFrame(Vector2.One \* (float)Mathf.Sin(phase \*
> Mathf.Tau)); phase = Mathf.PosMod(phase + increment, 1.0); }

}
:::
:::::

In the example above, the \"AudioStreamPlayer\" node must use an
**AudioStreamGenerator** as its stream. The `fill_buffer` function
provides audio data for approximating a sine wave.

See also
`AudioEffectSpectrumAnalyzer<class_AudioEffectSpectrumAnalyzer>`{.interpreted-text
role="ref"} for performing real-time audio spectrum analysis.

\*\*Note:\*\* Due to performance constraints, this class is best used
from C# or from a compiled language via GDExtension. If you still want
to use this class from GDScript, consider using a lower
`mix_rate<class_AudioStreamGenerator_property_mix_rate>`{.interpreted-text
role="ref"} such as 11,025 Hz or 22,050 Hz.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- [Audio Generator
  Demo](https://godotengine.org/asset-library/asset/2759)

::: {.rst-class}
classref-reftable-group
:::

## Properties

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

## Property Descriptions

:::: {#class_AudioStreamGenerator_property_buffer_length}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **buffer_length** =
`0.5`
`🔗<class_AudioStreamGenerator_property_buffer_length>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_buffer_length**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_buffer_length**()

The length of the buffer to generate (in seconds). Lower values result
in less latency, but require the script to generate audio data faster,
resulting in increased CPU usage and more risk for audio cracking if the
CPU can\'t keep up.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioStreamGenerator_property_mix_rate}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **mix_rate** =
`44100.0`
`🔗<class_AudioStreamGenerator_property_mix_rate>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mix_rate**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_mix_rate**()

The sample rate to use (in Hz). Higher values are more demanding for the
CPU to generate, but result in better quality.

In games, common sample rates in use are `11025`, `16000`, `22050`,
`32000`, `44100`, and `48000`.

According to the [Nyquist-Shannon sampling
theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem),
there is no quality difference to human hearing when going past 40,000
Hz (since most humans can only hear up to \~20,000 Hz, often less). If
you are generating lower-pitched sounds such as voices, lower sample
rates such as `32000` or `22050` may be usable with no loss in quality.
