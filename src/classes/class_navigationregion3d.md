github_url

:   hide

# NavigationRegion3D {#class_NavigationRegion3D}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A traversable 3D region that
`NavigationAgent3D<class_NavigationAgent3D>`{.interpreted-text
role="ref"}s can use for pathfinding.

::: {.rst-class}
classref-introduction-group
:::

## Description

A traversable 3D region based on a
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"}
that `NavigationAgent3D<class_NavigationAgent3D>`{.interpreted-text
role="ref"}s can use for pathfinding.

Two regions can be connected to each other if they share a similar edge.
You can set the minimum distance between two vertices required to
connect two edges by using
`NavigationServer3D.map_set_edge_connection_margin<class_NavigationServer3D_method_map_set_edge_connection_margin>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Overlapping two regions\' navigation meshes is not enough
for connecting two regions. They must share a similar edge.

The cost of entering this region from another region can be controlled
with the
`enter_cost<class_NavigationRegion3D_property_enter_cost>`{.interpreted-text
role="ref"} value.

\*\*Note:\*\* This value is not added to the path cost when the start
position is already inside this region.

The cost of traveling distances inside this region can be controlled
with the
`travel_cost<class_NavigationRegion3D_property_travel_cost>`{.interpreted-text
role="ref"} multiplier.

\*\*Note:\*\* This node caches changes to its properties, so if you make
changes to the underlying region `RID<class_RID>`{.interpreted-text
role="ref"} in
`NavigationServer3D<class_NavigationServer3D>`{.interpreted-text
role="ref"}, they will not be reflected in this node\'s properties.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- `Using NavigationRegions <../tutorials/navigation/navigation_using_navigationregions>`{.interpreted-text
  role="doc"}

::: {.rst-class}
classref-reftable-group
:::

## Properties

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

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Signals

:::: {#class_NavigationRegion3D_signal_bake_finished}
::: {.rst-class}
classref-signal
:::
::::

**bake_finished**()
`🔗<class_NavigationRegion3D_signal_bake_finished>`{.interpreted-text
role="ref"}

Notifies when the navigation mesh bake operation is completed.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationRegion3D_signal_navigation_mesh_changed}
::: {.rst-class}
classref-signal
:::
::::

**navigation_mesh_changed**()
`🔗<class_NavigationRegion3D_signal_navigation_mesh_changed>`{.interpreted-text
role="ref"}

Notifies when the
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"} has
changed.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_NavigationRegion3D_property_enabled}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enabled** = `true`
`🔗<class_NavigationRegion3D_property_enabled>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_enabled**()

Determines if the **NavigationRegion3D** is enabled or disabled.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationRegion3D_property_enter_cost}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **enter_cost** =
`0.0`
`🔗<class_NavigationRegion3D_property_enter_cost>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enter_cost**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_enter_cost**()

When pathfinding enters this region\'s navigation mesh from another
regions navigation mesh the
`enter_cost<class_NavigationRegion3D_property_enter_cost>`{.interpreted-text
role="ref"} value is added to the path distance for determining the
shortest path.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationRegion3D_property_navigation_layers}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **navigation_layers** =
`1`
`🔗<class_NavigationRegion3D_property_navigation_layers>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_navigation_layers**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_navigation_layers**()

A bitfield determining all navigation layers the region belongs to.
These navigation layers can be checked upon when requesting a path with
`NavigationServer3D.map_get_path<class_NavigationServer3D_method_map_get_path>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationRegion3D_property_navigation_mesh}
::: {.rst-class}
classref-property
:::
::::

`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"}
**navigation_mesh**
`🔗<class_NavigationRegion3D_property_navigation_mesh>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_navigation_mesh**(value:
  `NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"})
- `NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"}
  **get_navigation_mesh**()

The `NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"}
resource to use.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationRegion3D_property_travel_cost}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **travel_cost** =
`1.0`
`🔗<class_NavigationRegion3D_property_travel_cost>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_travel_cost**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_travel_cost**()

When pathfinding moves inside this region\'s navigation mesh the
traveled distances are multiplied with
`travel_cost<class_NavigationRegion3D_property_travel_cost>`{.interpreted-text
role="ref"} for determining the shortest path.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationRegion3D_property_use_edge_connections}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**use_edge_connections** = `true`
`🔗<class_NavigationRegion3D_property_use_edge_connections>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_edge_connections**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_use_edge_connections**()

If enabled the navigation region will use edge connections to connect
with other navigation regions within proximity of the navigation map
edge connection margin.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_NavigationRegion3D_method_bake_navigation_mesh}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**bake_navigation_mesh**(on_thread: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_NavigationRegion3D_method_bake_navigation_mesh>`{.interpreted-text
role="ref"}

Bakes the `NavigationMesh<class_NavigationMesh>`{.interpreted-text
role="ref"}. If `on_thread` is set to `true` (default), the baking is
done on a separate thread. Baking on separate thread is useful because
navigation baking is not a cheap operation. When it is completed, it
automatically sets the new
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"}.
Please note that baking on separate thread may be very slow if geometry
is parsed from meshes as async access to each mesh involves heavy
synchronization. Also, please note that baking on a separate thread is
automatically disabled on operating systems that cannot use threads
(such as Web with threads disabled).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationRegion3D_method_get_navigation_layer_value}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_navigation_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationRegion3D_method_get_navigation_layer_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`navigation_layers<class_NavigationRegion3D_property_navigation_layers>`{.interpreted-text
role="ref"} bitmask is enabled, given a `layer_number` between 1 and 32.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationRegion3D_method_get_navigation_map}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_navigation_map**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationRegion3D_method_get_navigation_map>`{.interpreted-text
role="ref"}

Returns the current navigation map `RID<class_RID>`{.interpreted-text
role="ref"} used by this region.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationRegion3D_method_get_region_rid}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_region_rid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationRegion3D_method_get_region_rid>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`get_rid<class_NavigationRegion3D_method_get_rid>`{.interpreted-text
role="ref"} instead.

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of this
region on the
`NavigationServer3D<class_NavigationServer3D>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationRegion3D_method_get_rid}
::: {.rst-class}
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_rid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationRegion3D_method_get_rid>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of this
region on the
`NavigationServer3D<class_NavigationServer3D>`{.interpreted-text
role="ref"}. Combined with
`NavigationServer3D.map_get_closest_point_owner<class_NavigationServer3D_method_map_get_closest_point_owner>`{.interpreted-text
role="ref"} can be used to identify the **NavigationRegion3D** closest
to a point on the merged navigation map.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationRegion3D_method_is_baking}
::: {.rst-class}
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_baking**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationRegion3D_method_is_baking>`{.interpreted-text
role="ref"}

Returns `true` when the
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"} is
being baked on a background thread.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationRegion3D_method_set_navigation_layer_value}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_navigation_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationRegion3D_method_set_navigation_layer_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`navigation_layers<class_NavigationRegion3D_property_navigation_layers>`{.interpreted-text
role="ref"} bitmask, given a `layer_number` between 1 and 32.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationRegion3D_method_set_navigation_map}
::: {.rst-class}
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_navigation_map**(navigation_map:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_NavigationRegion3D_method_set_navigation_map>`{.interpreted-text
role="ref"}

Sets the `RID<class_RID>`{.interpreted-text role="ref"} of the
navigation map this region should use. By default the region will
automatically join the `World3D<class_World3D>`{.interpreted-text
role="ref"} default navigation map so this function is only required to
override the default map.
