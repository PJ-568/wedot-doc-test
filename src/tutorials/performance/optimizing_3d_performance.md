::: {.meta keywords="optimization"}
:::

# Optimizing 3D performance {#doc_optimizing_3d_performance}

## Culling

Godot will automatically perform view frustum culling in order to
prevent rendering objects that are outside the viewport. This works well
for games that take place in a small area, however things can quickly
become problematic in larger levels.

### Occlusion culling

Walking around a town for example, you may only be able to see a few
buildings in the street you are in, as well as the sky and a few birds
flying overhead. As far as a naive renderer is concerned however, you
can still see the entire town. It won\'t just render the buildings in
front of you, it will render the street behind that, with the people on
that street, the buildings behind that. You quickly end up in situations
where you are attempting to render 10× or 100× more than what is
visible.

Things aren\'t quite as bad as they seem, because the Z-buffer usually
allows the GPU to only fully shade the objects that are at the front.
This is called *depth prepass* and is enabled by default in Godot when
using the Forward+ or Compatibility rendering methods. However, unneeded
objects are still reducing performance.

One way we can potentially reduce the amount to be rendered is to **take
advantage of occlusion**. Godot 4.0 and later offers a new approach to
occlusion culling using occluder nodes. See
`doc_occlusion_culling`{.interpreted-text role="ref"} for instructions
on setting up occlusion culling in your scene.

> [!NOTE]
> In some cases, you may have to adapt your level design to add more
> occlusion opportunities. For example, you may have to add more walls
> to prevent the player from seeing too far away, which would decrease
> performance due to the lost opportunities for occlusion culling.

## Transparent objects

Godot sorts objects by `Material <class_Material>`{.interpreted-text
role="ref"} and `Shader
<class_Shader>`{.interpreted-text role="ref"} to improve performance.
This, however, can not be done with transparent objects. Transparent
objects are rendered from back to front to make blending with what is
behind work. As a result, **try to use as few transparent objects as
possible**. If an object has a small section with transparency, try to
make that section a separate surface with its own material.

For more information, see the
`GPU optimizations <doc_gpu_optimization>`{.interpreted-text role="ref"}
doc.

## Level of detail (LOD)

In some situations, particularly at a distance, it can be a good idea to
**replace complex geometry with simpler versions**. The end user will
probably not be able to see much difference. Consider looking at a large
number of trees in the far distance. There are several strategies for
replacing models at varying distance. You could use lower poly models,
or use transparency to simulate more complex geometry.

Godot 4 offers several ways to control level of detail:

- An automatic approach on mesh import using
  `doc_mesh_lod`{.interpreted-text role="ref"}.
- A manual approach configured in the 3D node using
  `doc_visibility_ranges`{.interpreted-text role="ref"}.
- `Decals <doc_using_decals>`{.interpreted-text role="ref"} and
  `lights <doc_lights_and_shadows>`{.interpreted-text role="ref"} can
  also benefit from level of detail using their respective **Distance
  Fade** properties.

While they can be used independently, these approaches are most
effective when used together. For example, you can set up visibility
ranges to hide particle effects that are too far away from the player to
notice. At the same time, you can rely on mesh LOD to make the particle
effect\'s meshes rendered with less detail at a distance.

Visibility ranges are also a good way to set up *impostors* for distant
geometry (see below).

### Billboards and imposters

The simplest version of using transparency to deal with LOD is
billboards. For example, you can use a single transparent quad to
represent a tree at distance. This can be very cheap to render, unless
of course, there are many trees in front of each other. In this case,
transparency may start eating into fill rate (for more information on
fill rate, see `doc_gpu_optimization`{.interpreted-text role="ref"}).

An alternative is to render not just one tree, but a number of trees
together as a group. This can be especially effective if you can see an
area but cannot physically approach it in a game.

You can make imposters by pre-rendering views of an object at different
angles. Or you can even go one step further, and periodically re-render
a view of an object onto a texture to be used as an imposter. At a
distance, you need to move the viewer a considerable distance for the
angle of view to change significantly. This can be complex to get
working, but may be worth it depending on the type of project you are
making.

### Use instancing (MultiMesh)

If several identical objects have to be drawn in the same place or
nearby, try using `MultiMesh <class_MultiMesh>`{.interpreted-text
role="ref"} instead. MultiMesh allows the drawing of many thousands of
objects at very little performance cost, making it ideal for flocks,
grass, particles, and anything else where you have thousands of
identical objects.

See also the `Using MultiMesh <doc_using_multimesh>`{.interpreted-text
role="ref"} documentation.

## Bake lighting

Lighting objects is one of the most costly rendering operations.
Realtime lighting, shadows (especially multiple lights), and
`global illumination <doc_introduction_to_global_illumination>`{.interpreted-text
role="ref"} are especially expensive. They may simply be too much for
lower power mobile devices to handle.

**Consider using baked lighting**, especially for mobile. This can look
fantastic, but has the downside that it will not be dynamic. Sometimes,
this is a tradeoff worth making.

See `doc_using_lightmap_gi`{.interpreted-text role="ref"} for
instructions on using baked lightmaps. For best performance, you should
set lights\' bake mode to **Static** as opposed to the default
**Dynamic**, as this will skip real-time lighting on meshes that have
baked lighting.

The downside of lights with the **Static** bake mode is that they can\'t
cast shadows onto meshes with baked lighting. This can make scenes with
outdoor environments and dynamic objects look flat. A good balance
between performance and quality is to keep **Dynamic** for the
`class_DirectionalLight3D`{.interpreted-text role="ref"} node, and use
**Static** for most (if not all) omni and spot lights.

## Animation and skinning

Animation and vertex animation such as skinning and morphing can be very
expensive on some platforms. You may need to lower the polycount
considerably for animated models, or limit the number of them on screen
at any given time. You can also reduce the animation rate for distant or
occluded meshes, or pause the animation entirely if the player is
unlikely to notice the animation being stopped.

The `class_VisibleOnScreenEnabler3D`{.interpreted-text role="ref"} and
`class_VisibleOnScreenNotifier3D`{.interpreted-text role="ref"} nodes
can be useful for this purpose.

## Large worlds

If you are making large worlds, there are different considerations than
what you may be familiar with from smaller games.

Large worlds may need to be built in tiles that can be loaded on demand
as you move around the world. This can prevent memory use from getting
out of hand, and also limit the processing needed to the local area.

There may also be rendering and physics glitches due to floating point
error in large worlds. This can be resolved using
`doc_large_world_coordinates`{.interpreted-text role="ref"}. If using
large world coordinates is not an option, you may be able to use
techniques such as orienting the world around the player (rather than
the other way around), or shifting the origin periodically to keep
things centred around `Vector3(0, 0, 0)`.