github_url

:   hide

# Time {#class_Time}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A singleton for working with time data.

::: {.rst-class}
classref-introduction-group
:::

## Description

The Time singleton allows converting time between various formats and
also getting time information from the system.

This class conforms with as many of the ISO 8601 standards as possible.
All dates follow the Proleptic Gregorian calendar. As such, the day
before `1582-10-15` is `1582-10-14`, not `1582-10-04`. The year before 1
AD (aka 1 BC) is number `0`, with the year before that (2 BC) being
`-1`, etc.

Conversion methods assume \"the same timezone\", and do not handle
timezone conversions or DST automatically. Leap seconds are also not
handled, they must be done manually if desired. Suffixes such as \"Z\"
are not handled, you need to strip them away manually.

When getting time information from the system, the time can either be in
the local timezone or UTC depending on the `utc` parameter. However, the
`get_unix_time_from_system<class_Time_method_get_unix_time_from_system>`{.interpreted-text
role="ref"} method always uses UTC as it returns the seconds passed
since the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time).

\*\*Important:\*\* The `_from_system` methods use the system clock that
the user can manually set. **Never use** this method for precise time
calculation since its results are subject to automatic adjustments by
the user or the operating system. **Always use**
`get_ticks_usec<class_Time_method_get_ticks_usec>`{.interpreted-text
role="ref"} or
`get_ticks_msec<class_Time_method_get_ticks_msec>`{.interpreted-text
role="ref"} for precise time calculation instead, since they are
guaranteed to be monotonic (i.e. never decrease).

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

