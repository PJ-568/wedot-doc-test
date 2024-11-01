github_url

:   hide

# Signal {#class_Signal}

A built-in type representing a signal of an
`Object<class_Object>`{.interpreted-text role="ref"}.

::: {.rst-class}
classref-introduction-group
:::

## Description

**Signal** is a built-in `Variant<class_Variant>`{.interpreted-text
role="ref"} type that represents a signal of an
`Object<class_Object>`{.interpreted-text role="ref"} instance. Like all
`Variant<class_Variant>`{.interpreted-text role="ref"} types, it can be
stored in variables and passed to functions. Signals allow all connected
`Callable<class_Callable>`{.interpreted-text role="ref"}s (and by
extension their respective objects) to listen and react to events,
without directly referencing one another. This keeps the code flexible
and easier to manage. You can check whether an
`Object<class_Object>`{.interpreted-text role="ref"} has a given signal
name using
`Object.has_signal<class_Object_method_has_signal>`{.interpreted-text
role="ref"}.

In GDScript, signals can be declared with the `signal` keyword. In C#,
you may use the `[Signal]` attribute on a delegate.

::::: {.tabs}
::: {.code-tab}
gdscript

signal attacked

\# Additional arguments may be declared. \# These arguments must be
passed when the signal is emitted. signal item_dropped(item_name,
amount)
:::

::: {.code-tab}
csharp

\[Signal\] delegate void AttackedEventHandler();

// Additional arguments may be declared. // These arguments must be
passed when the signal is emitted. \[Signal\] delegate void
ItemDroppedEventHandler(string itemName, int amount);
:::
:::::

> [!NOTE]
> There are notable differences when using this API with C#. See
> `doc_c_sharp_differences`{.interpreted-text role="ref"} for more
> information.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- `Using Signals <../getting_started/step_by_step/signals>`{.interpreted-text
  role="doc"}
- [GDScript
  Basics](../tutorials/scripting/gdscript/gdscript_basics.html#signals)

::: {.rst-class}
classref-reftable-group
:::

## Constructors

||
||
||
||
||

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
||
||
||

::: {.rst-class}
classref-reftable-group
:::

## Operators

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

## Constructor Descriptions

:::: {#class_Signal_constructor_Signal}
::: {.rst-class}
classref-constructor
:::
::::

`Signal<class_Signal>`{.interpreted-text role="ref"} **Signal**()
`🔗<class_Signal_constructor_Signal>`{.interpreted-text role="ref"}

Constructs an empty **Signal** with no object nor signal name bound.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-constructor
:::

`Signal<class_Signal>`{.interpreted-text role="ref"} **Signal**(from:
`Signal<class_Signal>`{.interpreted-text role="ref"})

Constructs a **Signal** as a copy of the given **Signal**.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-constructor
:::

`Signal<class_Signal>`{.interpreted-text role="ref"} **Signal**(object:
`Object<class_Object>`{.interpreted-text role="ref"}, signal:
`StringName<class_StringName>`{.interpreted-text role="ref"})

Creates a **Signal** object referencing a signal named `signal` in the
specified `object`.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Signal_method_connect}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **connect**(callable:
`Callable<class_Callable>`{.interpreted-text role="ref"}, flags:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_Signal_method_connect>`{.interpreted-text role="ref"}

Connects this signal to the specified `callable`. Optional `flags` can
be also added to configure the connection\'s behavior (see
`ConnectFlags<enum_Object_ConnectFlags>`{.interpreted-text role="ref"}
constants). You can provide additional arguments to the connected
`callable` by using
`Callable.bind<class_Callable_method_bind>`{.interpreted-text
role="ref"}.

A signal can only be connected once to the same
`Callable<class_Callable>`{.interpreted-text role="ref"}. If the signal
is already connected, returns
`@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>`{.interpreted-text
role="ref"} and pushes an error message, unless the signal is connected
with
`Object.CONNECT_REFERENCE_COUNTED<class_Object_constant_CONNECT_REFERENCE_COUNTED>`{.interpreted-text
role="ref"}. To prevent this, use
`is_connected<class_Signal_method_is_connected>`{.interpreted-text
role="ref"} first to check for existing connections.

    for button in $Buttons.get_children():
        button.pressed.connect(_on_pressed.bind(button))

    func _on_pressed(button):
        print(button.name, " was pressed")

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_disconnect}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**disconnect**(callable: `Callable<class_Callable>`{.interpreted-text
role="ref"}) `🔗<class_Signal_method_disconnect>`{.interpreted-text
role="ref"}

Disconnects this signal from the specified
`Callable<class_Callable>`{.interpreted-text role="ref"}. If the
connection does not exist, generates an error. Use
`is_connected<class_Signal_method_is_connected>`{.interpreted-text
role="ref"} to make sure that the connection exists.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_emit}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **emit**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_emit>`{.interpreted-text
role="ref"}

Emits this signal. All `Callable<class_Callable>`{.interpreted-text
role="ref"}s connected to this signal will be triggered. This method
supports a variable number of arguments, so parameters can be passed as
a comma separated list.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_get_connections}
::: {.rst-class}
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **get_connections**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_get_connections>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
connections for this signal. Each connection is represented as a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} that
contains three entries:

- `signal` is a reference to this signal;
- `callable` is a reference to the connected
  `Callable<class_Callable>`{.interpreted-text role="ref"};
- `flags` is a combination of
  `ConnectFlags<enum_Object_ConnectFlags>`{.interpreted-text
  role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_get_name}
::: {.rst-class}
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_get_name>`{.interpreted-text
role="ref"}

Returns the name of this signal.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_get_object}
::: {.rst-class}
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"} **get_object**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_get_object>`{.interpreted-text
role="ref"}

Returns the object emitting this signal.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_get_object_id}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_object_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_get_object_id>`{.interpreted-text
role="ref"}

Returns the ID of the object emitting this signal (see
`Object.get_instance_id<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"}).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_has_connections}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_connections**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_has_connections>`{.interpreted-text
role="ref"}

Returns `true` if any `Callable<class_Callable>`{.interpreted-text
role="ref"} is connected to this signal.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_is_connected}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_connected**(callable: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_is_connected>`{.interpreted-text
role="ref"}

Returns `true` if the specified
`Callable<class_Callable>`{.interpreted-text role="ref"} is connected to
this signal.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_is_null}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_null**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_is_null>`{.interpreted-text
role="ref"}

Returns `true` if this **Signal** has no object and the signal name is
empty. Equivalent to `signal == Signal()`.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_Signal_operator_neq_Signal}
::: {.rst-class}
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Signal<class_Signal>`{.interpreted-text role="ref"})
`🔗<class_Signal_operator_neq_Signal>`{.interpreted-text role="ref"}

Returns `true` if the signals do not share the same object and name.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_operator_eq_Signal}
::: {.rst-class}
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Signal<class_Signal>`{.interpreted-text role="ref"})
`🔗<class_Signal_operator_eq_Signal>`{.interpreted-text role="ref"}

Returns `true` if both signals share the same object and name.
