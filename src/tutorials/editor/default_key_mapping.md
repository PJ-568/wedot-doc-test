article_outdated

:   True

::: {.meta keywords="cheatsheet, cheat sheet, shortcut"}
:::

# Default editor shortcuts {#doc_default_key_mapping}

Many Godot editor functions can be executed with keyboard shortcuts.
This page lists functions which have associated shortcuts by default,
but many others are available for customization in editor settings as
well. To change keys associated with these and other actions navigate to
**Editor \> Editor Settings \> Shortcuts**.

While some actions are universal, a lot of shortcuts are specific to
individual tools. For this reason it is possible for some key
combinations to be assigned to more than one function. The correct
action will be performed depending on the context.

> [!NOTE]
> While Windows and Linux builds of the editor share most of the default
> settings, some shortcuts may differ for macOS version. This is done
> for better integration of the editor into macOS ecosystem. Users
> fluent with standard shortcuts on that OS should find Godot Editor\'s
> default key mapping intuitive.

## General editor actions

| Action name | Windows, Linux | macOS | Editor setting |
|----|----|----|----|
| Open 2D Editor | `Ctrl + F1`{.interpreted-text role="kbd"} | `Opt + 1`{.interpreted-text role="kbd"} | `editor/editor_2d` |
| Open 3D Editor | `Ctrl + F2`{.interpreted-text role="kbd"} | `Opt + 2`{.interpreted-text role="kbd"} | `editor/editor_3d` |
| Open Script Editor | `Ctrl + F3`{.interpreted-text role="kbd"} | `Opt + 3`{.interpreted-text role="kbd"} | `editor/editor_script` |
| Search Help | `F1`{.interpreted-text role="kbd"} | `Opt + Space`{.interpreted-text role="kbd"} | `editor/editor_help` |
| Distraction Free Mode | `Ctrl + Shift + F11`{.interpreted-text role="kbd"} | `Cmd + Ctrl + D`{.interpreted-text role="kbd"} | `editor/distraction_free_mode` |
| Next tab | `Ctrl + Tab`{.interpreted-text role="kbd"} | `Cmd + Tab`{.interpreted-text role="kbd"} | `editor/next_tab` |
| Previous tab | `Ctrl + Shift + Tab`{.interpreted-text role="kbd"} | `Cmd + Shift + Tab`{.interpreted-text role="kbd"} | `editor/prev_tab` |
| Filter Files | `Ctrl + Alt + P`{.interpreted-text role="kbd"} | `Opt + Cmd + P`{.interpreted-text role="kbd"} | `editor/filter_files` |
| Open Scene | `Ctrl + O`{.interpreted-text role="kbd"} | `Cmd + O`{.interpreted-text role="kbd"} | `editor/open_scene` |
| Close Scene | `Ctrl + Shift + W`{.interpreted-text role="kbd"} | `Cmd + Shift + W`{.interpreted-text role="kbd"} | `editor/close_scene` |
| Reopen Closed Scene | `Ctrl + Shift + T`{.interpreted-text role="kbd"} | `Cmd + Shift + T`{.interpreted-text role="kbd"} | `editor/reopen_closed_scene` |
| Save Scene | `Ctrl + S`{.interpreted-text role="kbd"} | `Cmd + S`{.interpreted-text role="kbd"} | `editor/save_scene` |
| Save Scene As | `Ctrl + Shift + S`{.interpreted-text role="kbd"} | `Cmd + Shift + S`{.interpreted-text role="kbd"} | `editor/save_scene_as` |
| Save All Scenes | `Ctrl + Shift + Alt + S`{.interpreted-text role="kbd"} | `Cmd + Shift + Opt + S`{.interpreted-text role="kbd"} | `editor/save_all_scenes` |
| Quick Open | `Shift + Alt + O`{.interpreted-text role="kbd"} | `Shift + Opt + O`{.interpreted-text role="kbd"} | `editor/quick_open` |
| Quick Open Scene | `Ctrl + Shift + O`{.interpreted-text role="kbd"} | `Cmd + Shift + O`{.interpreted-text role="kbd"} | `editor/quick_open_scene` |
| Quick Open Script | `Ctrl + Alt + O`{.interpreted-text role="kbd"} | `Opt + Cmd + O`{.interpreted-text role="kbd"} | `editor/quick_open_script` |
| Undo | `Ctrl + Z`{.interpreted-text role="kbd"} | `Cmd + Z`{.interpreted-text role="kbd"} | `editor/undo` |
| Redo | `Ctrl + Shift + Z`{.interpreted-text role="kbd"} | `Cmd + Shift + Z`{.interpreted-text role="kbd"} | `editor/redo` |
| Quit | `Ctrl + Q`{.interpreted-text role="kbd"} | `Cmd + Q`{.interpreted-text role="kbd"} | `editor/file_quit` |
| Quit to Project List | `Ctrl + Shift + Q`{.interpreted-text role="kbd"} | `Shift + Opt + Q`{.interpreted-text role="kbd"} | `editor/quit_to_project_list` |
| Take Screenshot | `Ctrl + F12`{.interpreted-text role="kbd"} | `Cmd + F12`{.interpreted-text role="kbd"} | `editor/take_screenshot` |
| Toggle Fullscreen | `Shift + F11`{.interpreted-text role="kbd"} | `Cmd + Ctrl + F`{.interpreted-text role="kbd"} | `editor/fullscreen_mode` |
| Play | `F5`{.interpreted-text role="kbd"} | `Cmd + B`{.interpreted-text role="kbd"} | `editor/play` |
| Pause Scene | `F7`{.interpreted-text role="kbd"} | `Cmd + Ctrl + Y`{.interpreted-text role="kbd"} | `editor/pause_scene` |
| Stop | `F8`{.interpreted-text role="kbd"} | `Cmd + .`{.interpreted-text role="kbd"} | `editor/stop` |
| Play Scene | `F6`{.interpreted-text role="kbd"} | `Cmd + R`{.interpreted-text role="kbd"} | `editor/play_scene` |
| Play Custom Scene | `Ctrl + Shift + F5`{.interpreted-text role="kbd"} | `Cmd + Shift + R`{.interpreted-text role="kbd"} | `editor/play_custom_scene` |
| Expand Bottom Panel | `Shift + F12`{.interpreted-text role="kbd"} | `Shift + F12`{.interpreted-text role="kbd"} | `editor/bottom_panel_expand` |
| Command Palette | `Ctrl + Shift + P`{.interpreted-text role="kbd"} | `Cmd + Shift + P`{.interpreted-text role="kbd"} | `editor/command_palette` |