:::: {#enum_Time_Month}
::: {.rst-class}
classref-enumeration
:::
::::

enum **Month**: `🔗<enum_Time_Month>`{.interpreted-text role="ref"}

:::: {#class_Time_constant_MONTH_JANUARY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Month<enum_Time_Month>`{.interpreted-text role="ref"} **MONTH_JANUARY**
= `1`

The month of January, represented numerically as `01`.

:::: {#class_Time_constant_MONTH_FEBRUARY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Month<enum_Time_Month>`{.interpreted-text role="ref"}
**MONTH_FEBRUARY** = `2`

The month of February, represented numerically as `02`.

:::: {#class_Time_constant_MONTH_MARCH}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Month<enum_Time_Month>`{.interpreted-text role="ref"} **MONTH_MARCH** =
`3`

The month of March, represented numerically as `03`.

:::: {#class_Time_constant_MONTH_APRIL}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Month<enum_Time_Month>`{.interpreted-text role="ref"} **MONTH_APRIL** =
`4`

The month of April, represented numerically as `04`.

:::: {#class_Time_constant_MONTH_MAY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Month<enum_Time_Month>`{.interpreted-text role="ref"} **MONTH_MAY** =
`5`

The month of May, represented numerically as `05`.

:::: {#class_Time_constant_MONTH_JUNE}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Month<enum_Time_Month>`{.interpreted-text role="ref"} **MONTH_JUNE** =
`6`

The month of June, represented numerically as `06`.

:::: {#class_Time_constant_MONTH_JULY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Month<enum_Time_Month>`{.interpreted-text role="ref"} **MONTH_JULY** =
`7`

The month of July, represented numerically as `07`.

:::: {#class_Time_constant_MONTH_AUGUST}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Month<enum_Time_Month>`{.interpreted-text role="ref"} **MONTH_AUGUST**
= `8`

The month of August, represented numerically as `08`.

:::: {#class_Time_constant_MONTH_SEPTEMBER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Month<enum_Time_Month>`{.interpreted-text role="ref"}
**MONTH_SEPTEMBER** = `9`

The month of September, represented numerically as `09`.

:::: {#class_Time_constant_MONTH_OCTOBER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Month<enum_Time_Month>`{.interpreted-text role="ref"} **MONTH_OCTOBER**
= `10`

The month of October, represented numerically as `10`.

:::: {#class_Time_constant_MONTH_NOVEMBER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Month<enum_Time_Month>`{.interpreted-text role="ref"}
**MONTH_NOVEMBER** = `11`

The month of November, represented numerically as `11`.

:::: {#class_Time_constant_MONTH_DECEMBER}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Month<enum_Time_Month>`{.interpreted-text role="ref"}
**MONTH_DECEMBER** = `12`

The month of December, represented numerically as `12`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Time_Weekday}
::: {.rst-class}
classref-enumeration
:::
::::

enum **Weekday**: `🔗<enum_Time_Weekday>`{.interpreted-text role="ref"}

:::: {#class_Time_constant_WEEKDAY_SUNDAY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Weekday<enum_Time_Weekday>`{.interpreted-text role="ref"}
**WEEKDAY_SUNDAY** = `0`

The day of the week Sunday, represented numerically as `0`.

:::: {#class_Time_constant_WEEKDAY_MONDAY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Weekday<enum_Time_Weekday>`{.interpreted-text role="ref"}
**WEEKDAY_MONDAY** = `1`

The day of the week Monday, represented numerically as `1`.

:::: {#class_Time_constant_WEEKDAY_TUESDAY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Weekday<enum_Time_Weekday>`{.interpreted-text role="ref"}
**WEEKDAY_TUESDAY** = `2`

The day of the week Tuesday, represented numerically as `2`.

:::: {#class_Time_constant_WEEKDAY_WEDNESDAY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Weekday<enum_Time_Weekday>`{.interpreted-text role="ref"}
**WEEKDAY_WEDNESDAY** = `3`

The day of the week Wednesday, represented numerically as `3`.

:::: {#class_Time_constant_WEEKDAY_THURSDAY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Weekday<enum_Time_Weekday>`{.interpreted-text role="ref"}
**WEEKDAY_THURSDAY** = `4`

The day of the week Thursday, represented numerically as `4`.

:::: {#class_Time_constant_WEEKDAY_FRIDAY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Weekday<enum_Time_Weekday>`{.interpreted-text role="ref"}
**WEEKDAY_FRIDAY** = `5`

The day of the week Friday, represented numerically as `5`.

:::: {#class_Time_constant_WEEKDAY_SATURDAY}
::: {.rst-class}
classref-enumeration-constant
:::
::::

`Weekday<enum_Time_Weekday>`{.interpreted-text role="ref"}
**WEEKDAY_SATURDAY** = `6`

The day of the week Saturday, represented numerically as `6`.

::: {.rst-class}
classref-section-separator
:::

------------------------------------------------------------------------

::: {.rst-class}
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Time_method_get_date_dict_from_system}
::: {.rst-class}
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_date_dict_from_system**(utc: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_date_dict_from_system>`{.interpreted-text
role="ref"}

Returns the current date as a dictionary of keys: `year`, `month`,
`day`, and `weekday`.

The returned values are in the system\'s local time when `utc` is
`false`, otherwise they are in UTC.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_date_dict_from_unix_time}
::: {.rst-class}
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_date_dict_from_unix_time**(unix_time_val:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_date_dict_from_unix_time>`{.interpreted-text
role="ref"}

Converts the given Unix timestamp to a dictionary of keys: `year`,
`month`, `day`, and `weekday`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_date_string_from_system}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_date_string_from_system**(utc:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_date_string_from_system>`{.interpreted-text
role="ref"}

Returns the current date as an ISO 8601 date string (YYYY-MM-DD).

The returned values are in the system\'s local time when `utc` is
`false`, otherwise they are in UTC.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_date_string_from_unix_time}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_date_string_from_unix_time**(unix_time_val:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_date_string_from_unix_time>`{.interpreted-text
role="ref"}

Converts the given Unix timestamp to an ISO 8601 date string
(YYYY-MM-DD).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_datetime_dict_from_datetime_string}
::: {.rst-class}
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_datetime_dict_from_datetime_string**(datetime:
`String<class_String>`{.interpreted-text role="ref"}, weekday:
`bool<class_bool>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_datetime_dict_from_datetime_string>`{.interpreted-text
role="ref"}

Converts the given ISO 8601 date and time string (YYYY-MM-DDTHH:MM:SS)
to a dictionary of keys: `year`, `month`, `day`, `weekday`, `hour`,
`minute`, and `second`.

If `weekday` is `false`, then the `weekday` entry is excluded (the
calculation is relatively expensive).

\*\*Note:\*\* Any decimal fraction in the time string will be ignored
silently.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_datetime_dict_from_system}
::: {.rst-class}
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_datetime_dict_from_system**(utc:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_datetime_dict_from_system>`{.interpreted-text
role="ref"}

Returns the current date as a dictionary of keys: `year`, `month`,
`day`, `weekday`, `hour`, `minute`, `second`, and `dst` (Daylight
Savings Time).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_datetime_dict_from_unix_time}
::: {.rst-class}
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_datetime_dict_from_unix_time**(unix_time_val:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_datetime_dict_from_unix_time>`{.interpreted-text
role="ref"}

Converts the given Unix timestamp to a dictionary of keys: `year`,
`month`, `day`, `weekday`, `hour`, `minute`, and `second`.

The returned Dictionary\'s values will be the same as the
`get_datetime_dict_from_system<class_Time_method_get_datetime_dict_from_system>`{.interpreted-text
role="ref"} if the Unix timestamp is the current time, with the
exception of Daylight Savings Time as it cannot be determined from the
epoch.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_datetime_string_from_datetime_dict}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_datetime_string_from_datetime_dict**(datetime:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}, use_space:
`bool<class_bool>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_datetime_string_from_datetime_dict>`{.interpreted-text
role="ref"}

Converts the given dictionary of keys to an ISO 8601 date and time
string (YYYY-MM-DDTHH:MM:SS).

The given dictionary can be populated with the following keys: `year`,
`month`, `day`, `hour`, `minute`, and `second`. Any other entries
(including `dst`) are ignored.

If the dictionary is empty, `0` is returned. If some keys are omitted,
they default to the equivalent values for the Unix epoch timestamp 0
(1970-01-01 at 00:00:00).

If `use_space` is `true`, the date and time bits are separated by an
empty space character instead of the letter T.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_datetime_string_from_system}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_datetime_string_from_system**(utc:
`bool<class_bool>`{.interpreted-text role="ref"} = false, use_space:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_datetime_string_from_system>`{.interpreted-text
role="ref"}

Returns the current date and time as an ISO 8601 date and time string
(YYYY-MM-DDTHH:MM:SS).

The returned values are in the system\'s local time when `utc` is
`false`, otherwise they are in UTC.

If `use_space` is `true`, the date and time bits are separated by an
empty space character instead of the letter T.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_datetime_string_from_unix_time}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_datetime_string_from_unix_time**(unix_time_val:
`int<class_int>`{.interpreted-text role="ref"}, use_space:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_datetime_string_from_unix_time>`{.interpreted-text
role="ref"}

Converts the given Unix timestamp to an ISO 8601 date and time string
(YYYY-MM-DDTHH:MM:SS).

If `use_space` is `true`, the date and time bits are separated by an
empty space character instead of the letter T.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_offset_string_from_offset_minutes}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_offset_string_from_offset_minutes**(offset_minutes:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_offset_string_from_offset_minutes>`{.interpreted-text
role="ref"}

Converts the given timezone offset in minutes to a timezone offset
string. For example, -480 returns \"-08:00\", 345 returns \"+05:45\",
and 0 returns \"+00:00\".

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_ticks_msec}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_ticks_msec**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Time_method_get_ticks_msec>`{.interpreted-text
role="ref"}

Returns the amount of time passed in milliseconds since the engine
started.

Will always be positive or 0 and uses a 64-bit value (it will wrap after
roughly 500 million years).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_ticks_usec}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_ticks_usec**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Time_method_get_ticks_usec>`{.interpreted-text
role="ref"}

Returns the amount of time passed in microseconds since the engine
started.

Will always be positive or 0 and uses a 64-bit value (it will wrap after
roughly half a million years).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_time_dict_from_system}
::: {.rst-class}
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_time_dict_from_system**(utc: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_time_dict_from_system>`{.interpreted-text
role="ref"}

Returns the current time as a dictionary of keys: `hour`, `minute`, and
`second`.

The returned values are in the system\'s local time when `utc` is
`false`, otherwise they are in UTC.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_time_dict_from_unix_time}
::: {.rst-class}
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_time_dict_from_unix_time**(unix_time_val:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_time_dict_from_unix_time>`{.interpreted-text
role="ref"}

Converts the given time to a dictionary of keys: `hour`, `minute`, and
`second`.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_time_string_from_system}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_time_string_from_system**(utc:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_time_string_from_system>`{.interpreted-text
role="ref"}

Returns the current time as an ISO 8601 time string (HH:MM:SS).

The returned values are in the system\'s local time when `utc` is
`false`, otherwise they are in UTC.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_time_string_from_unix_time}
::: {.rst-class}
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_time_string_from_unix_time**(unix_time_val:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_time_string_from_unix_time>`{.interpreted-text
role="ref"}

Converts the given Unix timestamp to an ISO 8601 time string (HH:MM:SS).

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_time_zone_from_system}
::: {.rst-class}
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_time_zone_from_system**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_time_zone_from_system>`{.interpreted-text
role="ref"}

Returns the current time zone as a dictionary of keys: `bias` and
`name`.

- `bias` is the offset from UTC in minutes, since not all time zones are
  multiples of an hour from UTC.
- `name` is the localized name of the time zone, according to the OS
  locale settings of the current user.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_unix_time_from_datetime_dict}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_unix_time_from_datetime_dict**(datetime:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_unix_time_from_datetime_dict>`{.interpreted-text
role="ref"}

Converts a dictionary of time values to a Unix timestamp.

The given dictionary can be populated with the following keys: `year`,
`month`, `day`, `hour`, `minute`, and `second`. Any other entries
(including `dst`) are ignored.

If the dictionary is empty, `0` is returned. If some keys are omitted,
they default to the equivalent values for the Unix epoch timestamp 0
(1970-01-01 at 00:00:00).

You can pass the output from
`get_datetime_dict_from_unix_time<class_Time_method_get_datetime_dict_from_unix_time>`{.interpreted-text
role="ref"} directly into this function and get the same as what was put
in.

\*\*Note:\*\* Unix timestamps are often in UTC. This method does not do
any timezone conversion, so the timestamp will be in the same timezone
as the given datetime dictionary.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_unix_time_from_datetime_string}
::: {.rst-class}
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_unix_time_from_datetime_string**(datetime:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_unix_time_from_datetime_string>`{.interpreted-text
role="ref"}

Converts the given ISO 8601 date and/or time string to a Unix timestamp.
The string can contain a date only, a time only, or both.

\*\*Note:\*\* Unix timestamps are often in UTC. This method does not do
any timezone conversion, so the timestamp will be in the same timezone
as the given datetime string.

\*\*Note:\*\* Any decimal fraction in the time string will be ignored
silently.

::: {.rst-class}
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Time_method_get_unix_time_from_system}
::: {.rst-class}
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_unix_time_from_system**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Time_method_get_unix_time_from_system>`{.interpreted-text
role="ref"}

Returns the current Unix timestamp in seconds based on the system time
in UTC. This method is implemented by the operating system and always
returns the time in UTC. The Unix timestamp is the number of seconds
passed since 1970-01-01 at 00:00:00, the [Unix
epoch](https://en.wikipedia.org/wiki/Unix_time).

\*\*Note:\*\* Unlike other methods that use integer timestamps, this
method returns the timestamp as a `float<class_float>`{.interpreted-text
role="ref"} for sub-second precision.