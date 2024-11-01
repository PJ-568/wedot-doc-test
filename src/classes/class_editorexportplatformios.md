github_url

:   hide

# EditorExportPlatformIOS {#class_EditorExportPlatformIOS}

**Inherits:**
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Exporter for iOS.

::: {.rst-class}
classref-introduction-group
:::

## Tutorials

- `Exporting for iOS <../tutorials/export/exporting_for_ios>`{.interpreted-text
  role="doc"}
- `iOS plugins documentation index <../tutorials/platform/ios/index>`{.interpreted-text
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

## Property Descriptions

:::: {#class_EditorExportPlatformIOS_property_application/additional_plist_content}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/additional_plist_content**
`🔗<class_EditorExportPlatformIOS_property_application/additional_plist_content>`{.interpreted-text
role="ref"}

Additional data added to the root `<dict>` section of the
[Info.plist](https://developer.apple.com/documentation/bundleresources/information_property_list)
file. The value should be an XML section with pairs of key-value
elements, e.g.:

``` text
<key>key_name</key>
<string>value</string>
```

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/app_store_team_id}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/app_store_team_id**
`🔗<class_EditorExportPlatformIOS_property_application/app_store_team_id>`{.interpreted-text
role="ref"}

Apple Team ID, unique 10-character string. To locate your Team ID check
\"Membership details\" section in your Apple developer account
dashboard, or \"Organizational Unit\" of your code signing certificate.
See [Locate your Team
ID](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/bundle_identifier}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/bundle_identifier**
`🔗<class_EditorExportPlatformIOS_property_application/bundle_identifier>`{.interpreted-text
role="ref"}

Unique application identifier in a reverse-DNS format, can only contain
alphanumeric characters (`A-Z`, `a-z`, and `0-9`), hyphens (`-`), and
periods (`.`).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/code_sign_identity_debug}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/code_sign_identity_debug**
`🔗<class_EditorExportPlatformIOS_property_application/code_sign_identity_debug>`{.interpreted-text
role="ref"}

The \"Full Name\", \"Common Name\" or SHA-1 hash of the signing identity
used for debug export.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/code_sign_identity_release}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/code_sign_identity_release**
`🔗<class_EditorExportPlatformIOS_property_application/code_sign_identity_release>`{.interpreted-text
role="ref"}

The \"Full Name\", \"Common Name\" or SHA-1 hash of the signing identity
used for release export.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/delete_old_export_files_unconditionally}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/delete_old_export_files_unconditionally**
`🔗<class_EditorExportPlatformIOS_property_application/delete_old_export_files_unconditionally>`{.interpreted-text
role="ref"}

If `true`, existing \"project name\" and \"project name.xcodeproj\" in
the export destination directory will be unconditionally deleted during
export.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/export_method_debug}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**application/export_method_debug**
`🔗<class_EditorExportPlatformIOS_property_application/export_method_debug>`{.interpreted-text
role="ref"}

Application distribution target (debug export).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/export_method_release}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**application/export_method_release**
`🔗<class_EditorExportPlatformIOS_property_application/export_method_release>`{.interpreted-text
role="ref"}

Application distribution target (release export).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/export_project_only}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/export_project_only**
`🔗<class_EditorExportPlatformIOS_property_application/export_project_only>`{.interpreted-text
role="ref"}

If `true`, exports iOS project files without building an XCArchive or
`.ipa` file. If `false`, exports iOS project files and builds an
XCArchive and `.ipa` file at the same time. When combining Godot with
Fastlane or other build pipelines, you may want to set this to `true`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/generate_simulator_library_if_missing}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/generate_simulator_library_if_missing**
`🔗<class_EditorExportPlatformIOS_property_application/generate_simulator_library_if_missing>`{.interpreted-text
role="ref"}

If `true`, and ARM64 simulator library is missing from the export
template, it is automatically generated from ARM64 device library.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/icon_interpolation}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**application/icon_interpolation**
`🔗<class_EditorExportPlatformIOS_property_application/icon_interpolation>`{.interpreted-text
role="ref"}

Interpolation method used to resize application icon.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/min_ios_version}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/min_ios_version**
`🔗<class_EditorExportPlatformIOS_property_application/min_ios_version>`{.interpreted-text
role="ref"}

Minimum version of iOS required for this application to run in the
`major.minor.patch` or `major.minor` format, can only contain numeric
characters (`0-9`) and periods (`.`).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/provisioning_profile_uuid_debug}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/provisioning_profile_uuid_debug**
`🔗<class_EditorExportPlatformIOS_property_application/provisioning_profile_uuid_debug>`{.interpreted-text
role="ref"}