## Bottom panels

Only bottom panels that are always available have a default shortcut
assigned. Others must be manually bound in the Editor Settings if
desired.

| Action name | Windows, Linux | macOS | Editor setting |
|----|----|----|----|
| Toggle Last Opened Panel | `Ctrl + J`{.interpreted-text role="kbd"} | `Ctrl + J`{.interpreted-text role="kbd"} | `editor/toggle_last_opened_bottom_panel` |
| Toggle Animation Bottom Panel | `Alt + N`{.interpreted-text role="kbd"} | `Alt + N`{.interpreted-text role="kbd"} | `bottom_panels/toggle_animation_bottom_panel` |
| Toggle Audio Bottom Panel | `Alt + A`{.interpreted-text role="kbd"} | `Alt + A`{.interpreted-text role="kbd"} | `bottom_panels/toggle_audio_bottom_panel` |
| Toggle Debugger Bottom Panel | `Alt + D`{.interpreted-text role="kbd"} | `Alt + D`{.interpreted-text role="kbd"} | `bottom_panels/toggle_debugger_bottom_panel` |
| Toggle FileSystem Bottom Panel | `Alt + F`{.interpreted-text role="kbd"} | `Alt + F`{.interpreted-text role="kbd"} | `bottom_panels/toggle_filesystem_bottom_panel` |
| Toggle Output Bottom Panel | `Alt + O`{.interpreted-text role="kbd"} | `Alt + O`{.interpreted-text role="kbd"} | `bottom_panels/toggle_output_bottom_panel` |
| Toggle Shader Editor Bottom Panel | `Alt + S`{.interpreted-text role="kbd"} | `Alt + S`{.interpreted-text role="kbd"} | `bottom_panels/toggle_shader_editor_bottom_panel` |

## 2D / CanvasItem editor {#d-canvasitem-editor}

| Action name | Windows, Linux | macOS | Editor setting |
|----|----|----|----|
| Zoom In | `Ctrl + =`{.interpreted-text role="kbd"} | `Cmd + =`{.interpreted-text role="kbd"} | `canvas_item_editor/zoom_plus` |
| Zoom Out | `Ctrl + -`{.interpreted-text role="kbd"} | `Cmd + -`{.interpreted-text role="kbd"} | `canvas_item_editor/zoom_minus` |
| Zoom Reset | `Ctrl + 0`{.interpreted-text role="kbd"} | `Cmd + 0`{.interpreted-text role="kbd"} | `canvas_item_editor/zoom_reset` |
| Pan View | `Space`{.interpreted-text role="kbd"} | `Space`{.interpreted-text role="kbd"} | `canvas_item_editor/pan_view` |
| Select Mode | `Q`{.interpreted-text role="kbd"} | `Q`{.interpreted-text role="kbd"} | `canvas_item_editor/select_mode` |
| Move Mode | `W`{.interpreted-text role="kbd"} | `W`{.interpreted-text role="kbd"} | `canvas_item_editor/move_mode` |
| Rotate Mode | `E`{.interpreted-text role="kbd"} | `E`{.interpreted-text role="kbd"} | `canvas_item_editor/rotate_mode` |
| Scale Mode | `S`{.interpreted-text role="kbd"} | `S`{.interpreted-text role="kbd"} | `canvas_item_editor/scale_mode` |
| Ruler Mode | `R`{.interpreted-text role="kbd"} | `R`{.interpreted-text role="kbd"} | `canvas_item_editor/ruler_mode` |
| Use Smart Snap | `Shift + S`{.interpreted-text role="kbd"} | `Shift + S`{.interpreted-text role="kbd"} | `canvas_item_editor/use_smart_snap` |
| Use Grid Snap | `Shift + G`{.interpreted-text role="kbd"} | `Shift + G`{.interpreted-text role="kbd"} | `canvas_item_editor/use_grid_snap` |
| Multiply grid step by 2 | `Num *`{.interpreted-text role="kbd"} | `Num *`{.interpreted-text role="kbd"} | `canvas_item_editor/multiply_grid_step` |
| Divide grid step by 2 | `Num /`{.interpreted-text role="kbd"} | `Num /`{.interpreted-text role="kbd"} | `canvas_item_editor/divide_grid_step` |
| Always Show Grid | `G`{.interpreted-text role="kbd"} | `G`{.interpreted-text role="kbd"} | `canvas_item_editor/show_grid` |
| Show Helpers | `H`{.interpreted-text role="kbd"} | `H`{.interpreted-text role="kbd"} | `canvas_item_editor/show_helpers` |
| Show Guides | `Y`{.interpreted-text role="kbd"} | `Y`{.interpreted-text role="kbd"} | `canvas_item_editor/show_guides` |
| Center Selection | `F`{.interpreted-text role="kbd"} | `F`{.interpreted-text role="kbd"} | `canvas_item_editor/center_selection` |
| Frame Selection | `Shift + F`{.interpreted-text role="kbd"} | `Shift + F`{.interpreted-text role="kbd"} | `canvas_item_editor/frame_selection` |
| Preview Canvas Scale | `Ctrl + Shift + P`{.interpreted-text role="kbd"} | `Cmd + Shift + P`{.interpreted-text role="kbd"} | `canvas_item_editor/preview_canvas_scale` |
| Insert Key | `Ins`{.interpreted-text role="kbd"} | `Ins`{.interpreted-text role="kbd"} | `canvas_item_editor/anim_insert_key` |
| Insert Key (Existing Tracks) | `Ctrl + Ins`{.interpreted-text role="kbd"} | `Cmd + Ins`{.interpreted-text role="kbd"} | `canvas_item_editor/anim_insert_key_existing_tracks` |
| Make Custom Bones from Nodes | `Ctrl + Shift + B`{.interpreted-text role="kbd"} | `Cmd + Shift + B`{.interpreted-text role="kbd"} | `canvas_item_editor/skeleton_make_bones` |
| Clear Pose | `Shift + K`{.interpreted-text role="kbd"} | `Shift + K`{.interpreted-text role="kbd"} | `canvas_item_editor/anim_clear_pose` |

