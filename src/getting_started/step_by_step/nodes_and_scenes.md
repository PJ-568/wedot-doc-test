# Nodes and Scenes {#doc_nodes_and_scenes}

In `doc_key_concepts_overview`{.interpreted-text role="ref"}, we saw
that a Godot game is a tree of scenes and that each scene is a tree of
nodes. In this lesson, we explain a bit more about them. You will also
create your first scene.

## Nodes

**Nodes are the fundamental building blocks of your game**. They are
like the ingredients in a recipe. There are dozens of kinds that can
display an image, play a sound, represent a camera, and much more.

![image](img/nodes_and_scenes_nodes.webp)

All nodes have the following characteristics:

- A name.
- Editable properties.
- They receive callbacks to update every frame.
- You can extend them with new properties and functions.
- You can add them to another node as a child.

The last characteristic is important. **Together, nodes form a tree**,
which is a powerful feature to organize projects. Since different nodes
have different functions, combining them produces more complex behavior.
As we saw before, you can build a playable character the camera follows
using a `CharacterBody2D <class_CharacterBody2D>`{.interpreted-text
role="ref"} node, a `Sprite2D <class_Sprite2D>`{.interpreted-text
role="ref"} node, a `Camera2D <class_Camera2D>`{.interpreted-text
role="ref"} node, and a
`CollisionShape2D <class_CollisionShape2D>`{.interpreted-text
role="ref"} node.

![image](img/nodes_and_scenes_character_nodes.webp)

## Scenes

When you organize nodes in a tree, like our character, we call this
construct a scene. Once saved, scenes work like new node types in the
editor, where you can add them as a child of an existing node. In that
case, the instance of the scene appears as a single node with its
internals hidden.

Scenes allow you to structure your game\'s code however you want. You
can **compose nodes** to create custom and complex node types, like a
game character that runs and jumps, a life bar, a chest with which you
can interact, and more.

![image](img/nodes_and_scenes_3d_scene_example.png)

The Godot editor essentially is a **scene editor**. It has plenty of
tools for editing 2D and 3D scenes, as well as user interfaces. A Godot
project can contain as many of these scenes as you need. The engine only
requires one as your application\'s **main scene**. This is the scene
Godot will first load when you or a player runs the game.

On top of acting like nodes, scenes have the following characteristics:

1.  They always have one root node, like the \"Player\" in our example.
2.  You can save them to your local drive and load them later.
3.  You can create as many instances of a scene as you\'d like. You
    could have five or ten characters in your game, created from your
    Character scene.

## Creating your first scene

Let\'s create our first scene with a single node. To do so, you will
need to
`create a new project <doc_creating_and_importing_projects>`{.interpreted-text
role="ref"} first. After opening the project, you should see an empty
editor.

![image](img/nodes_and_scenes_01_empty_editor.webp)

In an empty scene, the Scene dock on the left shows several options to
add a root node quickly. \"2D Scene\" adds a
`Node2D <class_Node2D>`{.interpreted-text role="ref"} node, \"3D Scene\"
adds a `Node3D <class_Node3D>`{.interpreted-text role="ref"} node, and
\"User Interface\" adds a `Control <class_Control>`{.interpreted-text
role="ref"} node. These presets are here for convenience; they are not
mandatory. \"Other Node\" lets you select any node to be the root node.
In an empty scene, \"Other Node\" is equivalent to pressing the \"Add
Child Node\" button at the top-left of the Scene dock, which usually
adds a new node as a child of the currently selected node.

We\'re going to add a single `Label <class_Label>`{.interpreted-text
role="ref"} node to our scene. Its function is to draw text on the
screen.

Press the \"Add Child Node\" button or \"Other Node\" to create a root
node.

![image](img/nodes_and_scenes_02_scene_dock.webp)

The Create Node dialog opens, showing the long list of available nodes.

![image](img/nodes_and_scenes_03_create_node_window.webp)

Select the Label node. You can type its name to filter down the list.

![image](img/nodes_and_scenes_04_create_label_window.webp)

Click on the Label node to select it and click the Create button at the
bottom of the window.

![image](img/nodes_and_scenes_05_editor_with_label.webp)

A lot happens when you add a scene\'s first node. The scene changes to
the 2D workspace because Label is a 2D node type. The Label appears,
selected, in the top-left corner of the viewport. The node appears in
the Scene dock on the left, and the node\'s properties appear in the
Inspector dock on the right.

## Changing a node\'s properties

The next step is to change the Label\'s \"Text\" property. Let\'s change
it to \"Hello World\".

Head to the Inspector dock on the right of the viewport. Click inside
the field below the Text property and type \"Hello World\".

![image](img/nodes_and_scenes_06_label_text.webp)

You will see the text draw in the viewport as you type.

::: {.seealso}
You can edit any property listed in the Inspector as we did with the
Text. For a complete reference of the Inspector dock, see
`doc_editor_inspector_dock`{.interpreted-text role="ref"}.
:::

You can move your Label node in the viewport by selecting the move tool
in the toolbar.

![image](img/nodes_and_scenes_07_move_tool.webp)

With the Label selected, click and drag anywhere in the viewport to move
it to the center of the view delimited by the rectangle.

![image](img/nodes_and_scenes_08_hello_world_text.webp)

## Running the scene

Everything\'s ready to run the scene! Press the Play Scene button in the
top-right of the screen or press `F6`{.interpreted-text role="kbd"}
(`Cmd + R`{.interpreted-text role="kbd"} on macOS).

![image](img/nodes_and_scenes_09_play_scene_button.webp)

A popup invites you to save the scene, which is required to run it.
Click the Save button in the file browser to save it as `label.tscn`.

![image](img/nodes_and_scenes_10_save_scene_as.webp)

> [!NOTE]
> The Save Scene As dialog, like other file dialogs in the editor, only
> allows you to save files inside the project. The `res://` path at the
> top of the window represents the project\'s root directory and stands
> for \"resource path\". For more information about file paths in Godot,
> see `doc_filesystem`{.interpreted-text role="ref"}.

The application should open in a new window and display the text \"Hello
World\".

![image](img/nodes_and_scenes_11_final_result.webp)

Close the window or press `F8`{.interpreted-text role="kbd"}
(`Cmd + .`{.interpreted-text role="kbd"} on macOS) to quit the running
scene.

## Setting the main scene

To run our test scene, we used the Run Current Scene button. Another
button next to it allows you to set and run the project\'s main scene.
You can press `F5`{.interpreted-text role="kbd"}
(`Cmd + B`{.interpreted-text role="kbd"} on macOS) to do so.

![image](img/nodes_and_scenes_12_play_button.webp)

A popup window appears and invites you to select the main scene.

![image](img/nodes_and_scenes_13_main_scene_popup.webp)

Click the Select button, and in the file dialog that appears, double
click on `label.tscn`.

![image](img/nodes_and_scenes_14_select_main_scene.webp)

The demo should run again. Moving forward, every time you run the
project, Godot will use this scene as a starting point.

> [!NOTE]
> The editor saves the main scene\'s path in a project.godot file in
> your project\'s directory. While you can edit this text file directly
> to change project settings, you can also use the \"Project -\> Project
> Settings\" window to do so. For more information, see
> `doc_project_settings`{.interpreted-text role="ref"}.

In the next part, we will discuss another key concept in games and in
Godot: creating instances of a scene.