UUID of the provisioning profile. If left empty, Xcode will download or
create a provisioning profile automatically. See [Edit, download, or
delete provisioning
profiles](https://developer.apple.com/help/account/manage-profiles/edit-download-or-delete-profiles).

Can be overridden with the environment variable
`GODOT_IOS_PROVISIONING_PROFILE_UUID_DEBUG`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/provisioning_profile_uuid_release}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/provisioning_profile_uuid_release**
`🔗<class_EditorExportPlatformIOS_property_application/provisioning_profile_uuid_release>`{.interpreted-text
role="ref"}

UUID of the provisioning profile. If left empty, Xcode will download or
create a provisioning profile automatically. See [Edit, download, or
delete provisioning
profiles](https://developer.apple.com/help/account/manage-profiles/edit-download-or-delete-profiles).

Can be overridden with the environment variable
`GODOT_IOS_PROVISIONING_PROFILE_UUID_RELEASE`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/short_version}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/short_version**
`🔗<class_EditorExportPlatformIOS_property_application/short_version>`{.interpreted-text
role="ref"}

Application version visible to the user, can only contain numeric
characters (`0-9`) and periods (`.`). Falls back to
`ProjectSettings.application/config/version<class_ProjectSettings_property_application/config/version>`{.interpreted-text
role="ref"} if left empty.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/signature}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/signature**
`🔗<class_EditorExportPlatformIOS_property_application/signature>`{.interpreted-text
role="ref"}

A four-character creator code that is specific to the bundle. Optional.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/targeted_device_family}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**application/targeted_device_family**
`🔗<class_EditorExportPlatformIOS_property_application/targeted_device_family>`{.interpreted-text
role="ref"}

Supported device family.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_application/version}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/version**
`🔗<class_EditorExportPlatformIOS_property_application/version>`{.interpreted-text
role="ref"}

Machine-readable application version, in the `major.minor.patch` format,
can only contain numeric characters (`0-9`) and periods (`.`). This must
be incremented on every new release pushed to the App Store.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_architectures/arm64}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **architectures/arm64**
`🔗<class_EditorExportPlatformIOS_property_architectures/arm64>`{.interpreted-text
role="ref"}

If `true`, `arm64` binaries are included into exported project.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_capabilities/access_wifi}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**capabilities/access_wifi**
`🔗<class_EditorExportPlatformIOS_property_capabilities/access_wifi>`{.interpreted-text
role="ref"}

If `true`, networking features related to Wi-Fi access are enabled. See
[Required Device
Capabilities](https://developer.apple.com/support/required-device-capabilities/).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_capabilities/performance_a12}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**capabilities/performance_a12**
`🔗<class_EditorExportPlatformIOS_property_capabilities/performance_a12>`{.interpreted-text
role="ref"}

Requires the graphics performance and features of the A12 Bionic and
later chips (devices supporting all Vulkan renderer features).

Enabling this option limits supported devices to: iPhone XS, iPhone XR,
iPad Mini (5th gen.), iPad Air (3rd gen.), iPad (8th gen) and newer.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_capabilities/performance_gaming_tier}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**capabilities/performance_gaming_tier**
`🔗<class_EditorExportPlatformIOS_property_capabilities/performance_gaming_tier>`{.interpreted-text
role="ref"}

Requires the graphics performance and features of the A17 Pro and later
chips.

Enabling this option limits supported devices to: iPhone 15 Pro and
newer.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_capabilities/push_notifications}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**capabilities/push_notifications**
`🔗<class_EditorExportPlatformIOS_property_capabilities/push_notifications>`{.interpreted-text
role="ref"}

If `true`, push notifications are enabled. See [Required Device
Capabilities](https://developer.apple.com/support/required-device-capabilities/).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_custom_template/debug}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**custom_template/debug**
`🔗<class_EditorExportPlatformIOS_property_custom_template/debug>`{.interpreted-text
role="ref"}

Path to the custom export template. If left empty, default template is
used.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_custom_template/release}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**custom_template/release**
`🔗<class_EditorExportPlatformIOS_property_custom_template/release>`{.interpreted-text
role="ref"}

Path to the custom export template. If left empty, default template is
used.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/app_store_1024x1024}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/app_store_1024x1024**
`🔗<class_EditorExportPlatformIOS_property_icons/app_store_1024x1024>`{.interpreted-text
role="ref"}

App Store application icon file. If left empty, it will fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/app_store_1024x1024_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/app_store_1024x1024_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/app_store_1024x1024_dark>`{.interpreted-text
role="ref"}

App Store application icon file, dark version. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/app_store_1024x1024_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/app_store_1024x1024_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/app_store_1024x1024_tinted>`{.interpreted-text
role="ref"}