## 3D / Spatial editor {#doc_default_key_mapping_shortcuts_spatial_editor}

| Action name | Windows, Linux | macOS | Editor setting |
|----|----|----|----|
| Toggle Freelook | `Shift + F`{.interpreted-text role="kbd"} | `Shift + F`{.interpreted-text role="kbd"} | `spatial_editor/freelook_toggle` |
| Freelook Left | `A`{.interpreted-text role="kbd"} | `A`{.interpreted-text role="kbd"} | `spatial_editor/freelook_left` |
| Freelook Right | `D`{.interpreted-text role="kbd"} | `D`{.interpreted-text role="kbd"} | `spatial_editor/freelook_right` |
| Freelook Forward | `W`{.interpreted-text role="kbd"} | `W`{.interpreted-text role="kbd"} | `spatial_editor/freelook_forward` |
| Freelook Backwards | `S`{.interpreted-text role="kbd"} | `S`{.interpreted-text role="kbd"} | `spatial_editor/freelook_backwards` |
| Freelook Up | `E`{.interpreted-text role="kbd"} | `E`{.interpreted-text role="kbd"} | `spatial_editor/freelook_up` |
| Freelook Down | `Q`{.interpreted-text role="kbd"} | `Q`{.interpreted-text role="kbd"} | `spatial_editor/freelook_down` |
| Freelook Speed Modifier | `Shift`{.interpreted-text role="kbd"} | `Shift`{.interpreted-text role="kbd"} | `spatial_editor/freelook_speed_modifier` |
| Freelook Slow Modifier | `Alt`{.interpreted-text role="kbd"} | `Opt`{.interpreted-text role="kbd"} | `spatial_editor/freelook_slow_modifier` |
| Select Mode | `Q`{.interpreted-text role="kbd"} | `Q`{.interpreted-text role="kbd"} | `spatial_editor/tool_select` |
| Move Mode | `W`{.interpreted-text role="kbd"} | `W`{.interpreted-text role="kbd"} | `spatial_editor/tool_move` |
| Rotate Mode | `E`{.interpreted-text role="kbd"} | `E`{.interpreted-text role="kbd"} | `spatial_editor/tool_rotate` |
| Scale Mode | `R`{.interpreted-text role="kbd"} | `R`{.interpreted-text role="kbd"} | `spatial_editor/tool_scale` |
| Use Local Space | `T`{.interpreted-text role="kbd"} | `T`{.interpreted-text role="kbd"} | `spatial_editor/local_coords` |
| Use Snap | `Y`{.interpreted-text role="kbd"} | `Y`{.interpreted-text role="kbd"} | `spatial_editor/snap` |
| Snap Object to Floor | `PgDown`{.interpreted-text role="kbd"} | `PgDown`{.interpreted-text role="kbd"} | `spatial_editor/snap_to_floor` |
| Top View | `Num 7`{.interpreted-text role="kbd"} | `Num 7`{.interpreted-text role="kbd"} | `spatial_editor/top_view` |
| Bottom View | `Alt + Num 7`{.interpreted-text role="kbd"} | `Opt + Num 7`{.interpreted-text role="kbd"} | `spatial_editor/bottom_view` |
| Front View | `Num 1`{.interpreted-text role="kbd"} | `Num 1`{.interpreted-text role="kbd"} | `spatial_editor/front_view` |
| Rear View | `Alt + Num 1`{.interpreted-text role="kbd"} | `Opt + Num 1`{.interpreted-text role="kbd"} | `spatial_editor/rear_view` |
| Right View | `Num 3`{.interpreted-text role="kbd"} | `Num 3`{.interpreted-text role="kbd"} | `spatial_editor/right_view` |
| Left View | `Alt + Num 3`{.interpreted-text role="kbd"} | `Opt + Num 3`{.interpreted-text role="kbd"} | `spatial_editor/left_view` |
| Switch Perspective/Orthogonal View | `Num 5`{.interpreted-text role="kbd"} | `Num 5`{.interpreted-text role="kbd"} | `spatial_editor/switch_perspective_orthogonal` |
| Insert Animation Key | `K`{.interpreted-text role="kbd"} | `K`{.interpreted-text role="kbd"} | `spatial_editor/insert_anim_key` |
| Focus Origin | `O`{.interpreted-text role="kbd"} | `O`{.interpreted-text role="kbd"} | `spatial_editor/focus_origin` |
| Focus Selection | `F`{.interpreted-text role="kbd"} | `F`{.interpreted-text role="kbd"} | `spatial_editor/focus_selection` |
| Align Transform with View | `Ctrl + Alt + M`{.interpreted-text role="kbd"} | `Opt + Cmd + M`{.interpreted-text role="kbd"} | `spatial_editor/align_transform_with_view` |
| Align Rotation with View | `Ctrl + Alt + F`{.interpreted-text role="kbd"} | `Opt + Cmd + F`{.interpreted-text role="kbd"} | `spatial_editor/align_rotation_with_view` |
| 1 Viewport | `Ctrl + 1`{.interpreted-text role="kbd"} | `Cmd + 1`{.interpreted-text role="kbd"} | `spatial_editor/1_viewport` |
| 2 Viewports | `Ctrl + 2`{.interpreted-text role="kbd"} | `Cmd + 2`{.interpreted-text role="kbd"} | `spatial_editor/2_viewports` |
| 2 Viewports (Alt) | `Ctrl + Alt + 2`{.interpreted-text role="kbd"} | `Opt + Cmd + 2`{.interpreted-text role="kbd"} | `spatial_editor/2_viewports_alt` |
| 3 Viewports | `Ctrl + 3`{.interpreted-text role="kbd"} | `Cmd + 3`{.interpreted-text role="kbd"} | `spatial_editor/3_viewports` |
| 3 Viewports (Alt) | `Ctrl + Alt + 3`{.interpreted-text role="kbd"} | `Opt + Cmd + 3`{.interpreted-text role="kbd"} | `spatial_editor/3_viewports_alt` |
| 4 Viewports | `Ctrl + 4`{.interpreted-text role="kbd"} | `Cmd + 4`{.interpreted-text role="kbd"} | `spatial_editor/4_viewports` |

