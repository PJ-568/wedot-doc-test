github_url

:   hide

# NavigationPathQueryParameters2D {#class_NavigationPathQueryParameters2D}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides parameters for 2D navigation path queries.

::: {.rst-class}
classref-introduction-group
:::

## Description

By changing various properties of this object, such as the start and
target position, you can configure path queries to the
`NavigationServer2D<class_NavigationServer2D>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- `Using NavigationPathQueryObjects <../tutorials/navigation/navigation_using_navigationpathqueryobjects>`{.interpreted-text
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

## Enumerations

:::: {#enum_NavigationPathQueryParameters2D_PathfindingAlgorithm}
::: {.rst-class}
classref-enumeration
:::
::::

enum **PathfindingAlgorithm**:
`🔗<enum_NavigationPathQueryParameters2D_PathfindingAlgorithm>`{.interpreted-text
role="ref"}

:::: {#class_NavigationPathQueryParameters2D_constant_PATHFINDING_ALGORITHM_ASTAR}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`PathfindingAlgorithm<enum_NavigationPathQueryParameters2D_PathfindingAlgorithm>`{.interpreted-text
role="ref"} **PATHFINDING_ALGORITHM_ASTAR** = `0`

The path query uses the default A\* pathfinding algorithm.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_NavigationPathQueryParameters2D_PathPostProcessing}
::: {.rst-class}
classref-enumeration
:::
::::

enum **PathPostProcessing**:
`🔗<enum_NavigationPathQueryParameters2D_PathPostProcessing>`{.interpreted-text
role="ref"}

:::: {#class_NavigationPathQueryParameters2D_constant_PATH_POSTPROCESSING_CORRIDORFUNNEL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`PathPostProcessing<enum_NavigationPathQueryParameters2D_PathPostProcessing>`{.interpreted-text
role="ref"} **PATH_POSTPROCESSING_CORRIDORFUNNEL** = `0`

Applies a funnel algorithm to the raw path corridor found by the
pathfinding algorithm. This will result in the shortest path possible
inside the path corridor. This postprocessing very much depends on the
navigation mesh polygon layout and the created corridor. Especially
tile- or gridbased layouts can face artificial corners with diagonal
movement due to a jagged path corridor imposed by the cell shapes.

:::: {#class_NavigationPathQueryParameters2D_constant_PATH_POSTPROCESSING_EDGECENTERED}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`PathPostProcessing<enum_NavigationPathQueryParameters2D_PathPostProcessing>`{.interpreted-text
role="ref"} **PATH_POSTPROCESSING_EDGECENTERED** = `1`

Centers every path position in the middle of the traveled navigation
mesh polygon edge. This creates better paths for tile- or gridbased
layouts that restrict the movement to the cells center.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_NavigationPathQueryParameters2D_PathMetadataFlags}
::: {.rst-class}
classref-enumeration
:::
::::

flags **PathMetadataFlags**:
`🔗<enum_NavigationPathQueryParameters2D_PathMetadataFlags>`{.interpreted-text
role="ref"}

:::: {#class_NavigationPathQueryParameters2D_constant_PATH_METADATA_INCLUDE_NONE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`PathMetadataFlags<enum_NavigationPathQueryParameters2D_PathMetadataFlags>`{.interpreted-text
role="ref"} **PATH_METADATA_INCLUDE_NONE** = `0`

Don\'t include any additional metadata about the returned path.

:::: {#class_NavigationPathQueryParameters2D_constant_PATH_METADATA_INCLUDE_TYPES}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`PathMetadataFlags<enum_NavigationPathQueryParameters2D_PathMetadataFlags>`{.interpreted-text
role="ref"} **PATH_METADATA_INCLUDE_TYPES** = `1`

Include the type of navigation primitive (region or link) that each
point of the path goes through.

:::: {#class_NavigationPathQueryParameters2D_constant_PATH_METADATA_INCLUDE_RIDS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`PathMetadataFlags<enum_NavigationPathQueryParameters2D_PathMetadataFlags>`{.interpreted-text
role="ref"} **PATH_METADATA_INCLUDE_RIDS** = `2`

Include the `RID<class_RID>`{.interpreted-text role="ref"}s of the
regions and links that each point of the path goes through.

:::: {#class_NavigationPathQueryParameters2D_constant_PATH_METADATA_INCLUDE_OWNERS}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`PathMetadataFlags<enum_NavigationPathQueryParameters2D_PathMetadataFlags>`{.interpreted-text
role="ref"} **PATH_METADATA_INCLUDE_OWNERS** = `4`

Include the `ObjectID`s of the `Object<class_Object>`{.interpreted-text
role="ref"}s which manage the regions and links each point of the path
goes through.

:::: {#class_NavigationPathQueryParameters2D_constant_PATH_METADATA_INCLUDE_ALL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`PathMetadataFlags<enum_NavigationPathQueryParameters2D_PathMetadataFlags>`{.interpreted-text
role="ref"} **PATH_METADATA_INCLUDE_ALL** = `7`

Include all available metadata about the returned path.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_NavigationPathQueryParameters2D_property_map}
::: {.rst-class}
classref-property
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **map** = `RID()`
`🔗<class_NavigationPathQueryParameters2D_property_map>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_map**(value: `RID<class_RID>`{.interpreted-text role="ref"})
- `RID<class_RID>`{.interpreted-text role="ref"} **get_map**()

