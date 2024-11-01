github_url

:   hide

# EditorSelection {#class_EditorSelection}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Manages the SceneTree selection in the editor.

::: {.rst-class}
classref-introduction-group
:::

## Description

This object manages the SceneTree selection in the editor.

\*\*Note:\*\* This class shouldn\'t be instantiated directly. Instead,
access the singleton using
`EditorInterface.get_selection<class_EditorInterface_method_get_selection>`{.interpreted-text
role="ref"}.

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

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Signals

:::: {#class_EditorSelection_signal_selection_changed}
::: {.rst-class}
classref-signal
:::
::::

**selection_changed**()
`🔗<class_EditorSelection_signal_selection_changed>`{.interpreted-text
role="ref"}

Emitted when the selection changes.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorSelection_method_add_node}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_node**(node: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_EditorSelection_method_add_node>`{.interpreted-text
role="ref"}

Adds a node to the selection.

\*\*Note:\*\* The newly selected node will not be automatically edited
in the inspector. If you want to edit a node, use
`EditorInterface.edit_node<class_EditorInterface_method_edit_node>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSelection_method_clear}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_EditorSelection_method_clear>`{.interpreted-text role="ref"}

Clear the selection.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSelection_method_get_selected_nodes}
::: {.rst-class}
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Node<class_Node>`{.interpreted-text role="ref"}\]
**get_selected_nodes**()
`🔗<class_EditorSelection_method_get_selected_nodes>`{.interpreted-text
role="ref"}

Returns the list of selected nodes.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSelection_method_get_transformable_selected_nodes}
::: {.rst-class}
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Node<class_Node>`{.interpreted-text role="ref"}\]
**get_transformable_selected_nodes**()
`🔗<class_EditorSelection_method_get_transformable_selected_nodes>`{.interpreted-text
role="ref"}

Returns the list of selected nodes, optimized for transform operations
(i.e. moving them, rotating, etc.). This list can be used to avoid
situations where a node is selected and is also a child/grandchild.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSelection_method_remove_node}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_node**(node: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_EditorSelection_method_remove_node>`{.interpreted-text
role="ref"}

Removes a node from the selection.