## Text editor

| Action name | Windows, Linux | macOS | Editor setting |
|----|----|----|----|
| Cut | `Ctrl + X`{.interpreted-text role="kbd"} | `Cmd + X`{.interpreted-text role="kbd"} | `script_text_editor/cut` |
| Copy | `Ctrl + C`{.interpreted-text role="kbd"} | `Cmd + C`{.interpreted-text role="kbd"} | `script_text_editor/copy` |
| Paste | `Ctrl + V`{.interpreted-text role="kbd"} | `Cmd + V`{.interpreted-text role="kbd"} | `script_text_editor/paste` |
| Select All | `Ctrl + A`{.interpreted-text role="kbd"} | `Cmd + A`{.interpreted-text role="kbd"} | `script_text_editor/select_all` |
| Find | `Ctrl + F`{.interpreted-text role="kbd"} | `Cmd + F`{.interpreted-text role="kbd"} | `script_text_editor/find` |
| Find Next | `F3`{.interpreted-text role="kbd"} | `Cmd + G`{.interpreted-text role="kbd"} | `script_text_editor/find_next` |
| Find Previous | `Shift + F3`{.interpreted-text role="kbd"} | `Cmd + Shift + G`{.interpreted-text role="kbd"} | `script_text_editor/find_previous` |
| Find in Files | `Ctrl + Shift + F`{.interpreted-text role="kbd"} | `Cmd + Shift + F`{.interpreted-text role="kbd"} | `script_text_editor/find_in_files` |
| Replace | `Ctrl + R`{.interpreted-text role="kbd"} | `Opt + Cmd + F`{.interpreted-text role="kbd"} | `script_text_editor/replace` |
| Replace in Files | `Ctrl + Shift + R`{.interpreted-text role="kbd"} | `Cmd + Shift + R`{.interpreted-text role="kbd"} | `script_text_editor/replace_in_files` |
| Undo | `Ctrl + Z`{.interpreted-text role="kbd"} | `Cmd + Z`{.interpreted-text role="kbd"} | `script_text_editor/undo` |
| Redo | `Ctrl + Y`{.interpreted-text role="kbd"} | `Cmd + Y`{.interpreted-text role="kbd"} | `script_text_editor/redo` |
| Move Up | `Alt + Up Arrow`{.interpreted-text role="kbd"} | `Opt + Up Arrow`{.interpreted-text role="kbd"} | `script_text_editor/move_up` |
| Move Down | `Alt + Down Arrow`{.interpreted-text role="kbd"} | `Opt + Down Arrow`{.interpreted-text role="kbd"} | `script_text_editor/move_down` |
| Delete Line | `Ctrl + Shift + K`{.interpreted-text role="kbd"} | `Cmd + Shift + K`{.interpreted-text role="kbd"} | `script_text_editor/delete_line` |
| Toggle Comment | `Ctrl + K`{.interpreted-text role="kbd"} | `Cmd + K`{.interpreted-text role="kbd"} | `script_text_editor/toggle_comment` |
| Fold/Unfold Line | `Alt + F`{.interpreted-text role="kbd"} | `Ctrl + Cmd + F`{.interpreted-text role="kbd"} | `script_text_editor/toggle_fold_line` |
| Duplicate Lines | `Ctrl + Alt + Down Arrow`{.interpreted-text role="kbd"} | `Cmd + Shift + Down Arrow`{.interpreted-text role="kbd"} | `script_text_editor/duplicate_lines` |
| Duplicate Selection | `Ctrl + Shift + D`{.interpreted-text role="kbd"} | `Cmd + Shift + C`{.interpreted-text role="kbd"} | `script_text_editor/duplicate_selection` |
| Complete Symbol | `Ctrl + Space`{.interpreted-text role="kbd"} | `Ctrl + Space`{.interpreted-text role="kbd"} | `script_text_editor/complete_symbol` |
| Evaluate Selection | `Ctrl + Shift + E`{.interpreted-text role="kbd"} | `Cmd + Shift + E`{.interpreted-text role="kbd"} | `script_text_editor/evaluate_selection` |
| Trim Trailing Whitespace | `Ctrl + Alt + T`{.interpreted-text role="kbd"} | `Opt + Cmd + T`{.interpreted-text role="kbd"} | `script_text_editor/trim_trailing_whitespace` |
| Uppercase | `Shift + F4`{.interpreted-text role="kbd"} | `Shift + F4`{.interpreted-text role="kbd"} | `script_text_editor/convert_to_uppercase` |
| Lowercase | `Shift + F5`{.interpreted-text role="kbd"} | `Shift + F5`{.interpreted-text role="kbd"} | `script_text_editor/convert_to_lowercase` |
| Capitalize | `Shift + F6`{.interpreted-text role="kbd"} | `Shift + F6`{.interpreted-text role="kbd"} | `script_text_editor/capitalize` |
| Convert Indent to Spaces | `Ctrl + Shift + Y`{.interpreted-text role="kbd"} | `Cmd + Shift + Y`{.interpreted-text role="kbd"} | `script_text_editor/convert_indent_to_spaces` |
| Convert Indent to Tabs | `Ctrl + Shift + I`{.interpreted-text role="kbd"} | `Cmd + Shift + I`{.interpreted-text role="kbd"} | `script_text_editor/convert_indent_to_tabs` |
| Auto Indent | `Ctrl + I`{.interpreted-text role="kbd"} | `Cmd + I`{.interpreted-text role="kbd"} | `script_text_editor/auto_indent` |
| Toggle Bookmark | `Ctrl + Alt + B`{.interpreted-text role="kbd"} | `Opt + Cmd + B`{.interpreted-text role="kbd"} | `script_text_editor/toggle_bookmark` |
| Go to Next Bookmark | `Ctrl + B`{.interpreted-text role="kbd"} | `Cmd + B`{.interpreted-text role="kbd"} | `script_text_editor/goto_next_bookmark` |
| Go to Previous Bookmark | `Ctrl + Shift + B`{.interpreted-text role="kbd"} | `Cmd + Shift + B`{.interpreted-text role="kbd"} | `script_text_editor/goto_previous_bookmark` |
| Go to Function | `Ctrl + Alt + F`{.interpreted-text role="kbd"} | `Ctrl + Cmd + J`{.interpreted-text role="kbd"} | `script_text_editor/goto_function` |
| Go to Line | `Ctrl + L`{.interpreted-text role="kbd"} | `Cmd + L`{.interpreted-text role="kbd"} | `script_text_editor/goto_line` |
| Toggle Breakpoint | `F9`{.interpreted-text role="kbd"} | `Cmd + Shift + B`{.interpreted-text role="kbd"} | `script_text_editor/toggle_breakpoint` |
| Remove All Breakpoints | `Ctrl + Shift + F9`{.interpreted-text role="kbd"} | `Cmd + Shift + F9`{.interpreted-text role="kbd"} | `script_text_editor/remove_all_breakpoints` |
| Go to Next Breakpoint | `Ctrl + .`{.interpreted-text role="kbd"} | `Cmd + .`{.interpreted-text role="kbd"} | `script_text_editor/goto_next_breakpoint` |
| Go to Previous Breakpoint | `Ctrl + ,`{.interpreted-text role="kbd"} | `Cmd + ,`{.interpreted-text role="kbd"} | `script_text_editor/goto_previous_breakpoint` |
| Contextual Help | `Alt + F1`{.interpreted-text role="kbd"} | `Opt + Shift + Space`{.interpreted-text role="kbd"} | `script_text_editor/contextual_help` |