The navigation map `RID<class_RID>`{.interpreted-text role="ref"} used
in the path query.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPathQueryParameters2D_property_metadata_flags}
::: {.rst-class}
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`PathMetadataFlags<enum_NavigationPathQueryParameters2D_PathMetadataFlags>`{.interpreted-text
role="ref"}\] **metadata_flags** = `7`
`🔗<class_NavigationPathQueryParameters2D_property_metadata_flags>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_metadata_flags**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`PathMetadataFlags<enum_NavigationPathQueryParameters2D_PathMetadataFlags>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`PathMetadataFlags<enum_NavigationPathQueryParameters2D_PathMetadataFlags>`{.interpreted-text
  role="ref"}\] **get_metadata_flags**()

Additional information to include with the navigation path.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPathQueryParameters2D_property_navigation_layers}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **navigation_layers** =
`1`
`🔗<class_NavigationPathQueryParameters2D_property_navigation_layers>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_navigation_layers**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_navigation_layers**()

The navigation layers the query will use (as a bitmask).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPathQueryParameters2D_property_path_postprocessing}
::: {.rst-class}
classref-property
:::
::::

`PathPostProcessing<enum_NavigationPathQueryParameters2D_PathPostProcessing>`{.interpreted-text
role="ref"} **path_postprocessing** = `0`
`🔗<class_NavigationPathQueryParameters2D_property_path_postprocessing>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_postprocessing**(value:
  `PathPostProcessing<enum_NavigationPathQueryParameters2D_PathPostProcessing>`{.interpreted-text
  role="ref"})
- `PathPostProcessing<enum_NavigationPathQueryParameters2D_PathPostProcessing>`{.interpreted-text
  role="ref"} **get_path_postprocessing**()

The path postprocessing applied to the raw path corridor found by the
`pathfinding_algorithm<class_NavigationPathQueryParameters2D_property_pathfinding_algorithm>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPathQueryParameters2D_property_pathfinding_algorithm}
::: {.rst-class}
classref-property
:::
::::

`PathfindingAlgorithm<enum_NavigationPathQueryParameters2D_PathfindingAlgorithm>`{.interpreted-text
role="ref"} **pathfinding_algorithm** = `0`
`🔗<class_NavigationPathQueryParameters2D_property_pathfinding_algorithm>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pathfinding_algorithm**(value:
  `PathfindingAlgorithm<enum_NavigationPathQueryParameters2D_PathfindingAlgorithm>`{.interpreted-text
  role="ref"})
- `PathfindingAlgorithm<enum_NavigationPathQueryParameters2D_PathfindingAlgorithm>`{.interpreted-text
  role="ref"} **get_pathfinding_algorithm**()

The pathfinding algorithm used in the path query.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPathQueryParameters2D_property_simplify_epsilon}
::: {.rst-class}
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **simplify_epsilon**
= `0.0`
`🔗<class_NavigationPathQueryParameters2D_property_simplify_epsilon>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_simplify_epsilon**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_simplify_epsilon**()

The path simplification amount in worlds units.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPathQueryParameters2D_property_simplify_path}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **simplify_path** =
`false`
`🔗<class_NavigationPathQueryParameters2D_property_simplify_path>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_simplify_path**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_simplify_path**()

If `true` a simplified version of the path will be returned with less
critical path points removed. The simplification amount is controlled by
`simplify_epsilon<class_NavigationPathQueryParameters2D_property_simplify_epsilon>`{.interpreted-text
role="ref"}. The simplification uses a variant of Ramer-Douglas-Peucker
algorithm for curve point decimation.

Path simplification can be helpful to mitigate various path following
issues that can arise with certain agent types and script behaviors.
E.g. \"steering\" agents or avoidance in \"open fields\".

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPathQueryParameters2D_property_start_position}
::: {.rst-class}
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**start_position** = `Vector2(0, 0)`
`🔗<class_NavigationPathQueryParameters2D_property_start_position>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_start_position**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_start_position**()

The pathfinding start position in global coordinates.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPathQueryParameters2D_property_target_position}
::: {.rst-class}
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**target_position** = `Vector2(0, 0)`
`🔗<class_NavigationPathQueryParameters2D_property_target_position>`{.interpreted-text
role="ref"}

::: {.rst-class}
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_position**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_target_position**()

The pathfinding target position in global coordinates.