App Store application icon file, tinted version. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/icon_1024x1024}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/icon_1024x1024**
`🔗<class_EditorExportPlatformIOS_property_icons/icon_1024x1024>`{.interpreted-text
role="ref"}

Base application icon used to generate other icons. If left empty, it
will fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/icon_1024x1024_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/icon_1024x1024_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/icon_1024x1024_dark>`{.interpreted-text
role="ref"}

Base application icon used to generate other icons, dark version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/icon_1024x1024_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/icon_1024x1024_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/icon_1024x1024_tinted>`{.interpreted-text
role="ref"}

Base application icon used to generate other icons, tinted version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/ios_128x128}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/ios_128x128**
`🔗<class_EditorExportPlatformIOS_property_icons/ios_128x128>`{.interpreted-text
role="ref"}

iOS application 64x64 icon file (2x DPI). If left empty, it will
fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/ios_128x128_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/ios_128x128_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/ios_128x128_dark>`{.interpreted-text
role="ref"}

iOS application 64x64 icon file (2x DPI), dark version. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/ios_128x128_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/ios_128x128_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/ios_128x128_tinted>`{.interpreted-text
role="ref"}

iOS application 64x64 icon file (2x DPI), tinted version. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/ios_136x136}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/ios_136x136**
`🔗<class_EditorExportPlatformIOS_property_icons/ios_136x136>`{.interpreted-text
role="ref"}

iOS application 68x68 icon file (2x DPI). If left empty, it will
fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/ios_136x136_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/ios_136x136_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/ios_136x136_dark>`{.interpreted-text
role="ref"}

iOS application 68x68 icon file (2x DPI), dark version. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/ios_136x136_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/ios_136x136_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/ios_136x136_tinted>`{.interpreted-text
role="ref"}

iOS application 68x68 icon file (2x DPI), tinted version. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/ios_192x192}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/ios_192x192**
`🔗<class_EditorExportPlatformIOS_property_icons/ios_192x192>`{.interpreted-text
role="ref"}

iOS application 64x64 icon file (3x DPI). If left empty, it will
fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/ios_192x192_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/ios_192x192_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/ios_192x192_dark>`{.interpreted-text
role="ref"}

iOS application 64x64 icon file (3x DPI), dark version. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/ios_192x192_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/ios_192x192_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/ios_192x192_tinted>`{.interpreted-text
role="ref"}

iOS application 64x64 icon file (3x DPI), tinted version. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/ipad_152x152}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/ipad_152x152**
`🔗<class_EditorExportPlatformIOS_property_icons/ipad_152x152>`{.interpreted-text
role="ref"}

Home screen application icon file on iPad (2x DPI). If left empty, it
will fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/ipad_152x152_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/ipad_152x152_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/ipad_152x152_dark>`{.interpreted-text
role="ref"}

Home screen application icon file on iPad (2x DPI), dark version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/ipad_152x152_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/ipad_152x152_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/ipad_152x152_tinted>`{.interpreted-text
role="ref"}

Home screen application icon file on iPad (2x DPI), tinted version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/ipad_167x167}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/ipad_167x167**
`🔗<class_EditorExportPlatformIOS_property_icons/ipad_167x167>`{.interpreted-text
role="ref"}

Home screen application icon file on iPad (3x DPI). If left empty, it
will fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/ipad_167x167_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/ipad_167x167_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/ipad_167x167_dark>`{.interpreted-text
role="ref"}

Home screen application icon file on iPad (3x DPI), dark version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/ipad_167x167_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/ipad_167x167_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/ipad_167x167_tinted>`{.interpreted-text
role="ref"}

Home screen application icon file on iPad (3x DPI), tinted version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/iphone_120x120}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/iphone_120x120**
`🔗<class_EditorExportPlatformIOS_property_icons/iphone_120x120>`{.interpreted-text
role="ref"}

Home screen application icon file on iPhone (2x DPI). If left empty, it
will fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/iphone_120x120_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/iphone_120x120_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/iphone_120x120_dark>`{.interpreted-text
role="ref"}

Home screen application icon file on iPhone (2x DPI), dark version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/iphone_120x120_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/iphone_120x120_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/iphone_120x120_tinted>`{.interpreted-text
role="ref"}

Home screen application icon file on iPhone (2x DPI), tinted version.
See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/iphone_180x180}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/iphone_180x180**
`🔗<class_EditorExportPlatformIOS_property_icons/iphone_180x180>`{.interpreted-text
role="ref"}