## Script editor

| Action name | Windows, Linux | macOS | Editor setting |
|----|----|----|----|
| Find | `Ctrl + F`{.interpreted-text role="kbd"} | `Cmd + F`{.interpreted-text role="kbd"} | `script_editor/find` |
| Find Next | `F3`{.interpreted-text role="kbd"} | `F3`{.interpreted-text role="kbd"} | `script_editor/find_next` |
| Find Previous | `Shift + F3`{.interpreted-text role="kbd"} | `Shift + F3`{.interpreted-text role="kbd"} | `script_editor/find_previous` |
| Find in Files | `Ctrl + Shift + F`{.interpreted-text role="kbd"} | `Cmd + Shift + F`{.interpreted-text role="kbd"} | `script_editor/find_in_files` |
| Move Up | `Shift + Alt + Up Arrow`{.interpreted-text role="kbd"} | `Shift + Opt + Up Arrow`{.interpreted-text role="kbd"} | `script_editor/window_move_up` |
| Move Down | `Shift + Alt + Down Arrow`{.interpreted-text role="kbd"} | `Shift + Opt + Down Arrow`{.interpreted-text role="kbd"} | `script_editor/window_move_down` |
| Next Script | `Ctrl + Shift + .`{.interpreted-text role="kbd"} | `Cmd + Shift + .`{.interpreted-text role="kbd"} | `script_editor/next_script` |
| Previous Script | `Ctrl + Shift + ,`{.interpreted-text role="kbd"} | `Cmd + Shift + ,`{.interpreted-text role="kbd"} | `script_editor/prev_script` |
| Reopen Closed Script | `Ctrl + Shift + T`{.interpreted-text role="kbd"} | `Cmd + Shift + T`{.interpreted-text role="kbd"} | `script_editor/reopen_closed_script` |
| Save | `Ctrl + Alt + S`{.interpreted-text role="kbd"} | `Opt + Cmd + S`{.interpreted-text role="kbd"} | `script_editor/save` |
| Save All | `Ctrl + Shift + Alt + S`{.interpreted-text role="kbd"} | `Cmd + Shift + Opt + S`{.interpreted-text role="kbd"} | `script_editor/save_all` |
| Soft Reload Script | `Ctrl + Shift + R`{.interpreted-text role="kbd"} | `Cmd + Shift + R`{.interpreted-text role="kbd"} | `script_editor/reload_script_soft` |
| History Previous | `Alt + Left Arrow`{.interpreted-text role="kbd"} | `Opt + Left Arrow`{.interpreted-text role="kbd"} | `script_editor/history_previous` |
| History Next | `Alt + Right Arrow`{.interpreted-text role="kbd"} | `Opt + Right Arrow`{.interpreted-text role="kbd"} | `script_editor/history_next` |
| Close | `Ctrl + W`{.interpreted-text role="kbd"} | `Cmd + W`{.interpreted-text role="kbd"} | `script_editor/close_file` |
| Run | `Ctrl + Shift + X`{.interpreted-text role="kbd"} | `Cmd + Shift + X`{.interpreted-text role="kbd"} | `script_editor/run_file` |
| Toggle Scripts Panel | `Ctrl + \\`{.interpreted-text role="kbd"} | `Cmd + \\`{.interpreted-text role="kbd"} | `script_editor/toggle_scripts_panel` |
| Zoom In | `Ctrl + =`{.interpreted-text role="kbd"} | `Cmd + =`{.interpreted-text role="kbd"} | `script_editor/zoom_in` |
| Zoom Out | `Ctrl + -`{.interpreted-text role="kbd"} | `Cmd + -`{.interpreted-text role="kbd"} | `script_editor/zoom_out` |
| Reset Zoom | `Ctrl + 0`{.interpreted-text role="kbd"} | `Cmd + 0`{.interpreted-text role="kbd"} | `script_editor/reset_zoom` |