Home screen application icon file on iPhone (3x DPI). If left empty, it
will fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/iphone_180x180_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/iphone_180x180_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/iphone_180x180_dark>`{.interpreted-text
role="ref"}

Home screen application icon file on iPhone (3x DPI), dark version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/iphone_180x180_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/iphone_180x180_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/iphone_180x180_tinted>`{.interpreted-text
role="ref"}

Home screen application icon file on iPhone (3x DPI), tinted version.
See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/notification_40x40}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/notification_40x40**
`🔗<class_EditorExportPlatformIOS_property_icons/notification_40x40>`{.interpreted-text
role="ref"}

Notification icon file on iPad and iPhone (2x DPI). If left empty, it
will fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/notification_40x40_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/notification_40x40_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/notification_40x40_dark>`{.interpreted-text
role="ref"}

Notification icon file on iPad and iPhone (2x DPI), dark version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/notification_40x40_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/notification_40x40_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/notification_40x40_tinted>`{.interpreted-text
role="ref"}

Notification icon file on iPad and iPhone (2x DPI), tinted version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/notification_60x60}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/notification_60x60**
`🔗<class_EditorExportPlatformIOS_property_icons/notification_60x60>`{.interpreted-text
role="ref"}

Notification icon file on iPhone (3x DPI). If left empty, it will
fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/notification_60x60_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/notification_60x60_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/notification_60x60_dark>`{.interpreted-text
role="ref"}

Notification icon file on iPhone (3x DPI), dark version. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/notification_60x60_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/notification_60x60_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/notification_60x60_tinted>`{.interpreted-text
role="ref"}

Notification icon file on iPhone (3x DPI), tinted version. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/notification_76x76}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/notification_76x76**
`🔗<class_EditorExportPlatformIOS_property_icons/notification_76x76>`{.interpreted-text
role="ref"}

Notification icon file on iPad and iPhone (2x DPI). If left empty, it
will fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/notification_76x76_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/notification_76x76_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/notification_76x76_dark>`{.interpreted-text
role="ref"}

Notification icon file on iPad and iPhone (2x DPI), dark version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/notification_76x76_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/notification_76x76_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/notification_76x76_tinted>`{.interpreted-text
role="ref"}

Notification icon file on iPad and iPhone (2x DPI), tinted version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/notification_114x114}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/notification_114x114**
`🔗<class_EditorExportPlatformIOS_property_icons/notification_114x114>`{.interpreted-text
role="ref"}

Notification icon file on iPad and iPhone (3x DPI). If left empty, it
will fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/notification_114x114_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/notification_114x114_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/notification_114x114_dark>`{.interpreted-text
role="ref"}

Notification icon file on iPad and iPhone (3x DPI), dark version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/notification_114x114_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/notification_114x114_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/notification_114x114_tinted>`{.interpreted-text
role="ref"}

Notification icon file on iPad and iPhone (3x DPI), tinted version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/settings_58x58}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/settings_58x58**
`🔗<class_EditorExportPlatformIOS_property_icons/settings_58x58>`{.interpreted-text
role="ref"}

Application settings icon file on iPad and iPhone (2x DPI). If left
empty, it will fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/settings_58x58_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/settings_58x58_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/settings_58x58_dark>`{.interpreted-text
role="ref"}

Application settings icon file on iPad and iPhone (2x DPI), dark
version. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/settings_58x58_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/settings_58x58_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/settings_58x58_tinted>`{.interpreted-text
role="ref"}

Application settings icon file on iPad and iPhone (2x DPI), tinted
version. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/settings_87x87}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/settings_87x87**
`🔗<class_EditorExportPlatformIOS_property_icons/settings_87x87>`{.interpreted-text
role="ref"}

Application settings icon file on iPhone (3x DPI). If left empty, it
will fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/settings_87x87_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/settings_87x87_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/settings_87x87_dark>`{.interpreted-text
role="ref"}

Application settings icon file on iPhone (3x DPI), dark version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/settings_87x87_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/settings_87x87_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/settings_87x87_tinted>`{.interpreted-text
role="ref"}

Application settings icon file on iPhone (3x DPI), tinted version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/spotlight_80x80}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/spotlight_80x80**
`🔗<class_EditorExportPlatformIOS_property_icons/spotlight_80x80>`{.interpreted-text
role="ref"}

Spotlight icon file on iPad and iPhone (2x DPI). If left empty, it will
fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/spotlight_80x80_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/spotlight_80x80_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/spotlight_80x80_dark>`{.interpreted-text
role="ref"}

Spotlight icon file on iPad and iPhone (2x DPI), dark version. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/spotlight_80x80_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/spotlight_80x80_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/spotlight_80x80_tinted>`{.interpreted-text
role="ref"}

Spotlight icon file on iPad and iPhone (2x DPI), tinted version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/spotlight_120x120}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/spotlight_120x120**
`🔗<class_EditorExportPlatformIOS_property_icons/spotlight_120x120>`{.interpreted-text
role="ref"}

Spotlight icon file on iPad and iPhone (3x DPI). If left empty, it will
fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/spotlight_120x120_dark}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/spotlight_120x120_dark**
`🔗<class_EditorExportPlatformIOS_property_icons/spotlight_120x120_dark>`{.interpreted-text
role="ref"}

Spotlight icon file on iPad and iPhone (3x DPI), dark version. See [App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_icons/spotlight_120x120_tinted}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**icons/spotlight_120x120_tinted**
`🔗<class_EditorExportPlatformIOS_property_icons/spotlight_120x120_tinted>`{.interpreted-text
role="ref"}

Spotlight icon file on iPad and iPhone (3x DPI), tinted version. See
[App
icons](https://developer.apple.com/design/human-interface-guidelines/foundations/app-icons).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/active_keyboard_access_reasons}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/active_keyboard_access_reasons**
`🔗<class_EditorExportPlatformIOS_property_privacy/active_keyboard_access_reasons>`{.interpreted-text
role="ref"}

The reasons your app use active keyboard API. See [Describing use of
required reason
API](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/camera_usage_description}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**privacy/camera_usage_description**
`🔗<class_EditorExportPlatformIOS_property_privacy/camera_usage_description>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the device\'s camera (in
English).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/camera_usage_description_localized}
::: {.rst-class}
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**privacy/camera_usage_description_localized**
`🔗<class_EditorExportPlatformIOS_property_privacy/camera_usage_description_localized>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the device\'s camera
(localized).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/advertising_data/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/advertising_data/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/advertising_data/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects advertising data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/advertising_data/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/advertising_data/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/advertising_data/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects advertising data. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/advertising_data/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/advertising_data/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/advertising_data/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links advertising data to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/advertising_data/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/advertising_data/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/advertising_data/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses advertising data for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/audio_data/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/audio_data/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/audio_data/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects audio data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/audio_data/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/audio_data/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/audio_data/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects audio data. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/audio_data/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/audio_data/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/audio_data/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links audio data to the user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/audio_data/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/audio_data/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/audio_data/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses audio data for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/browsing_history/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/browsing_history/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/browsing_history/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects browsing history.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/browsing_history/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/browsing_history/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/browsing_history/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects browsing history. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/browsing_history/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/browsing_history/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/browsing_history/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links browsing history to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/browsing_history/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/browsing_history/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/browsing_history/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses browsing history for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/coarse_location/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/coarse_location/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/coarse_location/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects coarse location data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/coarse_location/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/coarse_location/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/coarse_location/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects coarse location data. See [Describing data
use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/coarse_location/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/coarse_location/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/coarse_location/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links coarse location data to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/coarse_location/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/coarse_location/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/coarse_location/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses coarse location data for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/contacts/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/contacts/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/contacts/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects contacts.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/contacts/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/contacts/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/contacts/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects contacts. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/contacts/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/contacts/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/contacts/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links contacts to the user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/contacts/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/contacts/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/contacts/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses contacts for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/crash_data/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/crash_data/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/crash_data/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects crash data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/crash_data/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/crash_data/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/crash_data/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects crash data. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/crash_data/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/crash_data/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/crash_data/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links crash data to the user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/crash_data/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/crash_data/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/crash_data/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses crash data for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/credit_info/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/credit_info/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/credit_info/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects credit information.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/credit_info/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/credit_info/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/credit_info/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects credit information. See [Describing data
use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/credit_info/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/credit_info/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/credit_info/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links credit information to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/credit_info/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/credit_info/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/credit_info/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses credit information for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/customer_support/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/customer_support/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/customer_support/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects customer support data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/customer_support/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/customer_support/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/customer_support/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects customer support data. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/customer_support/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/customer_support/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/customer_support/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links customer support data to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/customer_support/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/customer_support/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/customer_support/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses customer support data for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/device_id/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/device_id/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/device_id/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects device IDs.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/device_id/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/device_id/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/device_id/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects device IDs. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/device_id/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/device_id/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/device_id/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links device IDs to the user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/device_id/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/device_id/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/device_id/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses device IDs for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/email_address/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/email_address/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/email_address/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects email address.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/email_address/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/email_address/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/email_address/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects email address. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/email_address/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/email_address/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/email_address/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links email address to the user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/email_address/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/email_address/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/email_address/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses email address for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/emails_or_text_messages/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/emails_or_text_messages/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/emails_or_text_messages/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects emails or text messages.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/emails_or_text_messages/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/emails_or_text_messages/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/emails_or_text_messages/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects emails or text messages. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/emails_or_text_messages/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/emails_or_text_messages/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/emails_or_text_messages/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links emails or text messages to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/emails_or_text_messages/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/emails_or_text_messages/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/emails_or_text_messages/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses emails or text messages for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/environment_scanning/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/environment_scanning/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/environment_scanning/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects environment scanning data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/environment_scanning/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/environment_scanning/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/environment_scanning/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects environment scanning data. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/environment_scanning/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/environment_scanning/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/environment_scanning/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links environment scanning data to the
user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/environment_scanning/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/environment_scanning/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/environment_scanning/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses environment scanning data for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/fitness/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/fitness/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/fitness/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects fitness and exercise data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/fitness/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/fitness/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/fitness/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects fitness and exercise data. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/fitness/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/fitness/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/fitness/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links fitness and exercise data to the
user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/fitness/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/fitness/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/fitness/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses fitness and exercise data for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/gameplay_content/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/gameplay_content/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/gameplay_content/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects gameplay content.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/gameplay_content/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/gameplay_content/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/gameplay_content/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects gameplay content. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/gameplay_content/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/gameplay_content/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/gameplay_content/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links gameplay content to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/gameplay_content/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/gameplay_content/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/gameplay_content/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses gameplay content for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/hands/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/hands/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/hands/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects user\'s hand structure and hand
movements.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/hands/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/hands/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/hands/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects user\'s hand structure and hand movements.
See [Describing data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/hands/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/hands/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/hands/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links user\'s hand structure and hand
movements to the user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/hands/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/hands/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/hands/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses user\'s hand structure and hand
movements for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/head/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/head/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/head/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects user\'s head movement.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/head/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/head/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/head/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects user\'s head movement. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/head/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/head/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/head/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links user\'s head movement to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/head/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/head/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/head/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses user\'s head movement for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/health/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/health/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/health/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects health and medical data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/health/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/health/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/health/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects health and medical data. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/health/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/health/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/health/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links health and medical data to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/health/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/health/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/health/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses health and medical data for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/name/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/name/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/name/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects user\'s name.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/name/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/name/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/name/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects user\'s name. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/name/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/name/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/name/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links user\'s name to the user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/name/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/name/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/name/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses user\'s name for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_contact_info/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_contact_info/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_contact_info/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects any other contact information.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_contact_info/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/other_contact_info/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_contact_info/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects any other contact information. See
[Describing data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_contact_info/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_contact_info/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_contact_info/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links any other contact information to the
user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_contact_info/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_contact_info/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_contact_info/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses any other contact information for
tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_data_types/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_data_types/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_data_types/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects any other data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_data_types/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/other_data_types/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_data_types/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects any other data. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_data_types/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_data_types/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_data_types/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links any other data to the user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_data_types/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_data_types/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_data_types/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses any other data for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_diagnostic_data/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_diagnostic_data/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_diagnostic_data/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects any other diagnostic data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_diagnostic_data/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/other_diagnostic_data/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_diagnostic_data/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects any other diagnostic data. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_diagnostic_data/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_diagnostic_data/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_diagnostic_data/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links any other diagnostic data to the
user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_diagnostic_data/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_diagnostic_data/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_diagnostic_data/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses any other diagnostic data for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_financial_info/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_financial_info/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_financial_info/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects any other financial information.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_financial_info/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/other_financial_info/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_financial_info/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects any other financial information. See
[Describing data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_financial_info/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_financial_info/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_financial_info/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links any other financial information to the
user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_financial_info/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_financial_info/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_financial_info/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses any other financial information for
tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_usage_data/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_usage_data/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_usage_data/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects any other usage data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_usage_data/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/other_usage_data/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_usage_data/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects any other usage data. See [Describing data
use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_usage_data/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_usage_data/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_usage_data/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links any other usage data to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_usage_data/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_usage_data/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_usage_data/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses any other usage data for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_user_content/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_user_content/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_user_content/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects any other user generated content.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_user_content/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/other_user_content/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_user_content/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects any other user generated content. See
[Describing data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_user_content/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_user_content/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_user_content/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links any other user generated content to the
user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/other_user_content/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_user_content/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/other_user_content/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses any other user generated content for
tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/payment_info/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/payment_info/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/payment_info/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects payment information.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/payment_info/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/payment_info/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/payment_info/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects payment information. See [Describing data
use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/payment_info/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/payment_info/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/payment_info/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links payment information to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/payment_info/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/payment_info/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/payment_info/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses payment information for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/performance_data/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/performance_data/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/performance_data/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects performance data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/performance_data/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/performance_data/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/performance_data/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects performance data. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/performance_data/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/performance_data/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/performance_data/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links performance data to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/performance_data/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/performance_data/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/performance_data/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses performance data for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/phone_number/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/phone_number/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/phone_number/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects phone number.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/phone_number/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/phone_number/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/phone_number/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects phone number. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/phone_number/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/phone_number/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/phone_number/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links phone number to the user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/phone_number/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/phone_number/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/phone_number/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses phone number for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/photos_or_videos/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/photos_or_videos/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/photos_or_videos/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects photos or videos.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/photos_or_videos/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/photos_or_videos/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/photos_or_videos/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects photos or videos. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/photos_or_videos/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/photos_or_videos/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/photos_or_videos/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links photos or videos to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/photos_or_videos/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/photos_or_videos/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/photos_or_videos/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses photos or videos for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/physical_address/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/physical_address/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/physical_address/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects physical address.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/physical_address/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/physical_address/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/physical_address/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects physical address. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/physical_address/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/physical_address/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/physical_address/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links physical address to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/physical_address/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/physical_address/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/physical_address/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses physical address for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/precise_location/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/precise_location/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/precise_location/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects precise location data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/precise_location/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/precise_location/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/precise_location/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects precise location data. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/precise_location/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/precise_location/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/precise_location/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links precise location data to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/precise_location/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/precise_location/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/precise_location/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses precise location data for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/product_interaction/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/product_interaction/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/product_interaction/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects product interaction data.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/product_interaction/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/product_interaction/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/product_interaction/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects product interaction data. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/product_interaction/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/product_interaction/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/product_interaction/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links product interaction data to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/product_interaction/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/product_interaction/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/product_interaction/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses product interaction data for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/purchase_history/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/purchase_history/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/purchase_history/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects purchase history.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/purchase_history/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/purchase_history/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/purchase_history/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects purchase history. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/purchase_history/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/purchase_history/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/purchase_history/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links purchase history to the user\'s
identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/purchase_history/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/purchase_history/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/purchase_history/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses purchase history for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/search_hhistory/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/search_hhistory/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/search_hhistory/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects search history.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/search_hhistory/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/search_hhistory/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/search_hhistory/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects search history. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/search_hhistory/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/search_hhistory/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/search_hhistory/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links search history to the user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/search_hhistory/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/search_hhistory/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/search_hhistory/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses search history for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/sensitive_info/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/sensitive_info/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/sensitive_info/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects sensitive user information.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/sensitive_info/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/sensitive_info/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/sensitive_info/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects sensitive user information. See
[Describing data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/sensitive_info/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/sensitive_info/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/sensitive_info/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links sensitive user information to the
user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/sensitive_info/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/sensitive_info/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/sensitive_info/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses sensitive user information for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/user_id/collected}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/user_id/collected**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/user_id/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects user IDs.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/user_id/collection_purposes}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/user_id/collection_purposes**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/user_id/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects user IDs. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/user_id/linked_to_user}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/user_id/linked_to_user**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/user_id/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links user IDs to the user\'s identity.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/collected_data/user_id/used_for_tracking}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/user_id/used_for_tracking**
`🔗<class_EditorExportPlatformIOS_property_privacy/collected_data/user_id/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses user IDs for tracking.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/disk_space_access_reasons}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/disk_space_access_reasons**
`🔗<class_EditorExportPlatformIOS_property_privacy/disk_space_access_reasons>`{.interpreted-text
role="ref"}

The reasons your app use free disk space API. See [Describing use of
required reason
API](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/file_timestamp_access_reasons}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/file_timestamp_access_reasons**
`🔗<class_EditorExportPlatformIOS_property_privacy/file_timestamp_access_reasons>`{.interpreted-text
role="ref"}

The reasons your app use file timestamp/metadata API. See [Describing
use of required reason
API](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/microphone_usage_description}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**privacy/microphone_usage_description**
`🔗<class_EditorExportPlatformIOS_property_privacy/microphone_usage_description>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the device\'s microphone
(in English).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/microphone_usage_description_localized}
::: {.rst-class}
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**privacy/microphone_usage_description_localized**
`🔗<class_EditorExportPlatformIOS_property_privacy/microphone_usage_description_localized>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the device\'s microphone
(localized).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/photolibrary_usage_description}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**privacy/photolibrary_usage_description**
`🔗<class_EditorExportPlatformIOS_property_privacy/photolibrary_usage_description>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s photo library
(in English).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/photolibrary_usage_description_localized}
::: {.rst-class}
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**privacy/photolibrary_usage_description_localized**
`🔗<class_EditorExportPlatformIOS_property_privacy/photolibrary_usage_description_localized>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s photo library
(localized).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/system_boot_time_access_reasons}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/system_boot_time_access_reasons**
`🔗<class_EditorExportPlatformIOS_property_privacy/system_boot_time_access_reasons>`{.interpreted-text
role="ref"}

The reasons your app use system boot time / absolute time API. See
[Describing use of required reason
API](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/tracking_domains}
::: {.rst-class}
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **privacy/tracking_domains**
`🔗<class_EditorExportPlatformIOS_property_privacy/tracking_domains>`{.interpreted-text
role="ref"}

The list of internet domains your app connects to that engage in
tracking. See [Privacy manifest
files](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/tracking_enabled}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/tracking_enabled**
`🔗<class_EditorExportPlatformIOS_property_privacy/tracking_enabled>`{.interpreted-text
role="ref"}

Indicates whether your app uses data for tracking. See [Privacy manifest
files](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_privacy/user_defaults_access_reasons}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/user_defaults_access_reasons**
`🔗<class_EditorExportPlatformIOS_property_privacy/user_defaults_access_reasons>`{.interpreted-text
role="ref"}

The reasons your app use user defaults API. See [Describing use of
required reason
API](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_storyboard/custom_bg_color}
::: {.rst-class}
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**storyboard/custom_bg_color**
`🔗<class_EditorExportPlatformIOS_property_storyboard/custom_bg_color>`{.interpreted-text
role="ref"}

A custom background color of the storyboard launch screen.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_storyboard/custom_image@2x}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**storyboard/custom_image@2x**
`🔗<class_EditorExportPlatformIOS_property_storyboard/custom_image@2x>`{.interpreted-text
role="ref"}

Application launch screen image file (2x DPI). If left empty, it will
fallback to
`ProjectSettings.application/boot_splash/image<class_ProjectSettings_property_application/boot_splash/image>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_storyboard/custom_image@3x}
::: {.rst-class}
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**storyboard/custom_image@3x**
`🔗<class_EditorExportPlatformIOS_property_storyboard/custom_image@3x>`{.interpreted-text
role="ref"}

Application launch screen image file (3x DPI). If left empty, it will
fallback to
`ProjectSettings.application/boot_splash/image<class_ProjectSettings_property_application/boot_splash/image>`{.interpreted-text
role="ref"}.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_storyboard/image_scale_mode}
::: {.rst-class}
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**storyboard/image_scale_mode**
`🔗<class_EditorExportPlatformIOS_property_storyboard/image_scale_mode>`{.interpreted-text
role="ref"}

Launch screen image scaling mode.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_storyboard/use_custom_bg_color}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**storyboard/use_custom_bg_color**
`🔗<class_EditorExportPlatformIOS_property_storyboard/use_custom_bg_color>`{.interpreted-text
role="ref"}

If `true`,
`storyboard/custom_bg_color<class_EditorExportPlatformIOS_property_storyboard/custom_bg_color>`{.interpreted-text
role="ref"} is used as a launch screen background color, otherwise
`application/boot_splash/bg_color` project setting is used.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_user_data/accessible_from_files_app}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**user_data/accessible_from_files_app**
`🔗<class_EditorExportPlatformIOS_property_user_data/accessible_from_files_app>`{.interpreted-text
role="ref"}

If `true`, the app \"Documents\" folder can be accessed via \"Files\"
app. See
[LSSupportsOpeningDocumentsInPlace](https://developer.apple.com/documentation/bundleresources/information_property_list/lssupportsopeningdocumentsinplace).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformIOS_property_user_data/accessible_from_itunes_sharing}
::: {.rst-class}
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**user_data/accessible_from_itunes_sharing**
`🔗<class_EditorExportPlatformIOS_property_user_data/accessible_from_itunes_sharing>`{.interpreted-text
role="ref"}

If `true`, the app \"Documents\" folder can be accessed via iTunes file
sharing. See
[UIFileSharingEnabled](https://developer.apple.com/documentation/bundleresources/information_property_list/uifilesharingenabled).