## Editor output

| Action name | Windows, Linux | macOS | Editor setting |
|----|----|----|----|
| Copy Selection | `Ctrl + C`{.interpreted-text role="kbd"} | `Cmd + C`{.interpreted-text role="kbd"} | `editor/copy_output` |
| Clear Output | `Ctrl + Shift + K`{.interpreted-text role="kbd"} | `Cmd + Shift + K`{.interpreted-text role="kbd"} | `editor/clear_output` |

## Debugger

| Action name | Windows, Linux | macOS | Editor setting |
|----|----|----|----|
| Step Into | `F11`{.interpreted-text role="kbd"} | `F11`{.interpreted-text role="kbd"} | `debugger/step_into` |
| Step Over | `F10`{.interpreted-text role="kbd"} | `F10`{.interpreted-text role="kbd"} | `debugger/step_over` |
| Continue | `F12`{.interpreted-text role="kbd"} | `F12`{.interpreted-text role="kbd"} | `debugger/continue` |

## File dialog

| Action name | Windows, Linux | macOS | Editor setting |
|----|----|----|----|
| Go Back | `Alt + Left Arrow`{.interpreted-text role="kbd"} | `Opt + Left Arrow`{.interpreted-text role="kbd"} | `file_dialog/go_back` |
| Go Forward | `Alt + Right Arrow`{.interpreted-text role="kbd"} | `Opt + Right Arrow`{.interpreted-text role="kbd"} | `file_dialog/go_forward` |
| Go Up | `Alt + Up Arrow`{.interpreted-text role="kbd"} | `Opt + Up Arrow`{.interpreted-text role="kbd"} | `file_dialog/go_up` |
| Refresh | `F5`{.interpreted-text role="kbd"} | `F5`{.interpreted-text role="kbd"} | `file_dialog/refresh` |
| Toggle Hidden Files | `Ctrl + H`{.interpreted-text role="kbd"} | `Cmd + H`{.interpreted-text role="kbd"} | `file_dialog/toggle_hidden_files` |
| Toggle Favorite | `Alt + F`{.interpreted-text role="kbd"} | `Opt + F`{.interpreted-text role="kbd"} | `file_dialog/toggle_favorite` |
| Toggle Mode | `Alt + V`{.interpreted-text role="kbd"} | `Opt + V`{.interpreted-text role="kbd"} | `file_dialog/toggle_mode` |
| Create Folder | `Ctrl + N`{.interpreted-text role="kbd"} | `Cmd + N`{.interpreted-text role="kbd"} | `file_dialog/create_folder` |
| Delete | `Del`{.interpreted-text role="kbd"} | `Cmd + BkSp`{.interpreted-text role="kbd"} | `file_dialog/delete` |
| Focus Path | `Ctrl + L`{.interpreted-text role="kbd"} | `Cmd + Shift + G`{.interpreted-text role="kbd"} | `file_dialog/focus_path` |
| Move Favorite Up | `Ctrl + Up Arrow`{.interpreted-text role="kbd"} | `Cmd + Up Arrow`{.interpreted-text role="kbd"} | `file_dialog/move_favorite_up` |
| Move Favorite Down | `Ctrl + Down Arrow`{.interpreted-text role="kbd"} | `Cmd + Down Arrow`{.interpreted-text role="kbd"} | `file_dialog/move_favorite_down` |

## FileSystem dock

| Action name | Windows, Linux | macOS | Editor setting |
|----|----|----|----|
| Copy Path | `Ctrl + C`{.interpreted-text role="kbd"} | `Cmd + C`{.interpreted-text role="kbd"} | `filesystem_dock/copy_path` |
| Duplicate | `Ctrl + D`{.interpreted-text role="kbd"} | `Cmd + D`{.interpreted-text role="kbd"} | `filesystem_dock/duplicate` |
| Delete | `Del`{.interpreted-text role="kbd"} | `Cmd + BkSp`{.interpreted-text role="kbd"} | `filesystem_dock/delete` |

## Scene tree dock

| Action name | Windows, Linux | macOS | Editor setting |
|----|----|----|----|
| Add Child Node | `Ctrl + A`{.interpreted-text role="kbd"} | `Cmd + A`{.interpreted-text role="kbd"} | `scene_tree/add_child_node` |
| Batch Rename | `Ctrl + F2`{.interpreted-text role="kbd"} | `Cmd + F2`{.interpreted-text role="kbd"} | `scene_tree/batch_rename` |
| Copy Node Path | `Ctrl + Shift + C`{.interpreted-text role="kbd"} | `Cmd + Shift +  C`{.interpreted-text role="kbd"} | `scene_tree/copy_node_path` |
| Delete | `Del`{.interpreted-text role="kbd"} | `Cmd + BkSp`{.interpreted-text role="kbd"} | `scene_tree/delete` |
| Force Delete | `Shift + Del`{.interpreted-text role="kbd"} | `Shift + Del`{.interpreted-text role="kbd"} | `scene_tree/delete_no_confirm` |
| Duplicate | `Ctrl + D`{.interpreted-text role="kbd"} | `Cmd + D`{.interpreted-text role="kbd"} | `scene_tree/duplicate` |
| Move Up | `Ctrl + Up Arrow`{.interpreted-text role="kbd"} | `Cmd + Up Arrow`{.interpreted-text role="kbd"} | `scene_tree/move_up` |
| Move Down | `Ctrl + Down Arrow`{.interpreted-text role="kbd"} | `Cmd + Down Arrow`{.interpreted-text role="kbd"} | `scene_tree/move_down` |

## Animation track editor

| Action name | Windows, Linux | macOS | Editor setting |
|----|----|----|----|
| Duplicate Selection | `Ctrl + D`{.interpreted-text role="kbd"} | `Cmd + D`{.interpreted-text role="kbd"} | `animation_editor/duplicate_selection` |
| Duplicate Transposed | `Ctrl + Shift + D`{.interpreted-text role="kbd"} | `Cmd + Shift + D`{.interpreted-text role="kbd"} | `animation_editor/duplicate_selection_transposed` |
| Delete Selection | `Del`{.interpreted-text role="kbd"} | `Cmd + BkSp`{.interpreted-text role="kbd"} | `animation_editor/delete_selection` |
| Go to Next Step | `Ctrl + Right Arrow`{.interpreted-text role="kbd"} | `Cmd + Right Arrow`{.interpreted-text role="kbd"} | `animation_editor/goto_next_step` |
| Go to Previous Step | `Ctrl + Left Arrow`{.interpreted-text role="kbd"} | `Cmd + Left Arrow`{.interpreted-text role="kbd"} | `animation_editor/goto_prev_step` |

## TileMap editor

| Action name | Windows, Linux | macOS | Editor setting |
|----|----|----|----|
| Select | `S`{.interpreted-text role="kbd"} | `S`{.interpreted-text role="kbd"} | `tiles_editor/selection_tool` |
| Cut Selection | `Ctrl + X`{.interpreted-text role="kbd"} | `Cmd + X`{.interpreted-text role="kbd"} | `tiles_editor/cut` |
| Copy Selection | `Ctrl + C`{.interpreted-text role="kbd"} | `Cmd + C`{.interpreted-text role="kbd"} | `tiles_editor/copy` |
| Paste Selection | `Ctrl + V`{.interpreted-text role="kbd"} | `Cmd + V`{.interpreted-text role="kbd"} | `tiles_editor/paste` |
| Delete Selection | `Del`{.interpreted-text role="kbd"} | `Cmd + BkSp`{.interpreted-text role="kbd"} | `tiles_editor/delete` |
| Cancel | `Esc`{.interpreted-text role="kbd"} | `Esc`{.interpreted-text role="kbd"} | `tiles_editor/cancel` |
| Paint | `D`{.interpreted-text role="kbd"} | `D`{.interpreted-text role="kbd"} | `tiles_editor/paint_tool` |
| Line | `L`{.interpreted-text role="kbd"} | `L`{.interpreted-text role="kbd"} | `tiles_editor/line_tool` |
| Rect | `R`{.interpreted-text role="kbd"} | `R`{.interpreted-text role="kbd"} | `tiles_editor/rect_tool` |
| Bucket | `B`{.interpreted-text role="kbd"} | `B`{.interpreted-text role="kbd"} | `tiles_editor/bucket_tool` |
| Picker | `P`{.interpreted-text role="kbd"} | `P`{.interpreted-text role="kbd"} | `tiles_editor/picker` |
| Eraser | `E`{.interpreted-text role="kbd"} | `E`{.interpreted-text role="kbd"} | `tiles_editor/eraser` |
| Flip Horizontally | `C`{.interpreted-text role="kbd"} | `C`{.interpreted-text role="kbd"} | `tiles_editor/flip_tile_horizontal` |
| Flip Vertically | `V`{.interpreted-text role="kbd"} | `V`{.interpreted-text role="kbd"} | `tiles_editor/flip_tile_vertical` |
| Rotate Left | `Z`{.interpreted-text role="kbd"} | `Z`{.interpreted-text role="kbd"} | `tiles_editor/rotate_tile_left` |
| Rotate Right | `X`{.interpreted-text role="kbd"} | `X`{.interpreted-text role="kbd"} | `tiles_editor/rotate_tile_right` |

## TileSet Editor

| Action name | Windows, Linux | macOS | Editor setting |
|----|----|----|----|
| Next Coordinate | `PgDown`{.interpreted-text role="kbd"} | `PgDown`{.interpreted-text role="kbd"} | `tileset_editor/next_shape` |
| Previous Coordinate | `PgUp`{.interpreted-text role="kbd"} | `PgUp`{.interpreted-text role="kbd"} | `tileset_editor/previous_shape` |
| Region Mode | `1`{.interpreted-text role="kbd"} | `1`{.interpreted-text role="kbd"} | `tileset_editor/editmode_region` |
| Collision Mode | `2`{.interpreted-text role="kbd"} | `2`{.interpreted-text role="kbd"} | `tileset_editor/editmode_collision` |
| Occlusion Mode | `3`{.interpreted-text role="kbd"} | `3`{.interpreted-text role="kbd"} | `tileset_editor/editmode_occlusion` |
| Navigation Mode | `4`{.interpreted-text role="kbd"} | `4`{.interpreted-text role="kbd"} | `tileset_editor/editmode_navigation` |
| Bitmask Mode | `5`{.interpreted-text role="kbd"} | `5`{.interpreted-text role="kbd"} | `tileset_editor/editmode_bitmask` |
| Priority Mode | `6`{.interpreted-text role="kbd"} | `6`{.interpreted-text role="kbd"} | `tileset_editor/editmode_priority` |
| Icon Mode | `7`{.interpreted-text role="kbd"} | `7`{.interpreted-text role="kbd"} | `tileset_editor/editmode_icon` |
| Z Index Mode | `8`{.interpreted-text role="kbd"} | `8`{.interpreted-text role="kbd"} | `tileset_editor/editmode_z_index` |

## Project manager

| Action name | Windows, Linux | macOS | Editor setting |
|----|----|----|----|
| New Project | `Ctrl + N`{.interpreted-text role="kbd"} | `Cmd + N`{.interpreted-text role="kbd"} | `project_manager/new_project` |
| Import Project | `Ctrl + I`{.interpreted-text role="kbd"} | `Cmd + I`{.interpreted-text role="kbd"} | `project_manager/import_project` |
| Scan for Projects | `Ctrl + S`{.interpreted-text role="kbd"} | `Cmd + S`{.interpreted-text role="kbd"} | `project_manager/scan_projects` |
| Edit Project | `Ctrl + E`{.interpreted-text role="kbd"} | `Cmd + E`{.interpreted-text role="kbd"} | `project_manager/edit_project` |
| Run Project | `Ctrl + R`{.interpreted-text role="kbd"} | `Cmd + R`{.interpreted-text role="kbd"} | `project_manager/run_project` |
| Rename Project | `F2`{.interpreted-text role="kbd"} | `Enter`{.interpreted-text role="kbd"} | `project_manager/rename_project` |
| Remove Project | `Delete`{.interpreted-text role="kbd"} | `Cmd + BkSp`{.interpreted-text role="kbd"} | `project_manager/remove_project` |
