# TailwindCSS Cheatsheet

> A TailwindCSS cheatsheet in markdown

## Intro
This is a cheatsheet which shows the TailwindCSS classnames paired with the regular CSS descriptions. It was created to have this information easily available offline. 

The details used in this cheatsheet have been taken from the 3.0.24 version of the online cheatsheet provided by the website [tailwindcomponents.com](https://tailwindcomponents.com/cheatsheet/). It was then formatted into markdown.

## How to use this list
- You can search for your desired CSS classes with `Ctrl + F` (or `Cmd + F` on macOS). 
- Click on a link in the Contents section to take you to the details.
- Or simply copy/download everything, to use offline.

## Contents
[Layout](#layout)
 - [Aspect Ratio](#aspect-ratio)
 - [Container](#container)
 - [Columns](#columns)
 - [Break After](#break-after)
 - [Break Before](#break-before)
 - [Break Inside](#break-inside)
 - [Box Decoration Break](#box-decoration-break)
 - [Box Sizing](#box-sizing)
 - [Display](#display)
 - [Float](#float)
 - [Clear](#clear)
 - [Isolation](#isolation)
 - [Object Fit](#object-fit)
 - [Object Position](#object-position)
 - [Overflow](#overflow)
 - [Overscroll Behavior](#overscroll-behavior)
 - [Position](#position)
 - [Top / Right / Bottom / Left](#top-/-right-/-bottom-/-left)
 - [Visibility](#visibility)
 - [Z-index](#z-index)

[Sizing](#sizing)
 - [Width](#width)
 - [Min Width](#min-width)
 - [Max Width](#max-width)
 - [Height](#height)
 - [Min Height](#min-height)
 - [Max Height](#max-height)

[Transforms](#transforms)
 - [Scale](#scale)
 - [Rotate ](#rotate)
 - [Translate](#translate)
 - [Skew](#skew)
 - [Transform Origin](#transform-origin)

[Effects](#effects)
 - [Box Shadow](#box-shadow)
 - [Opacity](#opacity)
 - [Mix Blend Mode](#mix-blend-mode)
 - [Background Blend Mode](#background-blend-mode)

[Spacing](#spacing)
 - [Padding](#padding)
 - [Margin](#margin)
 - [Space Between](#space-between)

[Typography](#typography)
 - [Font Family](#font-family)
 - [Font Size ](#font-size)
 - [Font Smoothing](#font-smoothing)
 - [Font Style ](#font-style)
 - [Font Weight](#font-weight)
 - [Font Variant Numeric](#font-variant-numeric)
 - [Letter Spacing](#letter-spacing)
 - [Line Height](#line-height)
 - [List Style Type](#list-style-type)
 - [List Style Position](#list-style-position)
 - [Text Align](#text-align)
 - [Text Color](#text-color)
 - [Text Decoration](#text-decoration)
 - [Text Decoration Style](#text-decoration-style)
 - [Text Decoration Thickness](#text-decoration-thickness)
 - [Text Underline Offset](#text-underline-offset)
 - [Text Transform](#text-transform)
 - [Text Overflow](#text-overflow)
 - [Text Indent](#text-indent)
 - [Vertical Align](#vertical-align)
 - [White Space](#white-space)
 - [Word Break](#word-break)
 - [Content](#content)

[Interactivity](#interactivity)
 - [Appearance](#appearance)
 - [Cursor](#cursor)
 - [Pointer Events](#pointer-events)
 - [Resize ](#resize)
 - [Scroll Behavior](#scroll-behavior)
 - [Scroll Margin](#scroll-margin)
 - [Scroll Padding](#scroll-padding)
 - [Scroll Snap Align](#scroll-snap-align)
 - [Scroll Snap Stop](#scroll-snap-stop)
 - [Scroll Snap Type](#scroll-snap-type)
 - [Touch Action](#touch-action)
 - [User Select](#user-select)
 - [Will Change](#will-change)

[Filters](#filters)
 - [Blur](#blur)
 - [Brightness](#brightness)
 - [Contrast](#contrast)
 - [Drop Shadow](#drop-shadow)
 - [Grayscale](#grayscale)
 - [Hue Rotate](#hue-rotate)
 - [Invert](#invert)
 - [Saturate](#saturate)
 - [Sepia](#sepia)
 - [Backdrop Blur](#backdrop-blur)
 - [Backdrop Brightness](#backdrop-brightness)
 - [Backdrop Contrast ](#backdrop-contrast)
 - [Backdrop Grayscale](#backdrop-grayscale)
 - [Backdrop Hue Rotate](#backdrop-hue-rotate)
 - [Backdrop Invert](#backdrop-invert)
 - [Backdrop Opacity](#backdrop-opacity)
 - [Backdrop Saturate](#backdrop-saturate)
 - [Backdrop Sepia](#backdrop-sepia)

[Flexbox & Grid](#flexbox-&-grid)
 - [Flex basis](#flex-basis)
 - [Flex Direction](#flex-direction)
 - [Flex Wrap](#flex-wrap)
 - [Flex](#flex)
 - [Flex Grow](#flex-grow)
 - [Flex Shrink](#flex-shrink)
 - [Order](#order)
 - [Grid Template Columns](#grid-template-columns)
 - [Grid Column, start/end](#grid-column,-start/end)
 - [Grid Template Rows](#grid-template-rows)
 - [Grid Row, start/end](#grid-row,-start/end)
 - [Grid Auto Flow](#grid-auto-flow)
 - [Grid Auto Columns](#grid-auto-columns)
 - [Grid Auto Rows](#grid-auto-rows)
 - [Gap](#gap)
 - [Justify Content](#justify-content)
 - [Justify Items](#justify-items)
 - [Justify Self](#justify-self)
 - [Align Content](#align-content)
 - [Align Items](#align-items)
 - [Align Self](#align-self)
 - [Place Content](#place-content)
 - [Place Items](#place-items)
 - [Place Self](#place-self)

[Backgrounds](#backgrounds)
 - [Background Attachment](#background-attachment)
 - [Background Clip](#background-clip)
 - [Background Color](#background-color)
 - [Background Opacity](#background-opacity)
 - [Background Origin](#background-origin)
 - [Background Position](#background-position)
 - [Background Repeat](#background-repeat)
 - [Background Size](#background-size)
 - [Background Image](#background-image)
 - [Gradient Color Stops](#gradient-color-stops)

[SVG](#svg)
 - [Fill](#fill)
 - [Stroke](#stroke)
 - [Stroke Width](#stroke-width)

[Accessibility](#accessibility)
 - [Screen Readers](#screen-readers)

[Borders](#borders)
 - [Border Radius](#border-radius)
 - [Border Width](#border-width)
 - [Border Color](#border-color)
 - [Border Opacity](#border-opacity)
 - [Border Style](#border-style)
 - [Divide Width](#divide-width)
 - [Divide Color](#divide-color)
 - [Divide Opacity](#divide-opacity)
 - [Divide Style](#divide-style)
 - [Outline Width](#outline-width)
 - [Outline Style](#outline-style)
 - [Outline Offset](#outline-offset)
 - [Ring Width](#ring-width)
 - [Ring Color](#ring-color)
 - [Ring Opacity](#ring-opacity)
 - [Ring Offset Width](#ring-offset-width)
 - [Ring Offset Color](#ring-offset-color)

[Transitions & Animation](#transitions-&-animation)
 - [Transition Property](#transition-property)
 - [Transition Duration](#transition-duration)
 - [Transition Timing Function](#transition-timing-function)
 - [Transition Delay](#transition-delay)
 - [Animation](#animation)

[Tables](#tables)
 - [Border Collapse](#border-collapse)
 - [Table Layout](#table-layout)

---

## Layout

### Aspect Ratio
Utilities for controlling the aspect ratio of an element.

| Tailwind      | Description           | Other |
| ------------- | --------------------- | ----- |
| aspect-auto   | aspect-ratio: auto;   |       |
| aspect-square | aspect-ratio: 1 / 1;  |       |
| aspect-video  | aspect-ratio: 16 / 9; |       |


### Container
Sets the max-width to match the min-width of the current breakpoint.

| Tailwind  | Description  | Other              |
| --------- | ------------ | ------------------ |
| container | none         | width: 100%        |
|           | sm (640px)   | max-width: 640px;  |
|           | md (768px)   | max-width: 768px;  |
|           | lg (1024px)  | max-width: 1024px; |
|           | xl (1280px)  | max-width: 1280px; |
|           | 2xl (1536px) | max-width: 1536px; |


### Columns
Utilities for controlling the number of columns within an element.

| Tailwind     | Description     | Other |
| ------------ | --------------- | ----- |
| columns-1    | columns: 1;     |       |
| columns-2    | columns: 2;     |       |
| columns-3    | columns: 3;     |       |
| columns-4    | columns: 4;     |       |
| columns-5    | columns: 5;     |       |
| columns-6    | columns: 6;     |       |
| columns-7    | columns: 7;     |       |
| columns-8    | columns: 8;     |       |
| columns-9    | columns: 9;     |       |
| columns-10   | columns: 10;    |       |
| columns-11   | columns: 11;    |       |
| columns-12   | columns: 12;    |       |
| columns-auto | columns: auto;  |       |
| columns-3xs  | columns: 16rem; |       |
| columns-2xs  | columns: 18rem; |       |
| columns-xs   | columns: 20rem; |       |
| columns-sm   | columns: 24rem; |       |
| columns-md   | columns: 28rem; |       |
| columns-lg   | columns: 32rem; |       |
| columns-xl   | columns: 36rem; |       |
| columns-2xl  | columns: 42rem; |       |
| columns-3xl  | columns: 48rem; |       |
| columns-4xl  | columns: 56rem; |       |
| columns-5xl  | columns: 64rem; |       |
| columns-6xl  | columns: 72rem; |       |
| columns-7xl  | columns: 80rem; |       |



### Break After
Utilities for controlling how a column or page should break after an element.

| Tailwind               | Description              | Other |
| ---------------------- | ------------------------ | ----- |
| break-after-auto       | break-after: auto;       |       |
| break-after-avoid      | break-after: avoid;      |       |
| break-after-all        | break-after: all;        |       |
| break-after-avoid-page | break-after: avoid-page; |       |
| break-after-page       | break-after: page;       |       |
| break-after-left       | break-after: left;       |       |
| break-after-right      | break-after: right;      |       |
| break-after-column     | break-after: column;     |       |



### Break Before
Utilities for controlling how a column or page should break before an element.

| Tailwind                | Description               | Other |
| ----------------------- | ------------------------- | ----- |
| break-before-auto       | break-before: auto;       |       |
| break-before-avoid      | break-before: avoid;      |       |
| break-before-all        | break-before: all;        |       |
| break-before-avoid-page | break-before: avoid-page; |       |
| break-before-page       | break-before: page;       |       |
| break-before-left       | break-before: left;       |       |
| break-before-right      | break-before: right;      |       |
| break-before-column     | break-before: column;     |       |



### Break Inside
Utilities for controlling how a column or page should break within an element.

| Tailwind                | Description               | Other |
| ----------------------- | ------------------------- | ----- |
| break-inside-auto       | break-inside: auto;       |       |
| break-inside-avoid      | break-inside: avoid;      |       |
| break-inside-avoid-page | break-inside: avoid-page; |       |
| break-inside-column     | break-inside: column;     |       |



### Box Decoration Break
Utilities for controlling how element fragments should be rendered across multiple lines, columns, or pages.

| Tailwind         | Description                  | Other |
| ---------------- | ---------------------------- | ----- |
| decoration-slice | box-decoration-break: slice; |       |
| decoration-clone | box-decoration-break: clone; |       |



### Box Sizing
Sets how the total width and height of an element is calculated.

| Tailwind    | Description              | Other |
| ----------- | ------------------------ | ----- |
| box-border  | box-sizing: border-box;  |       |
| box-content | box-sizing: content-box; |       |



### Display
Sets the display box type of an element.

| Tailwind           | Description                  | Other |
| ------------------ | ---------------------------- | ----- |
| block              | display: block;              |       |
| inline-block       | display: inline-block;       |       |
| inline             | display: inline;             |       |
| flex               | display: flex;               |       |
| inline-flex        | display: inline-flex;        |       |
| table              | display: table;              |       |
| inline-table       | display: inline-table;       |       |
| table-caption      | display: table-caption;      |       |
| table-cell         | display: table-cell;         |       |
| table-column       | display: table-column;       |       |
| table-column-group | display: table-column-group; |       |
| table-footer-group | display: table-footer-group; |       |
| table-header-group | display: table-header-group; |       |
| table-row-group    | display: table-row-group;    |       |
| table-row          | display: table-row;          |       |
| flow-root          | display: flow-root;          |       |
| grid               | display: grid;               |       |
| inline-grid        | display: inline-grid;        |       |
| contents           | display: contents;           |       |
| list-item          | display: list-item;          |       |
| hidden             | display: none;               |       |



### Float
Sets an element's placement to a side of its container and allows content to wrap around it.

| Tailwind    | Description   | Other |
| ----------- | ------------- | ----- |
| float-right | float: right; |       |
| float-left  | float: left;  |       |
| float-none  | float: none;  |       |



### Clear
Sets whether an element is moved below preceding floated elements.

| Tailwind    | Description   | Other |
| ----------- | ------------- | ----- |
| clear-right | clear: right; |       |
| clear-left  | clear: left;  |       |
| clear-none  | clear: none;  |       |
| clear-both  | clear: both;  |       |


### Isolation
Sets whether an element is moved below preceding floated elements.

| Tailwind     | Description         | Other |
| ------------ | ------------------- | ----- |
| isolate      | isolation: isolate; |       |
| isolate-auto | isolation: auto;    |       |



### Object Fit
Sets how the content of a replaced element (img or video tag) should be resized.


| Tailwind          | Description             | Other |
| ----------------- | ----------------------- | ----- |
| object-contain    | object-fit: contain;    |       |
| object-cover      | object-fit: cover;      |       |
| object-fill       | object-fit: fill;       |       |
| object-none       | object-fit: none;       |       |
| object-scale-down | object-fit: scale-down; |       |


### Object Position
Sets the alignment of the selected replaced element.

| Tailwind            | Description                    | Other |
| ------------------- | ------------------------------ | ----- |
| object-bottom       | object-position: bottom;       |       |
| object-center       | object-position: center;       |       |
| object-left         | object-position: left;         |       |
| object-left-bottom  | object-position: left bottom;  |       |
| object-left-top     | object-position: left top;     |       |
| object-right        | object-position: right;        |       |
| object-right-bottom | object-position: right bottom; |       |
| object-right-top    | object-position: right top;    |       |
| object-top          | object-position: top;          |       |


### Overflow
Sets how to handle content that's too big for its container.

| Tailwind           | Description                        | Other |
| ------------------ | ---------------------------------- | ----- |
| overflow-auto      | overflow: auto;                    |       |
| overflow-x-auto    | overflow-x: auto;                  |       |
| overflow-y-auto    | overflow-y: auto;                  |       |
| overflow-hidden    | overflow: hidden;                  |       |
| overflow-x-hidden  | overflow-x: hidden;                |       |
| overflow-y-hidden  | overflow-y: hidden;                |       |
| overflow-visible   | overflow: visible;                 |       |
| overflow-x-visible | overflow-x: visible;               |       |
| overflow-y-visible | overflow-y: visible;               |       |
| overflow-scroll    | overflow: scroll;                  |       |
| overflow-x-scroll  | overflow-x: scroll;                |       |
| overflow-y-scroll  | overflow-y: scroll;                |       |
| scrolling-touch    | -webkit-overflow-scrolling: touch; |       |
| scrolling-auto     | -webkit-overflow-scrolling: auto;  |       |



### Overscroll Behavior
Sets of utilities for controlling how the browser behaves when reaching the boundary of a scrolling area.

| Tailwind             | Description                     | Other |
| -------------------- | ------------------------------- | ----- |
| overscroll-auto      | overscroll-behavior: auto;      |       |
| overscroll-y-auto    | overscroll-behavior-y: auto;    |       |
| overscroll-x-auto    | overscroll-behavior-x: auto;    |       |
| overscroll-contain   | overscroll-behavior: contain;   |       |
| overscroll-y-contain | overscroll-behavior-y: contain; |       |
| overscroll-x-contain | overscroll-behavior-x: contain; |       |
| overscroll-none      | overscroll-behavior: none;      |       |
| overscroll-y-none    | overscroll-behavior-y: none;    |       |
| overscroll-x-none    | overscroll-behavior-x: none;    |       |



### Position
Sets an element's position.

| Tailwind | Description         | Other |
| -------- | ------------------- | ----- |
| static   | position: static;   |       |
| fixed    | position: fixed;    |       |
| absolute | position: absolute; |       |
| relative | position: relative; |       |
| sticky   | position: sticky;   |       |



### Top / Right / Bottom / Left
Sets the placement of a positioned element.

| Tailwind      | Description                                                                   | Other |
| ------------- | ----------------------------------------------------------------------------- | ----- |
| inset-0       | top: 0; right: 0; bottom: 0; left: 0;                                         |       |
| -inset-0      | top: 0; right: 0; bottom: 0; left: 0;                                         |       |
| inset-y-0     | top: 0; bottom: 0;                                                            |       |
| -inset-y-0    | top: 0; bottom: 0;                                                            |       |
| inset-x-0     | right: 0; left: 0;                                                            |       |
| -inset-x-0    | right: 0; left: 0;                                                            |       |
| top-0         | top: 0;                                                                       |       |
| right-0       | right: 0;                                                                     |       |
| bottom-0      | bottom: 0;                                                                    |       |
| left-0        | left: 0;                                                                      |       |
| -top-0        | top: 0;                                                                       |       |
| -right-0      | right: 0;                                                                     |       |
| -bottom-0     | bottom: 0;                                                                    |       |
| -left-0       | left: 0;                                                                      |       |
| inset-0.5     | top: 0.125rem; right: 0.125rem; bottom: 0.125rem; left: 0.125rem;             |       |
| -inset-0.5    | top: -0.125rem; right: -0.125rem; bottom: -0.125rem; left: -0.125rem;         |       |
| inset-y-0.5   | top: 0.125rem; bottom: 0.125rem;                                              |       |
| -inset-y-0.5  | top: -0.125rem; bottom: -0.125rem;                                            |       |
| inset-x-0.5   | right: 0.125rem; left: 0.125rem;                                              |       |
| -inset-x-0.5  | right: -0.125rem; left: -0.125rem;                                            |       |
| top-0.5       | top: 0.125rem;                                                                |       |
| right-0.5     | right: 0.125rem;                                                              |       |
| bottom-0.5    | bottom: 0.125rem;                                                             |       |
| left-0.5      | left: 0.125rem;                                                               |       |
| -top-0.5      | top: -0.125rem;                                                               |       |
| -right-0.5    | right: -0.125rem;                                                             |       |
| -bottom-0.5   | bottom: -0.125rem;                                                            |       |
| -left-0.5     | left: -0.125rem;                                                              |       |
| inset-1       | top: 0.25rem; right: 0.25rem; bottom: 0.25rem; left: 0.25rem;                 |       |
| -inset-1      | top: -0.25rem; right: -0.25rem; bottom: -0.25rem; left: -0.25rem;             |       |
| inset-y-1     | top: 0.25rem; bottom: 0.25rem;                                                |       |
| -inset-y-1    | top: -0.25rem; bottom: -0.25rem;                                              |       |
| inset-x-1     | right: 0.25rem; left: 0.25rem;                                                |       |
| -inset-x-1    | right: -0.25rem; left: -0.25rem;                                              |       |
| top-1         | top: 0.25rem;                                                                 |       |
| right-1       | right: 0.25rem;                                                               |       |
| bottom-1      | bottom: 0.25rem;                                                              |       |
| left-1        | left: 0.25rem;                                                                |       |
| -top-1        | top: -0.25rem;                                                                |       |
| -right-1      | right: -0.25rem;                                                              |       |
| -bottom-1     | bottom: -0.25rem;                                                             |       |
| -left-1       | left: -0.25rem;                                                               |       |
| inset-1.5     | top: 0.375rem; right: 0.375rem; bottom: 0.375rem; left: 0.375rem;             |       |
| -inset-1.5    | top: -0.375rem; right: -0.375rem; bottom: -0.375rem; left: -0.375rem;         |       |
| inset-y-1.5   | top: 0.375rem; bottom: 0.375rem;                                              |       |
| -inset-y-1.5  | top: -0.375rem; bottom: -0.375rem;                                            |       |
| inset-x-1.5   | right: 0.375rem; left: 0.375rem;                                              |       |
| -inset-x-1.5  | right: -0.375rem; left: -0.375rem;                                            |       |
| top-1.5       | top: 0.375rem;                                                                |       |
| right-1.5     | right: 0.375rem;                                                              |       |
| bottom-1.5    | bottom: 0.375rem;                                                             |       |
| left-1.5      | left: 0.375rem;                                                               |       |
| -top-1.5      | top: -0.375rem;                                                               |       |
| -right-1.5    | right: -0.375rem;                                                             |       |
| -bottom-1.5   | bottom: -0.375rem;                                                            |       |
| -left-1.5     | left: -0.375rem;                                                              |       |
| inset-2       | top: 0.5rem; right: 0.5rem; bottom: 0.5rem; left: 0.5rem;                     |       |
| -inset-2      | top: -0.5rem; right: -0.5rem; bottom: -0.5rem; left: -0.5rem;                 |       |
| inset-y-2     | top: 0.5rem; bottom: 0.5rem;                                                  |       |
| -inset-y-2    | top: -0.5rem; bottom: -0.5rem;                                                |       |
| inset-x-2     | right: 0.5rem; left: 0.5rem;                                                  |       |
| -inset-x-2    | right: -0.5rem; left: -0.5rem;                                                |       |
| top-2         | top: 0.5rem;                                                                  |       |
| right-2       | right: 0.5rem;                                                                |       |
| bottom-2      | bottom: 0.5rem;                                                               |       |
| left-2        | left: 0.5rem;                                                                 |       |
| -top-2        | top: -0.5rem;                                                                 |       |
| -right-2      | right: -0.5rem;                                                               |       |
| -bottom-2     | bottom: -0.5rem;                                                              |       |
| -left-2       | left: -0.5rem;                                                                |       |
| inset-2.5     | top: 0.625rem; right: 0.625rem; bottom: 0.625rem; left: 0.625rem;             |       |
| -inset-2.5    | top: -0.625rem; right: -0.625rem; bottom: -0.625rem; left: -0.625rem;         |       |
| inset-y-2.5   | top: 0.625rem; bottom: 0.625rem;                                              |       |
| -inset-y-2.5  | top: -0.625rem; bottom: -0.625rem;                                            |       |
| inset-x-2.5   | right: 0.625rem; left: 0.625rem;                                              |       |
| -inset-x-2.5  | right: -0.625rem; left: -0.625rem;                                            |       |
| top-2.5       | top: 0.625rem;                                                                |       |
| right-2.5     | right: 0.625rem;                                                              |       |
| bottom-2.5    | bottom: 0.625rem;                                                             |       |
| left-2.5      | left: 0.625rem;                                                               |       |
| -top-2.5      | top: -0.625rem;                                                               |       |
| -right-2.5    | right: -0.625rem;                                                             |       |
| -bottom-2.5   | bottom: -0.625rem;                                                            |       |
| -left-2.5     | left: -0.625rem;                                                              |       |
| inset-3       | top: 0.75rem; right: 0.75rem; bottom: 0.75rem; left: 0.75rem;                 |       |
| -inset-3      | top: -0.75rem; right: -0.75rem; bottom: -0.75rem; left: -0.75rem;             |       |
| inset-y-3     | top: 0.75rem; bottom: 0.75rem;                                                |       |
| -inset-y-3    | top: -0.75rem; bottom: -0.75rem;                                              |       |
| inset-x-3     | right: 0.75rem; left: 0.75rem;                                                |       |
| -inset-x-3    | right: -0.75rem; left: -0.75rem;                                              |       |
| top-3         | top: 0.75rem;                                                                 |       |
| right-3       | right: 0.75rem;                                                               |       |
| bottom-3      | bottom: 0.75rem;                                                              |       |
| left-3        | left: 0.75rem;                                                                |       |
| -top-3        | top: -0.75rem;                                                                |       |
| -right-3      | right: -0.75rem;                                                              |       |
| -bottom-3     | bottom: -0.75rem;                                                             |       |
| -left-3       | left: -0.75rem;                                                               |       |
| inset-3.5     | top: 0.875rem; right: 0.875rem; bottom: 0.875rem; left: 0.875rem;             |       |
| -inset-3.5    | top: -0.875rem; right: -0.875rem; bottom: -0.875rem; left: -0.875rem;         |       |
| inset-y-3.5   | top: 0.875rem; bottom: 0.875rem;                                              |       |
| -inset-y-3.5  | top: -0.875rem; bottom: -0.875rem;                                            |       |
| inset-x-3.5   | right: 0.875rem; left: 0.875rem;                                              |       |
| -inset-x-3.5  | right: -0.875rem; left: -0.875rem;                                            |       |
| top-3.5       | top: 0.875rem;                                                                |       |
| right-3.5     | right: 0.875rem;                                                              |       |
| bottom-3.5    | bottom: 0.875rem;                                                             |       |
| left-3.5      | left: 0.875rem;                                                               |       |
| -top-3.5      | top: -0.875rem;                                                               |       |
| -right-3.5    | right: -0.875rem;                                                             |       |
| -bottom-3.5   | bottom: -0.875rem;                                                            |       |
| -left-3.5     | left: -0.875rem;                                                              |       |
| inset-4       | top: 1rem; right: 1rem; bottom: 1rem; left: 1rem;                             |       |
| -inset-4      | top: -1rem; right: -1rem; bottom: -1rem; left: -1rem;                         |       |
| inset-y-4     | top: 1rem; bottom: 1rem;                                                      |       |
| -inset-y-4    | top: -1rem; bottom: -1rem;                                                    |       |
| inset-x-4     | right: 1rem; left: 1rem;                                                      |       |
| -inset-x-4    | right: -1rem; left: -1rem;                                                    |       |
| top-4         | top: 1rem;                                                                    |       |
| right-4       | right: 1rem;                                                                  |       |
| bottom-4      | bottom: 1rem;                                                                 |       |
| left-4        | left: 1rem;                                                                   |       |
| -top-4        | top: -1rem;                                                                   |       |
| -right-4      | right: -1rem;                                                                 |       |
| -bottom-4     | bottom: -1rem;                                                                |       |
| -left-4       | left: -1rem;                                                                  |       |
| inset-5       | top: 1.25rem; right: 1.25rem; bottom: 1.25rem; left: 1.25rem;                 |       |
| -inset-5      | top: -1.25rem; right: -1.25rem; bottom: -1.25rem; left: -1.25rem;             |       |
| inset-y-5     | top: 1.25rem; bottom: 1.25rem;                                                |       |
| -inset-y-5    | top: -1.25rem; bottom: -1.25rem;                                              |       |
| inset-x-5     | right: 1.25rem; left: 1.25rem;                                                |       |
| -inset-x-5    | right: -1.25rem; left: -1.25rem;                                              |       |
| top-5         | top: 1.25rem;                                                                 |       |
| right-5       | right: 1.25rem;                                                               |       |
| bottom-5      | bottom: 1.25rem;                                                              |       |
| left-5        | left: 1.25rem;                                                                |       |
| -top-5        | top: -1.25rem;                                                                |       |
| -right-5      | right: -1.25rem;                                                              |       |
| -bottom-5     | bottom: -1.25rem;                                                             |       |
| -left-5       | left: -1.25rem;                                                               |       |
| inset-6       | top: 1.5rem; right: 1.5rem; bottom: 1.5rem; left: 1.5rem;                     |       |
| -inset-6      | top: -1.5rem; right: -1.5rem; bottom: -1.5rem; left: -1.5rem;                 |       |
| inset-y-6     | top: 1.5rem; bottom: 1.5rem;                                                  |       |
| -inset-y-6    | top: -1.5rem; bottom: -1.5rem;                                                |       |
| inset-x-6     | right: 1.5rem; left: 1.5rem;                                                  |       |
| -inset-x-6    | right: -1.5rem; left: -1.5rem;                                                |       |
| top-6         | top: 1.5rem;                                                                  |       |
| right-6       | right: 1.5rem;                                                                |       |
| bottom-6      | bottom: 1.5rem;                                                               |       |
| left-6        | left: 1.5rem;                                                                 |       |
| -top-6        | top: -1.5rem;                                                                 |       |
| -right-6      | right: -1.5rem;                                                               |       |
| -bottom-6     | bottom: -1.5rem;                                                              |       |
| -left-6       | left: -1.5rem;                                                                |       |
| inset-7       | top: 1.75rem; right: 1.75rem; bottom: 1.75rem; left: 1.75rem;                 |       |
| -inset-7      | top: -1.75rem; right: -1.75rem; bottom: -1.75rem; left: -1.75rem;             |       |
| inset-y-7     | top: 1.75rem; bottom: 1.75rem;                                                |       |
| -inset-y-7    | top: -1.75rem; bottom: -1.75rem;                                              |       |
| inset-x-7     | right: 1.75rem; left: 1.75rem;                                                |       |
| -inset-x-7    | right: -1.75rem; left: -1.75rem;                                              |       |
| top-7         | top: 1.75rem;                                                                 |       |
| right-7       | right: 1.75rem;                                                               |       |
| bottom-7      | bottom: 1.75rem;                                                              |       |
| left-7        | left: 1.75rem;                                                                |       |
| -top-7        | top: -1.75rem;                                                                |       |
| -right-7      | right: -1.75rem;                                                              |       |
| -bottom-7     | bottom: -1.75rem;                                                             |       |
| -left-7       | left: -1.75rem;                                                               |       |
| inset-8       | top: 2rem; right: 2rem; bottom: 2rem; left: 2rem;                             |       |
| -inset-8      | top: -2rem; right: -2rem; bottom: -2rem; left: -2rem;                         |       |
| inset-y-8     | top: 2rem; bottom: 2rem;                                                      |       |
| -inset-y-8    | top: -2rem; bottom: -2rem;                                                    |       |
| inset-x-8     | right: 2rem; left: 2rem;                                                      |       |
| -inset-x-8    | right: -2rem; left: -2rem;                                                    |       |
| top-8         | top: 2rem;                                                                    |       |
| right-8       | right: 2rem;                                                                  |       |
| bottom-8      | bottom: 2rem;                                                                 |       |
| left-8        | left: 2rem;                                                                   |       |
| -top-8        | top: -2rem;                                                                   |       |
| -right-8      | right: -2rem;                                                                 |       |
| -bottom-8     | bottom: -2rem;                                                                |       |
| -left-8       | left: -2rem;                                                                  |       |
| inset-9       | top: 2.25rem; right: 2.25rem; bottom: 2.25rem; left: 2.25rem;                 |       |
| -inset-9      | top: -2.25rem; right: -2.25rem; bottom: -2.25rem; left: -2.25rem;             |       |
| inset-y-9     | top: 2.25rem; bottom: 2.25rem;                                                |       |
| -inset-y-9    | top: -2.25rem; bottom: -2.25rem;                                              |       |
| inset-x-9     | right: 2.25rem; left: 2.25rem;                                                |       |
| -inset-x-9    | right: -2.25rem; left: -2.25rem;                                              |       |
| top-9         | top: 2.25rem;                                                                 |       |
| right-9       | right: 2.25rem;                                                               |       |
| bottom-9      | bottom: 2.25rem;                                                              |       |
| left-9        | left: 2.25rem;                                                                |       |
| -top-9        | top: -2.25rem;                                                                |       |
| -right-9      | right: -2.25rem;                                                              |       |
| -bottom-9     | bottom: -2.25rem;                                                             |       |
| -left-9       | left: -2.25rem;                                                               |       |
| inset-10      | top: 2.5rem; right: 2.5rem; bottom: 2.5rem; left: 2.5rem;                     |       |
| -inset-10     | top: -2.5rem; right: -2.5rem; bottom: -2.5rem; left: -2.5rem;                 |       |
| inset-y-10    | top: 2.5rem; bottom: 2.5rem;                                                  |       |
| -inset-y-10   | top: -2.5rem; bottom: -2.5rem;                                                |       |
| inset-x-10    | right: 2.5rem; left: 2.5rem;                                                  |       |
| -inset-x-10   | right: -2.5rem; left: -2.5rem;                                                |       |
| top-10        | top: 2.5rem;                                                                  |       |
| right-10      | right: 2.5rem;                                                                |       |
| bottom-10     | bottom: 2.5rem;                                                               |       |
| left-10       | left: 2.5rem;                                                                 |       |
| -top-10       | top: -2.5rem;                                                                 |       |
| -right-10     | right: -2.5rem;                                                               |       |
| -bottom-10    | bottom: -2.5rem;                                                              |       |
| -left-10      | left: -2.5rem;                                                                |       |
| inset-11      | top: 2.75rem; right: 2.75rem; bottom: 2.75rem; left: 2.75rem;                 |       |
| -inset-11     | top: -2.75rem; right: -2.75rem; bottom: -2.75rem; left: -2.75rem;             |       |
| inset-y-11    | top: 2.75rem; bottom: 2.75rem;                                                |       |
| -inset-y-11   | top: -2.75rem; bottom: -2.75rem;                                              |       |
| inset-x-11    | right: 2.75rem; left: 2.75rem;                                                |       |
| -inset-x-11   | right: -2.75rem; left: -2.75rem;                                              |       |
| top-11        | top: 2.75rem;                                                                 |       |
| right-11      | right: 2.75rem;                                                               |       |
| bottom-11     | bottom: 2.75rem;                                                              |       |
| left-11       | left: 2.75rem;                                                                |       |
| -top-11       | top: -2.75rem;                                                                |       |
| -right-11     | right: -2.75rem;                                                              |       |
| -bottom-11    | bottom: -2.75rem;                                                             |       |
| -left-11      | left: -2.75rem;                                                               |       |
| inset-12      | top: 3rem; right: 3rem; bottom: 3rem; left: 3rem;                             |       |
| -inset-12     | top: -3rem; right: -3rem; bottom: -3rem; left: -3rem;                         |       |
| inset-y-12    | top: 3rem; bottom: 3rem;                                                      |       |
| -inset-y-12   | top: -3rem; bottom: -3rem;                                                    |       |
| inset-x-12    | right: 3rem; left: 3rem;                                                      |       |
| -inset-x-12   | right: -3rem; left: -3rem;                                                    |       |
| top-12        | top: 3rem;                                                                    |       |
| right-12      | right: 3rem;                                                                  |       |
| bottom-12     | bottom: 3rem;                                                                 |       |
| left-12       | left: 3rem;                                                                   |       |
| -top-12       | top: -3rem;                                                                   |       |
| -right-12     | right: -3rem;                                                                 |       |
| -bottom-12    | bottom: -3rem;                                                                |       |
| -left-12      | left: -3rem;                                                                  |       |
| inset-14      | top: 3.5rem; right: 3.5rem; bottom: 3.5rem; left: 3.5rem;                     |       |
| -inset-14     | top: -3.5rem; right: -3.5rem; bottom: -3.5rem; left: -3.5rem;                 |       |
| inset-y-14    | top: 3.5rem; bottom: 3.5rem;                                                  |       |
| -inset-y-14   | top: -3.5rem; bottom: -3.5rem;                                                |       |
| inset-x-14    | right: 3.5rem; left: 3.5rem;                                                  |       |
| -inset-x-14   | right: -3.5rem; left: -3.5rem;                                                |       |
| top-14        | top: 3.5rem;                                                                  |       |
| right-14      | right: 3.5rem;                                                                |       |
| bottom-14     | bottom: 3.5rem;                                                               |       |
| left-14       | left: 3.5rem;                                                                 |       |
| -top-14       | top: -3.5rem;                                                                 |       |
| -right-14     | right: -3.5rem;                                                               |       |
| -bottom-14    | bottom: -3.5rem;                                                              |       |
| -left-14      | left: -3.5rem;                                                                |       |
| inset-16      | top: 4rem; right: 4rem; bottom: 4rem; left: 4rem;                             |       |
| -inset-16     | top: -4rem; right: -4rem; bottom: -4rem; left: -4rem;                         |       |
| inset-y-16    | top: 4rem; bottom: 4rem;                                                      |       |
| -inset-y-16   | top: -4rem; bottom: -4rem;                                                    |       |
| inset-x-16    | right: 4rem; left: 4rem;                                                      |       |
| -inset-x-16   | right: -4rem; left: -4rem;                                                    |       |
| top-16        | top: 4rem;                                                                    |       |
| right-16      | right: 4rem;                                                                  |       |
| bottom-16     | bottom: 4rem;                                                                 |       |
| left-16       | left: 4rem;                                                                   |       |
| -top-16       | top: -4rem;                                                                   |       |
| -right-16     | right: -4rem;                                                                 |       |
| -bottom-16    | bottom: -4rem;                                                                |       |
| -left-16      | left: -4rem;                                                                  |       |
| inset-20      | top: 5rem; right: 5rem; bottom: 5rem; left: 5rem;                             |       |
| -inset-20     | top: -5rem; right: -5rem; bottom: -5rem; left: -5rem;                         |       |
| inset-y-20    | top: 5rem; bottom: 5rem;                                                      |       |
| -inset-y-20   | top: -5rem; bottom: -5rem;                                                    |       |
| inset-x-20    | right: 5rem; left: 5rem;                                                      |       |
| -inset-x-20   | right: -5rem; left: -5rem;                                                    |       |
| top-20        | top: 5rem;                                                                    |       |
| right-20      | right: 5rem;                                                                  |       |
| bottom-20     | bottom: 5rem;                                                                 |       |
| left-20       | left: 5rem;                                                                   |       |
| -top-20       | top: -5rem;                                                                   |       |
| -right-20     | right: -5rem;                                                                 |       |
| -bottom-20    | bottom: -5rem;                                                                |       |
| -left-20      | left: -5rem;                                                                  |       |
| inset-24      | top: 6rem; right: 6rem; bottom: 6rem; left: 6rem;                             |       |
| -inset-24     | top: -6rem; right: -6rem; bottom: -6rem; left: -6rem;                         |       |
| inset-y-24    | top: 6rem; bottom: 6rem;                                                      |       |
| -inset-y-24   | top: -6rem; bottom: -6rem;                                                    |       |
| inset-x-24    | right: 6rem; left: 6rem;                                                      |       |
| -inset-x-24   | right: -6rem; left: -6rem;                                                    |       |
| top-24        | top: 6rem;                                                                    |       |
| right-24      | right: 6rem;                                                                  |       |
| bottom-24     | bottom: 6rem;                                                                 |       |
| left-24       | left: 6rem;                                                                   |       |
| -top-24       | top: -6rem;                                                                   |       |
| -right-24     | right: -6rem;                                                                 |       |
| -bottom-24    | bottom: -6rem;                                                                |       |
| -left-24      | left: -6rem;                                                                  |       |
| inset-28      | top: 7rem; right: 7rem; bottom: 7rem; left: 7rem;                             |       |
| -inset-28     | top: -7rem; right: -7rem; bottom: -7rem; left: -7rem;                         |       |
| inset-y-28    | top: 7rem; bottom: 7rem;                                                      |       |
| -inset-y-28   | top: -7rem; bottom: -7rem;                                                    |       |
| inset-x-28    | right: 7rem; left: 7rem;                                                      |       |
| -inset-x-28   | right: -7rem; left: -7rem;                                                    |       |
| top-28        | top: 7rem;                                                                    |       |
| right-28      | right: 7rem;                                                                  |       |
| bottom-28     | bottom: 7rem;                                                                 |       |
| left-28       | left: 7rem;                                                                   |       |
| -top-28       | top: -7rem;                                                                   |       |
| -right-28     | right: -7rem;                                                                 |       |
| -bottom-28    | bottom: -7rem;                                                                |       |
| -left-28      | left: -7rem;                                                                  |       |
| inset-32      | top: 8rem; right: 8rem; bottom: 8rem; left: 8rem;                             |       |
| -inset-32     | top: -8rem; right: -8rem; bottom: -8rem; left: -8rem;                         |       |
| inset-y-32    | top: 8rem; bottom: 8rem;                                                      |       |
| -inset-y-32   | top: -8rem; bottom: -8rem;                                                    |       |
| inset-x-32    | right: 8rem; left: 8rem;                                                      |       |
| -inset-x-32   | right: -8rem; left: -8rem;                                                    |       |
| top-32        | top: 8rem;                                                                    |       |
| right-32      | right: 8rem;                                                                  |       |
| bottom-32     | bottom: 8rem;                                                                 |       |
| left-32       | left: 8rem;                                                                   |       |
| -top-32       | top: -8rem;                                                                   |       |
| -right-32     | right: -8rem;                                                                 |       |
| -bottom-32    | bottom: -8rem;                                                                |       |
| -left-32      | left: -8rem;                                                                  |       |
| inset-36      | top: 9rem; right: 9rem; bottom: 9rem; left: 9rem;                             |       |
| -inset-36     | top: -9rem; right: -9rem; bottom: -9rem; left: -9rem;                         |       |
| inset-y-36    | top: 9rem; bottom: 9rem;                                                      |       |
| -inset-y-36   | top: -9rem; bottom: -9rem;                                                    |       |
| inset-x-36    | right: 9rem; left: 9rem;                                                      |       |
| -inset-x-36   | right: -9rem; left: -9rem;                                                    |       |
| top-36        | top: 9rem;                                                                    |       |
| right-36      | right: 9rem;                                                                  |       |
| bottom-36     | bottom: 9rem;                                                                 |       |
| left-36       | left: 9rem;                                                                   |       |
| -top-36       | top: -9rem;                                                                   |       |
| -right-36     | right: -9rem;                                                                 |       |
| -bottom-36    | bottom: -9rem;                                                                |       |
| -left-36      | left: -9rem;                                                                  |       |
| inset-40      | top: 10rem; right: 10rem; bottom: 10rem; left: 10rem;                         |       |
| -inset-40     | top: -10rem; right: -10rem; bottom: -10rem; left: -10rem;                     |       |
| inset-y-40    | top: 10rem; bottom: 10rem;                                                    |       |
| -inset-y-40   | top: -10rem; bottom: -10rem;                                                  |       |
| inset-x-40    | right: 10rem; left: 10rem;                                                    |       |
| -inset-x-40   | right: -10rem; left: -10rem;                                                  |       |
| top-40        | top: 10rem;                                                                   |       |
| right-40      | right: 10rem;                                                                 |       |
| bottom-40     | bottom: 10rem;                                                                |       |
| left-40       | left: 10rem;                                                                  |       |
| -top-40       | top: -10rem;                                                                  |       |
| -right-40     | right: -10rem;                                                                |       |
| -bottom-40    | bottom: -10rem;                                                               |       |
| -left-40      | left: -10rem;                                                                 |       |
| inset-44      | top: 11rem; right: 11rem; bottom: 11rem; left: 11rem;                         |       |
| -inset-44     | top: -11rem; right: -11rem; bottom: -11rem; left: -11rem;                     |       |
| inset-y-44    | top: 11rem; bottom: 11rem;                                                    |       |
| -inset-y-44   | top: -11rem; bottom: -11rem;                                                  |       |
| inset-x-44    | right: 11rem; left: 11rem;                                                    |       |
| -inset-x-44   | right: -11rem; left: -11rem;                                                  |       |
| top-44        | top: 11rem;                                                                   |       |
| right-44      | right: 11rem;                                                                 |       |
| bottom-44     | bottom: 11rem;                                                                |       |
| left-44       | left: 11rem;                                                                  |       |
| -top-44       | top: -11rem;                                                                  |       |
| -right-44     | right: -11rem;                                                                |       |
| -bottom-44    | bottom: -11rem;                                                               |       |
| -left-44      | left: -11rem;                                                                 |       |
| inset-48      | top: 12rem; right: 12rem; bottom: 12rem; left: 12rem;                         |       |
| -inset-48     | top: -12rem; right: -12rem; bottom: -12rem; left: -12rem;                     |       |
| inset-y-48    | top: 12rem; bottom: 12rem;                                                    |       |
| -inset-y-48   | top: -12rem; bottom: -12rem;                                                  |       |
| inset-x-48    | right: 12rem; left: 12rem;                                                    |       |
| -inset-x-48   | right: -12rem; left: -12rem;                                                  |       |
| top-48        | top: 12rem;                                                                   |       |
| right-48      | right: 12rem;                                                                 |       |
| bottom-48     | bottom: 12rem;                                                                |       |
| left-48       | left: 12rem;                                                                  |       |
| -top-48       | top: -12rem;                                                                  |       |
| -right-48     | right: -12rem;                                                                |       |
| -bottom-48    | bottom: -12rem;                                                               |       |
| -left-48      | left: -12rem;                                                                 |       |
| inset-52      | top: 13rem; right: 13rem; bottom: 13rem; left: 13rem;                         |       |
| -inset-52     | top: -13rem; right: -13rem; bottom: -13rem; left: -13rem;                     |       |
| inset-y-52    | top: 13rem; bottom: 13rem;                                                    |       |
| -inset-y-52   | top: -13rem; bottom: -13rem;                                                  |       |
| inset-x-52    | right: 13rem; left: 13rem;                                                    |       |
| -inset-x-52   | right: -13rem; left: -13rem;                                                  |       |
| top-52        | top: 13rem;                                                                   |       |
| right-52      | right: 13rem;                                                                 |       |
| bottom-52     | bottom: 13rem;                                                                |       |
| left-52       | left: 13rem;                                                                  |       |
| -top-52       | top: -13rem;                                                                  |       |
| -right-52     | right: -13rem;                                                                |       |
| -bottom-52    | bottom: -13rem;                                                               |       |
| -left-52      | left: -13rem;                                                                 |       |
| inset-56      | top: 14rem; right: 14rem; bottom: 14rem; left: 14rem;                         |       |
| -inset-56     | top: -14rem; right: -14rem; bottom: -14rem; left: -14rem;                     |       |
| inset-y-56    | top: 14rem; bottom: 14rem;                                                    |       |
| -inset-y-56   | top: -14rem; bottom: -14rem;                                                  |       |
| inset-x-56    | right: 14rem; left: 14rem;                                                    |       |
| -inset-x-56   | right: -14rem; left: -14rem;                                                  |       |
| top-56        | top: 14rem;                                                                   |       |
| right-56      | right: 14rem;                                                                 |       |
| bottom-56     | bottom: 14rem;                                                                |       |
| left-56       | left: 14rem;                                                                  |       |
| -top-56       | top: -14rem;                                                                  |       |
| -right-56     | right: -14rem;                                                                |       |
| -bottom-56    | bottom: -14rem;                                                               |       |
| -left-56      | left: -14rem;                                                                 |       |
| inset-60      | top: 15rem; right: 15rem; bottom: 15rem; left: 15rem;                         |       |
| -inset-60     | top: -15rem; right: -15rem; bottom: -15rem; left: -15rem;                     |       |
| inset-y-60    | top: 15rem; bottom: 15rem;                                                    |       |
| -inset-y-60   | top: -15rem; bottom: -15rem;                                                  |       |
| inset-x-60    | right: 15rem; left: 15rem;                                                    |       |
| -inset-x-60   | right: -15rem; left: -15rem;                                                  |       |
| top-60        | top: 15rem;                                                                   |       |
| right-60      | right: 15rem;                                                                 |       |
| bottom-60     | bottom: 15rem;                                                                |       |
| left-60       | left: 15rem;                                                                  |       |
| -top-60       | top: -15rem;                                                                  |       |
| -right-60     | right: -15rem;                                                                |       |
| -bottom-60    | bottom: -15rem;                                                               |       |
| -left-60      | left: -15rem;                                                                 |       |
| inset-64      | top: 16rem; right: 16rem; bottom: 16rem; left: 16rem;                         |       |
| -inset-64     | top: -16rem; right: -16rem; bottom: -16rem; left: -16rem;                     |       |
| inset-y-64    | top: 16rem; bottom: 16rem;                                                    |       |
| -inset-y-64   | top: -16rem; bottom: -16rem;                                                  |       |
| inset-x-64    | right: 16rem; left: 16rem;                                                    |       |
| -inset-x-64   | right: -16rem; left: -16rem;                                                  |       |
| top-64        | top: 16rem;                                                                   |       |
| right-64      | right: 16rem;                                                                 |       |
| bottom-64     | bottom: 16rem;                                                                |       |
| left-64       | left: 16rem;                                                                  |       |
| -top-64       | top: -16rem;                                                                  |       |
| -right-64     | right: -16rem;                                                                |       |
| -bottom-64    | bottom: -16rem;                                                               |       |
| -left-64      | left: -16rem;                                                                 |       |
| inset-72      | top: 18rem; right: 18rem; bottom: 18rem; left: 18rem;                         |       |
| -inset-72     | top: -18rem; right: -18rem; bottom: -18rem; left: -18rem;                     |       |
| inset-y-72    | top: 18rem; bottom: 18rem;                                                    |       |
| -inset-y-72   | top: -18rem; bottom: -18rem;                                                  |       |
| inset-x-72    | right: 18rem; left: 18rem;                                                    |       |
| -inset-x-72   | right: -18rem; left: -18rem;                                                  |       |
| top-72        | top: 18rem;                                                                   |       |
| right-72      | right: 18rem;                                                                 |       |
| bottom-72     | bottom: 18rem;                                                                |       |
| left-72       | left: 18rem;                                                                  |       |
| -top-72       | top: -18rem;                                                                  |       |
| -right-72     | right: -18rem;                                                                |       |
| -bottom-72    | bottom: -18rem;                                                               |       |
| -left-72      | left: -18rem;                                                                 |       |
| inset-80      | top: 20; right: 20; bottom: 20; left: 20;                                     |       |
| -inset-80     | top: -20; right: -20; bottom: -20; left: -20;                                 |       |
| inset-y-80    | top: 20; bottom: 20;                                                          |       |
| -inset-y-80   | top: -20; bottom: -20;                                                        |       |
| inset-x-80    | right: 20; left: 20;                                                          |       |
| -inset-x-80   | right: -20; left: -20;                                                        |       |
| top-80        | top: 20;                                                                      |       |
| right-80      | right: 20;                                                                    |       |
| bottom-80     | bottom: 20;                                                                   |       |
| left-80       | left: 20;                                                                     |       |
| -top-80       | top: -20;                                                                     |       |
| -right-80     | right: -20;                                                                   |       |
| -bottom-80    | bottom: -20;                                                                  |       |
| -left-80      | left: -20rem;                                                                 |       |
| inset-96      | top: 24rem; right: 24rem; bottom: 24rem; left: 24rem;                         |       |
| -inset-96     | top: -24rem; right: -24rem; bottom: -24rem; left: -24rem;                     |       |
| inset-y-96    | top: 24rem; bottom: 24rem;                                                    |       |
| -inset-y-96   | top: -24rem; bottom: -24rem;                                                  |       |
| inset-x-96    | right: 24rem; left: 24rem;                                                    |       |
| -inset-x-96   | right: -24rem; left: -24rem;                                                  |       |
| top-96        | top: 24rem;                                                                   |       |
| right-96      | right: 24rem;                                                                 |       |
| bottom-96     | bottom: 24rem;                                                                |       |
| left-96       | left: 24rem;                                                                  |       |
| -top-96       | top: -24rem;                                                                  |       |
| -right-96     | right: -24rem;                                                                |       |
| -bottom-96    | bottom: -24rem;                                                               |       |
| -left-96      | left: -24rem;                                                                 |       |
| inset-auto    | top: auto; right: auto; bottom: auto; left: auto;                             |       |
| inset-y-auto  | top: auto; bottom: auto;                                                      |       |
| inset-x-auto  | right: auto; left: auto;                                                      |       |
| top-auto      | top: auto;                                                                    |       |
| right-auto    | right: auto;                                                                  |       |
| bottom-auto   | bottom: auto;                                                                 |       |
| left-auto     | left: auto;                                                                   |       |
| inset-1/2     | top: 50%; right: 50%; bottom: 50%; left: 50%;                                 |       |
| inset-2/3     | top: 66.666667%; right: 66.666667%; bottom: 66.666667%; left: 66.666667%;     |       |
| inset-1/4     | top: 25%; right: 25%; bottom: 25%; left: 25%;                                 |       |
| inset-3/4     | top: 75%; right: 75%; bottom: 75%; left: 75%;                                 |       |
| inset-full    | top: 100%; right: 100%; bottom: 100%; left: 100%;                             |       |
| -inset-1/2    | top: -50%; right: -50%; bottom: -50%; left: -50%;                             |       |
| -inset-2/3    | top: -66.666667%; right: -66.666667%; bottom: -66.666667%; left: -66.666667%; |       |
| -inset-1/4    | top: -25%; right: -25%; bottom: -25%; left: -25%;                             |       |
| -inset-3/4    | top: -75%; right: -75%; bottom: -75%; left: -75%;                             |       |
| -inset-full   | top: -100%; right: -100%; bottom: -100%; left: -100%;                         |       |
| inset-x-1/2   | right: 50%; left: 50%;                                                        |       |
| inset-x-2/3   | right: 66.666667%; left: 66.666667%;                                          |       |
| inset-x-1/4   | right: 25%; left: 25%;                                                        |       |
| inset-x-3/4   | right: 75%; left: 75%;                                                        |       |
| inset-x-full  | right: 100%; left: 100%;                                                      |       |
| -inset-x-1/2  | right: -50%; left: -50%;                                                      |       |
| -inset-x-2/3  | right: -66.666667%; left: -66.666667%;                                        |       |
| -inset-x-1/4  | right: -25%; left: -25%;                                                      |       |
| -inset-x-3/4  | right: -75%; left: -75%;                                                      |       |
| -inset-x-full | right: -100%; left: -100%;                                                    |       |
| inset-y-1/2   | top: 50%; bottom: 50%;                                                        |       |
| inset-y-2/3   | top: 66.666667%; bottom: 66.666667%;                                          |       |
| inset-y-1/4   | top: 25%; bottom: 25%;                                                        |       |
| inset-y-3/4   | top: 75%; bottom: 75%;                                                        |       |
| inset-y-full  | top: 100%; bottom: 100%;                                                      |       |
| -inset-y-1/2  | top: -50%; bottom: -50%;                                                      |       |
| -inset-y-2/3  | top: -66.666667%; bottom: -66.666667%;                                        |       |
| -inset-y-1/4  | top: -25%; bottom: -25%;                                                      |       |
| -inset-y-3/4  | top: -75%; bottom: -75%;                                                      |       |
| -inset-y-full | top: -100%; bottom: -100%;                                                    |       |
| top-1/2       | top: 50%;                                                                     |       |
| top-2/3       | top: 66.666667%;                                                              |       |
| top-1/4       | top: 25%;                                                                     |       |
| top-3/4       | top: 75%;                                                                     |       |
| top-full      | top: 100%;                                                                    |       |
| -top-1/2      | top: -50%;                                                                    |       |
| -top-2/3      | top: -66.666667%;                                                             |       |
| -top-1/4      | top: -25%;                                                                    |       |
| -top-3/4      | top: -75%;                                                                    |       |
| -top-full     | top: -100%;                                                                   |       |
| right-1/2     | right: 50%;                                                                   |       |
| right-2/3     | right: 66.666667%;                                                            |       |
| right-1/4     | right: 25%;                                                                   |       |
| right-3/4     | right: 75%;                                                                   |       |
| right-full    | right: 100%;                                                                  |       |
| -right-1/2    | right: -50%;                                                                  |       |
| -right-2/3    | right: -66.666667%;                                                           |       |
| -right-1/4    | right: -25%;                                                                  |       |
| -right-3/4    | right: -75%;                                                                  |       |
| -right-full   | right: -100%;                                                                 |       |
| bottom-1/2    | bottom: 50%;                                                                  |       |
| bottom-2/3    | bottom: 66.666667%;                                                           |       |
| bottom-1/4    | bottom: 25%;                                                                  |       |
| bottom-3/4    | bottom: 75%;                                                                  |       |
| bottom-full   | bottom: 100%;                                                                 |       |
| -bottom-1/2   | bottom: -50%;                                                                 |       |
| -bottom-2/3   | bottom: -66.666667%;                                                          |       |
| -bottom-1/4   | bottom: -25%;                                                                 |       |
| -bottom-3/4   | bottom: -75%;                                                                 |       |
| -bottom-full  | bottom: -100%;                                                                |       |
| left-1/2      | left: 50%;                                                                    |       |
| left-2/3      | left: 66.666667%;                                                             |       |
| left-1/4      | left: 25%;                                                                    |       |
| left-3/4      | left: 75%;                                                                    |       |
| left-full     | left: 100%;                                                                   |       |
| -left-1/2     | left: -50%;                                                                   |       |
| -left-2/3     | left: -66.666667%;                                                            |       |
| -left-1/4     | left: -25%;                                                                   |       |
| -left-3/4     | left: -75%;                                                                   |       |
| -left-full    | left: -100%;                                                                  |       |


---










### Visibility
Show or hide without affecting the layout of the document.

| Tailwind  | Description          | Other |
| --------- | -------------------- | ----- |
| visible   | visibility: visible; |       |
| invisible | visibility: hidden;  |       |


### Z-index
Sets the z-order ("stack order") of a positioned element.

| Tailwind | Description    | Other |
| -------- | -------------- | ----- |
| z-0      | z-index: 0;    |       |
| z-10     | z-index: 10;   |       |
| z-20     | z-index: 20;   |       |
| z-30     | z-index: 30;   |       |
| z-40     | z-index: 40;   |       |
| z-50     | z-index: 50;   |       |
| z-auto   | z-index: auto; |       |

---

## Sizing 

### Width

| Tailwind | Description         | Other |
| -------- | ------------------- | ----- |
| w-0      | width: 0;           |       |
| w-0.5    | width: 0.125rem;    | 2px   |
| w-1      | width: 0.25rem;     | 4px   |
| w-1.5    | width: 0.375rem;    | 6px   |
| w-2      | width: 0.5rem;      | 8px   |
| w-2.5    | width: 0.625rem;    | 10px  |
| w-3      | width: 0.75rem;     | 12px  |
| w-3.5    | width: 0.875rem;    | 14px  |
| w-4      | width: 1rem;        | 16px  |
| w-5      | width: 1.25rem;     | 20px  |
| w-6      | width: 1.5rem;      | 24px  |
| w-8      | width: 2rem;        | 32px  |
| w-10     | width: 2.5rem;      | 40px  |
| w-11     | width: 2.75rem;     | 44px  |
| w-12     | width: 3rem;        | 48px  |
| w-14     | width: 3.5rem;      | 56px  |
| w-16     | width: 4rem;        | 64px  |
| w-20     | width: 5rem;        | 80px  |
| w-24     | width: 6rem;        | 96px  |
| w-28     | width: 7rem;        | 112px |
| w-32     | width: 8rem;        | 128px |
| w-36     | width: 9rem;        | 144px |
| w-40     | width: 10rem;       | 160px |
| w-44     | width: 11rem;       | 176px |
| w-48     | width: 12rem;       | 192px |
| w-52     | width: 13rem;       | 208px |
| w-56     | width: 14rem;       | 224px |
| w-64     | width: 16rem;       | 256px |
| w-72     | width: 18rem;       | 288px |
| w-80     | width: 20rem;       | 320px |
| w-96     | width: 24rem;       | 384px |
| w-px     | width: 1px;         |       |
| w-auto   | width: auto;        |       |
| w-1/2    | width: 50%;         |       |
| w-1/3    | width: 33.333333%;  |       |
| w-2/3    | width: 66.666667%;  |       |
| w-1/4    | width: 25%;         |       |
| w-2/4    | width: 50%;         |       |
| w-3/4    | width: 75%;         |       |
| w-1/5    | width: 20%;         |       |
| w-2/5    | width: 40%;         |       |
| w-3/5    | width: 60%;         |       |
| w-4/5    | width: 80%;         |       |
| w-1/6    | width: 16.666667%;  |       |
| w-2/6    | width: 33.333333%;  |       |
| w-3/6    | width: 50%;         |       |
| w-4/6    | width: 66.666667%;  |       |
| w-5/6    | width: 83.333333%;  |       |
| w-1/12   | width: 8.333333%;   |       |
| w-2/12   | width: 16.666667%;  |       |
| w-3/12   | width: 25%;         |       |
| w-4/12   | width: 33.333333%;  |       |
| w-5/12   | width: 41.666667%;  |       |
| w-6/12   | width: 50%;         |       |
| w-7/12   | width: 58.333333%;  |       |
| w-8/12   | width: 66.666667%;  |       |
| w-9/12   | width: 75%;         |       |
| w-10/12  | width: 83.333333%;  |       |
| w-11/12  | width: 91.666667%;  |       |
| w-full   | width: 100%;        |       |
| w-screen | width: 100vw;       |       |
| w-min    | width: min-content; |       |
| w-max    | width: max-content; |       |
| w-fit    | width: fit-content; |       |


### Min Width
Sets the minimum width of an element.

| Tailwind   | Description             | Other |
| ---------- | ----------------------- | ----- |
| min-w-0    | min-width: 0;           |       |
| min-w-full | min-width: 100%;        |       |
| min-w-min  | min-width: min-content; |       |
| min-w-max  | min-width: max-content; |       |
| min-w-fit  | min-width: fit-content; |       |



### Max Width
Sets the maxiumum width of an element.

| Tailwind         | Description             | Other  |
| ---------------- | ----------------------- | ------ |
| max-w-0          | max-width: 0rem;        |        |
| max-w-none       | max-width: none;        |        |
| max-w-xs         | max-width: 20rem;       | 320px  |
| max-w-sm         | max-width: 24rem;       | 384px  |
| max-w-md         | max-width: 28rem;       | 448px  |
| max-w-lg         | max-width: 32rem;       | 512px  |
| max-w-xl         | max-width: 36rem;       | 576px  |
| max-w-2xl        | max-width: 42rem;       | 672px  |
| max-w-3xl        | max-width: 48rem;       | 768px  |
| max-w-4xl        | max-width: 56rem;       | 896px  |
| max-w-5xl        | max-width: 64rem;       | 1024px |
| max-w-6xl        | max-width: 72rem;       | 1152px |
| max-w-7xl        | max-width: 80rem;       | 1280px |
| max-w-full       | max-width: 100%;        |        |
| max-w-min        | max-width: min-content; |        |
| max-w-max        | max-width: max-content; |        |
| max-w-fit        | max-width: fit-content; |        |
| max-w-prose      | max-width: 65ch;        |        |
| max-w-screen-sm  | max-width: 640px;       |        |
| max-w-screen-md  | max-width: 768px;       |        |
| max-w-screen-lg  | max-width: 1024px;      |        |
| max-w-screen-xl  | max-width: 1280px;      |        |
| max-w-screen-2xl | max-width: 1536px;      |        |


### Height 

| Tailwind | Description          | Other |
| -------- | -------------------- | ----- |
| h-0      | height: 0;           |       |
| h-0.5    | height: 0.125rem;    | 2px   |
| h-1      | height: 0.25rem;     | 4px   |
| h-1.5    | height: 0.375rem;    | 6px   |
| h-2      | height: 0.5rem;      | 8px   |
| h-2.5    | height: 0.625rem;    | 10px  |
| h-3      | height: 0.75rem;     | 12px  |
| h-3.5    | height: 0.875rem;    | 14px  |
| h-4      | height: 1rem;        | 16px  |
| h-5      | height: 1.25rem;     | 20px  |
| h-6      | height: 1.5rem;      | 24px  |
| h-8      | height: 2rem;        | 32px  |
| h-10     | height: 2.5rem;      | 40px  |
| h-11     | height: 2.75rem;     | 44px  |
| h-12     | height: 3rem;        | 48px  |
| h-14     | height: 3.5rem;      | 56px  |
| h-16     | height: 4rem;        | 64px  |
| h-20     | height: 5rem;        | 80px  |
| h-24     | height: 6rem;        | 96px  |
| h-28     | height: 7rem;        | 112px |
| h-32     | height: 8rem;        | 128px |
| h-36     | height: 9rem;        | 144px |
| h-40     | height: 10rem;       | 160px |
| h-44     | height: 11rem;       | 176px |
| h-48     | height: 12rem;       | 192px |
| h-52     | height: 13rem;       | 208px |
| h-56     | height: 14rem;       | 224px |
| h-64     | height: 16rem;       | 256px |
| h-72     | height: 18rem;       | 288px |
| h-80     | height: 20rem;       | 320px |
| h-96     | height: 24rem;       | 384px |
| h-px     | height: 1px;         |       |
| h-auto   | height: auto;        |       |
| h-1/2    | height: 50%;         |       |
| h-1/3    | height: 33.333333%;  |       |
| h-2/3    | height: 66.666667%;  |       |
| h-1/4    | height: 25%;         |       |
| h-2/4    | height: 50%;         |       |
| h-3/4    | height: 75%;         |       |
| h-1/5    | height: 20%;         |       |
| h-2/5    | height: 40%;         |       |
| h-3/5    | height: 60%;         |       |
| h-4/5    | height: 80%;         |       |
| h-1/6    | height: 16.666667%;  |       |
| h-2/6    | height: 33.333333%;  |       |
| h-3/6    | height: 50%;         |       |
| h-4/6    | height: 66.666667%;  |       |
| h-5/6    | height: 83.333333%;  |       |
| h-full   | height: 100%;        |       |
| h-screen | height: 100vh;       |       |
| h-min    | height: min-content; |       |
| h-max    | height: max-content; |       |
| h-fit    | height: fit-content; |       |



### Min Height
Sets the minimum height of an element.

| Tailwind     | Description              | Other |
| ------------ | ------------------------ | ----- |
| min-h-0      | min-height: 0;           |       |
| min-h-full   | min-height: 100%;        |       |
| min-h-screen | min-height: 100vh;       |       |
| min-h-min    | min-height: min-content; |       |
| min-h-max    | min-height: max-content; |       |
| min-h-fit    | min-height: fit-content; |       |



### Max Height
Sets the maxiumum height of an element.

| Tailwind     | Description              | Other |
| ------------ | ------------------------ | ----- |
| max-h-0      | max-height: 0;           |       |
| max-h-0.5    | max-height: 0.125rem;    | 2px   |
| max-h-1      | max-height: 0.25rem;     | 4px   |
| max-h-1.5    | max-height: 0.375rem;    | 6px   |
| max-h-2      | max-height: 0.5rem;      | 8px   |
| max-h-2.5    | max-height: 0.625rem;    | 10px  |
| max-h-3      | max-height: 0.75rem;     | 12px  |
| max-h-3.5    | max-height: 0.875rem;    | 14px  |
| max-h-4      | max-height: 1rem;        | 16px  |
| max-h-5      | max-height: 1.25rem;     | 20px  |
| max-h-6      | max-height: 1.5rem;      | 24px  |
| max-h-8      | max-height: 2rem;        | 32px  |
| max-h-10     | max-height: 2.5rem;      | 40px  |
| max-h-11     | max-height: 2.75rem;     | 44px  |
| max-h-12     | max-height: 3rem;        | 48px  |
| max-h-14     | max-height: 3.5rem;      | 56px  |
| max-h-16     | max-height: 4rem;        | 64px  |
| max-h-20     | max-height: 5rem;        | 80px  |
| max-h-24     | max-height: 6rem;        | 96px  |
| max-h-28     | max-height: 7rem;        | 112px |
| max-h-32     | max-height: 8rem;        | 128px |
| max-h-36     | max-height: 9rem;        | 144px |
| max-h-40     | max-height: 10rem;       | 160px |
| max-h-44     | max-height: 11rem;       | 176px |
| max-h-48     | max-height: 12rem;       | 192px |
| max-h-52     | max-height: 13rem;       | 208px |
| max-h-56     | max-height: 14rem;       | 224px |
| max-h-64     | max-height: 16rem;       | 256px |
| max-h-72     | max-height: 18rem;       | 288px |
| max-h-80     | max-height: 20rem;       | 320px |
| max-h-96     | max-height: 24rem;       | 384px |
| max-h-px     | max-height: 1px;         |       |
| max-h-full   | max-height: 100%;        |       |
| max-h-screen | max-height: 100vh;       |       |
| max-h-min    | max-height: min-content; |       |
| max-h-max    | max-height: max-content; |       |
| max-h-fit    | max-height: fit-content; |       |



---


## Transforms


### Scale
Scales an element that has transform applied.

| Tailwind    | Description                                           | Other |
| ----------- | ----------------------------------------------------- | ----- |
| scale-0     | --transform-scale-x: 0; --transform-scale-y: 0;       |       |
| scale-50    | --transform-scale-x: .5; --transform-scale-y: .5;     |       |
| scale-75    | --transform-scale-x: .75; --transform-scale-y: .75;   |       |
| scale-90    | --transform-scale-x: .9; --transform-scale-y: .9;     |       |
| scale-95    | --transform-scale-x: .95; --transform-scale-y: .95;   |       |
| scale-100   | --transform-scale-x: 1; --transform-scale-y: 1;       |       |
| scale-105   | --transform-scale-x: 1.05; --transform-scale-y: 1.05; |       |
| scale-110   | --transform-scale-x: 1.1; --transform-scale-y: 1.1;   |       |
| scale-125   | --transform-scale-x: 1.25; --transform-scale-y: 1.25; |       |
| scale-150   | --transform-scale-x: 1.5; --transform-scale-y: 1.5;   |       |
| scale-x-0   | --transform-scale-x: 0;                               |       |
| scale-x-50  | --transform-scale-x: .5;                              |       |
| scale-x-75  | --transform-scale-x: .75;                             |       |
| scale-x-90  | --transform-scale-x: .9;                              |       |
| scale-x-95  | --transform-scale-x: .95;                             |       |
| scale-x-100 | --transform-scale-x: 1;                               |       |
| scale-x-105 | --transform-scale-x: 1.05;                            |       |
| scale-x-110 | --transform-scale-x: 1.1;                             |       |
| scale-x-125 | --transform-scale-x: 1.25;                            |       |
| scale-x-150 | --transform-scale-x: 1.5;                             |       |
| scale-y-0   | --transform-scale-y: 0;                               |       |
| scale-y-50  | --transform-scale-y: .5;                              |       |
| scale-y-75  | --transform-scale-y: .75;                             |       |
| scale-y-90  | --transform-scale-y: .9;                              |       |
| scale-y-95  | --transform-scale-y: .95;                             |       |
| scale-y-100 | --transform-scale-y: 1;                               |       |
| scale-y-105 | --transform-scale-y: 1.05;                            |       |
| scale-y-110 | --transform-scale-y: 1.1;                             |       |
| scale-y-125 | --transform-scale-y: 1.25;                            |       |
| scale-y-150 | --transform-scale-y: 1.5;                             |       |




### Rotate
Rotates an element that has transform applied.

| Tailwind   | Description                 | Other |
| ---------- | --------------------------- | ----- |
| rotate-0   | --transform-rotate: 0;      |       |
| rotate-1   | --transform-rotate: 1deg;   |       |
| rotate-2   | --transform-rotate: 2deg;   |       |
| rotate-3   | --transform-rotate: 3deg;   |       |
| rotate-6   | --transform-rotate: 6deg;   |       |
| rotate-12  | --transform-rotate: 12deg;  |       |
| rotate-45  | --transform-rotate: 45deg;  |       |
| rotate-90  | --transform-rotate: 90deg;  |       |
| rotate-180 | --transform-rotate: 180deg; |       |





### Translate
Translates an element that has transform applied.

| Tailwind         | Description                           | Other |
| ---------------- | ------------------------------------- | ----- |
| translate-x-0    | --transform-translate-x: 0;           |       |
| translate-x-0.5  | --transform-translate-x: 0.125rem;    | 2px   |
| translate-x-1    | --transform-translate-x: 0.25rem;     | 4px   |
| translate-x-1.5  | --transform-translate-x: 0.375rem;    | 6px   |
| translate-x-2    | --transform-translate-x: 0.5rem;      | 8px   |
| translate-x-2.5  | --transform-translate-x: 0.625rem;    | 10px  |
| translate-x-3    | --transform-translate-x: 0.75rem;     | 12px  |
| translate-x-3.5  | --transform-translate-x: 0.875rem;    | 14px  |
| translate-x-4    | --transform-translate-x: 1rem;        | 16px  |
| translate-x-5    | --transform-translate-x: 1.25rem;     | 20px  |
| translate-x-6    | --transform-translate-x: 1.5rem;      | 24px  |
| translate-x-7    | --transform-translate-x: 1.75rem;     | 28px  |
| translate-x-8    | --transform-translate-x: 2rem;        | 32px  |
| translate-x-9    | --transform-translate-x: 2.25rem;     | 36px  |
| translate-x-10   | --transform-translate-x: 2.5rem;      | 40px  |
| translate-x-11   | --transform-translate-x: 2.75rem;     | 44px  |
| translate-x-12   | --transform-translate-x: 3rem;        | 48px  |
| translate-x-14   | --transform-translate-x: 3.5rem;      | 56px  |
| translate-x-16   | --transform-translate-x: 4rem;        | 64px  |
| translate-x-20   | --transform-translate-x: 5rem;        | 80px  |
| translate-x-24   | --transform-translate-x: 6rem;        | 96px  |
| translate-x-28   | --transform-translate-x: 7rem;        | 112px |
| translate-x-32   | --transform-translate-x: 8rem;        | 128px |
| translate-x-36   | --transform-translate-x: 8rem;        | 144px |
| translate-x-40   | --transform-translate-x: 10rem;       | 160px |
| translate-x-44   | --transform-translate-x: 11rem;       | 176px |
| translate-x-48   | --transform-translate-x: 12rem;       | 192px |
| translate-x-52   | --transform-translate-x: 13rem;       | 208px |
| translate-x-56   | --transform-translate-x: 14rem;       | 224px |
| translate-x-60   | --transform-translate-x: 15rem;       | 240px |
| translate-x-64   | --transform-translate-x: 16rem;       | 256px |
| translate-x-72   | --transform-translate-x: 18rem;       | 288px |
| translate-x-80   | --transform-translate-x: 20rem;       | 320px |
| translate-x-96   | --transform-translate-x: 24rem;       | 384px |
| translate-x-px   | --transform-translate-x: 1px;         |       |
| translate-x-1/2  | --transform-translate-x: 50%;         |       |
| translate-x-1/3  | --transform-translate-x: 33.333333%;  |       |
| translate-x-2/3  | --transform-translate-x: 66.6666666%; |       |
| translate-x-1/4  | --transform-translate-x: 25%;         |       |
| translate-x-2/4  | --transform-translate-x: 50%;         |       |
| translate-x-3/4  | --transform-translate-x: 75%;         |       |
| translate-x-full | --transform-translate-x: 100%;        |       |
| translate-y-0    | --transform-translate-y: 0;           |       |
| translate-y-0.5  | --transform-translate-y: 0.125rem;    | 2px   |
| translate-y-1    | --transform-translate-y: 0.25rem;     | 4px   |
| translate-y-1.5  | --transform-translate-y: 0.375rem;    | 6px   |
| translate-y-2    | --transform-translate-y: 0.5rem;      | 8px   |
| translate-y-2.5  | --transform-translate-y: 0.625rem;    | 10px  |
| translate-y-3    | --transform-translate-y: 0.75rem;     | 12px  |
| translate-y-3.5  | --transform-translate-y: 0.875rem;    | 14px  |
| translate-y-4    | --transform-translate-y: 1rem;        | 16px  |
| translate-y-5    | --transform-translate-y: 1.25rem;     | 20px  |
| translate-y-6    | --transform-translate-y: 1.5rem;      | 24px  |
| translate-y-7    | --transform-translate-y: 1.75rem;     | 28px  |
| translate-y-8    | --transform-translate-y: 2rem;        | 32px  |
| translate-y-9    | --transform-translate-y: 2.25rem;     | 36px  |
| translate-y-10   | --transform-translate-y: 2.5rem;      | 40px  |
| translate-y-11   | --transform-translate-y: 2.75rem;     | 44px  |
| translate-y-12   | --transform-translate-y: 3rem;        | 48px  |
| translate-y-14   | --transform-translate-y: 3.5rem;      | 56px  |
| translate-y-16   | --transform-translate-y: 4rem;        | 64px  |
| translate-y-20   | --transform-translate-y: 5rem;        | 80px  |
| translate-y-24   | --transform-translate-y: 6rem;        | 96px  |
| translate-y-28   | --transform-translate-y: 7rem;        | 112px |
| translate-y-32   | --transform-translate-y: 8rem;        | 128px |
| translate-y-36   | --transform-translate-y: 8rem;        | 144px |
| translate-y-40   | --transform-translate-y: 10rem;       | 160px |
| translate-y-44   | --transform-translate-y: 11rem;       | 176px |
| translate-y-48   | --transform-translate-y: 12rem;       | 192px |
| translate-y-52   | --transform-translate-y: 13rem;       | 208px |
| translate-y-56   | --transform-translate-y: 14rem;       | 224px |
| translate-y-60   | --transform-translate-y: 15rem;       | 240px |
| translate-y-64   | --transform-translate-y: 16rem;       | 256px |
| translate-y-72   | --transform-translate-y: 18rem;       | 288px |
| translate-y-80   | --transform-translate-y: 20rem;       | 320px |
| translate-y-96   | --transform-translate-y: 24rem;       | 384px |
| translate-y-px   | --transform-translate-y: 1px;         |       |
| translate-y-1/2  | --transform-translate-y: 50%;         |       |
| translate-y-1/3  | --transform-translate-y: 33.333333%;  |       |
| translate-y-2/3  | --transform-translate-y: 66.6666666%; |       |
| translate-y-1/4  | --transform-translate-y: 25%;         |       |
| translate-y-2/4  | --transform-translate-y: 50%;         |       |
| translate-y-3/4  | --transform-translate-y: 75%;         |       |
| translate-y-full | --transform-translate-y: 100%;        |       |





### Skew
Skews an element that has transform applied.

| Tailwind  | Description                | Other |
| --------- | -------------------------- | ----- |
| skew-x-0  | --transform-skew-x: 0;     |       |
| skew-x-1  | --transform-skew-x: 1deg;  |       |
| skew-x-2  | --transform-skew-x: 2deg;  |       |
| skew-x-3  | --transform-skew-x: 3deg;  |       |
| skew-x-6  | --transform-skew-x: 6deg;  |       |
| skew-x-12 | --transform-skew-x: 12deg; |       |
| skew-y-0  | --transform-skew-y: 0;     |       |
| skew-y-1  | --transform-skew-y: 1deg;  |       |
| skew-y-2  | --transform-skew-y: 2deg;  |       |
| skew-y-3  | --transform-skew-y: 3deg;  |       |
| skew-y-6  | --transform-skew-y: 6deg;  |       |
| skew-y-12 | --transform-skew-y: 12deg; |       |



### Transform Origin
Sets the origin of an element's transforms. Think of the origin as pushing a thumbtack into the element at the specified position.

| Tailwind            | Description                     | Other |
| ------------------- | ------------------------------- | ----- |
| origin-center       | transform-origin: center;       |       |
| origin-top          | transform-origin: top;          |       |
| origin-top-right    | transform-origin: top right;    |       |
| origin-right        | transform-origin: right;        |       |
| origin-bottom-right | transform-origin: bottom right; |       |
| origin-bottom       | transform-origin: bottom;       |       |
| origin-bottom-left  | transform-origin: bottom left;  |       |
| origin-left         | transform-origin: left;         |       |
| origin-top-left     | transform-origin: top left;     |       |


---


## Effects


### Box Shadow

| Tailwind       | Description                                                                            | Other |
| -------------- | -------------------------------------------------------------------------------------- | ----- |
| shadow-xs      | box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.05);                                             |       |
| shadow-sm      | box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);                                           |       |
| shadow         | box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);           |       |
| shadow-md      | box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);     |       |
| shadow-lg      | box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);   |       |
| shadow-xl      | box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04); |       |
| shadow-2xl     | box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);                                     |       |
| shadow-inner   | box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.06);                                     |       |
| shadow-outline | box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);                                         |       |
| shadow-none    | box-shadow: none;                                                                      |       |




### Opacity

| Tailwind    | Description    | Other |
| ----------- | -------------- | ----- |
| opacity-0   | opacity: 0;    |       |
| opacity-5   | opacity: 0.05; |       |
| opacity-10  | opacity: 0.1;  |       |
| opacity-20  | opacity: 0.2;  |       |
| opacity-25  | opacity: 0.25; |       |
| opacity-30  | opacity: 0.3;  |       |
| opacity-40  | opacity: 0.4;  |       |
| opacity-50  | opacity: 0.5;  |       |
| opacity-60  | opacity: 0.6;  |       |
| opacity-70  | opacity: 0.7;  |       |
| opacity-75  | opacity: 0.75; |       |
| opacity-80  | opacity: 0.8;  |       |
| opacity-90  | opacity: 0.9;  |       |
| opacity-100 | opacity: 1;    |       |




### Mix Blend Mode
Utilities for controlling how an element should blend with the background.

| Tailwind              | Description                  | Other |
| --------------------- | ---------------------------- | ----- |
| mix-blend-normal      | mix-blend-mode: normal;      |       |
| mix-blend-multiply    | mix-blend-mode: multiply;    |       |
| mix-blend-screen      | mix-blend-mode: screen;      |       |
| mix-blend-overlay     | mix-blend-mode: overlay;     |       |
| mix-blend-darken      | mix-blend-mode: darken;      |       |
| mix-blend-lighten     | mix-blend-mode: lighten;     |       |
| mix-blend-color-dodge | mix-blend-mode: color-dodge; |       |
| mix-blend-color-burn  | mix-blend-mode: color-burn;  |       |
| mix-blend-hard-light  | mix-blend-mode: hard-light;  |       |
| mix-blend-soft-light  | mix-blend-mode: soft-light;  |       |
| mix-blend-difference  | mix-blend-mode: difference;  |       |
| mix-blend-exclusion   | mix-blend-mode: exclusion;   |       |
| mix-blend-hue         | mix-blend-mode: hue;         |       |
| mix-blend-saturation  | mix-blend-mode: saturation;  |       |
| mix-blend-color       | mix-blend-mode: color;       |       |
| mix-blend-luminosity  | mix-blend-mode: luminosity;  |       |




### Background Blend Mode
Utilities for controlling how an element's background image should blend with its background color.

| Tailwind             | Description                         | Other |
| -------------------- | ----------------------------------- | ----- |
| bg-blend-normal      | background-blend-mode: normal;      |       |
| bg-blend-multiply    | background-blend-mode: multiply;    |       |
| bg-blend-screen      | background-blend-mode: screen;      |       |
| bg-blend-overlay     | background-blend-mode: overlay;     |       |
| bg-blend-darken      | background-blend-mode: darken;      |       |
| bg-blend-lighten     | background-blend-mode: lighten;     |       |
| bg-blend-color-dodge | background-blend-mode: color-dodge; |       |
| bg-blend-color-burn  | background-blend-mode: color-burn;  |       |
| bg-blend-hard-light  | background-blend-mode: hard-light;  |       |
| bg-blend-soft-light  | background-blend-mode: soft-light;  |       |
| bg-blend-difference  | background-blend-mode: difference;  |       |
| bg-blend-exclusion   | background-blend-mode: exclusion;   |       |
| bg-blend-hue         | background-blend-mode: hue;         |       |
| bg-blend-saturation  | background-blend-mode: saturation;  |       |
| bg-blend-color       | background-blend-mode: color;       |       |
| bg-blend-luminosity  | background-blend-mode: luminosity;  |       |


---


## Spacing 


### Padding
Controls padding in 0.25rem increments.

| Tailwind | Description                                      | Other |
| -------- | ------------------------------------------------ | ----- |
| p-0      | padding: 0;                                      |       |
| p-0.5    | padding: 0.125rem;                               | 2px   |
| p-1      | padding: 0.25rem;                                | 4px   |
| p-1.5    | padding: 0.375rem;                               | 6px   |
| p-2      | padding: 0.5rem;                                 | 8px   |
| p-2.5    | padding: 0.625rem;                               | 10px  |
| p-3      | padding: 0.75rem;                                | 12px  |
| p-3.5    | padding: 0.875rem;                               | 14px  |
| p-4      | padding: 1rem;                                   | 16px  |
| p-5      | padding: 1.25rem;                                | 20px  |
| p-6      | padding: 1.5rem;                                 | 24px  |
| p-8      | padding: 2rem;                                   | 32px  |
| p-10     | padding: 2.5rem;                                 | 40px  |
| p-11     | padding: 2.75rem;                                | 44px  |
| p-12     | padding: 3rem;                                   | 48px  |
| p-14     | padding: 3.5rem;                                 | 56px  |
| p-16     | padding: 4rem;                                   | 64px  |
| p-20     | padding: 5rem;                                   | 80px  |
| p-24     | padding: 6rem;                                   | 96px  |
| p-28     | padding: 7rem;                                   | 112px |
| p-32     | padding: 8rem;                                   | 128px |
| p-36     | padding: 9rem;                                   | 144px |
| p-40     | padding: 10rem;                                  | 160px |
| p-44     | padding: 11rem;                                  | 176px |
| p-48     | padding: 12rem;                                  | 192px |
| p-52     | padding: 13rem;                                  | 208px |
| p-56     | padding: 14rem;                                  | 224px |
| p-64     | padding: 16rem;                                  | 256px |
| p-72     | padding: 18rem;                                  | 288px |
| p-80     | padding: 20rem;                                  | 320px |
| p-96     | padding: 24rem;                                  | 384px |
| p-px     | padding: 1px;                                    |       |
| py-0     | padding-top: 0; padding-bottom: 0;               |       |
| px-0     | padding-left: 0; padding-right: 0;               |       |
| py-0.5   | padding-top: 0.125rem; padding-bottom: 0.125rem; | 2px   |
| px-0.5   | padding-left: 0.125rem; padding-right: 0.125rem; | 2px   |
| py-1     | padding-top: 0.25rem; padding-bottom: 0.25rem;   | 4px   |
| px-1     | padding-left: 0.25rem; padding-right: 0.25rem;   | 4px   |
| py-1.5   | padding-top: 0.375rem; padding-bottom: 0.375rem; | 6px   |
| px-1.5   | padding-left: 0.375rem; padding-right: 0.375rem; | 6px   |
| py-2     | padding-top: 0.5rem; padding-bottom: 0.5rem;     | 8px   |
| px-2     | padding-left: 0.5rem; padding-right: 0.5rem;     | 8px   |
| py-2.5   | padding-top: 0.625rem; padding-bottom: 0.625rem; | 10px  |
| px-2.5   | padding-left: 0.625rem; padding-right: 0.625rem; | 10px  |
| py-3     | padding-top: 0.75rem; padding-bottom: 0.75rem;   | 12px  |
| px-3     | padding-left: 0.75rem; padding-right: 0.75rem;   | 12px  |
| py-3.5   | padding-top: 0.875rem; padding-bottom: 0.875rem; | 14px  |
| px-3.5   | padding-left: 0.875rem; padding-right: 0.875rem; | 14px  |
| py-4     | padding-top: 1rem; padding-bottom: 1rem;         | 16px  |
| px-4     | padding-left: 1rem; padding-right: 1rem;         | 16px  |
| py-5     | padding-top: 1.25rem; padding-bottom: 1.25rem;   | 20px  |
| px-5     | padding-left: 1.25rem; padding-right: 1.25rem;   | 20px  |
| py-6     | padding-top: 1.5rem; padding-bottom: 1.5rem;     | 24px  |
| px-6     | padding-left: 1.5rem; padding-right: 1.5rem;     | 24px  |
| py-7     | padding-top: 1.75rem; padding-bottom: 1.75rem;   | 24px  |
| px-7     | padding-left: 1.75rem; padding-right: 1.75rem;   | 24px  |
| py-8     | padding-top: 2rem; padding-bottom: 2rem;         | 32px  |
| px-8     | padding-left: 2rem; padding-right: 2rem;         | 32px  |
| py-9     | padding-top: 2.25rem; padding-bottom: 2.25rem;   | 36px  |
| px-9     | padding-left: 2.25rem; padding-right: 2.25rem;   | 36px  |
| py-10    | padding-top: 2.5rem; padding-bottom: 2.5rem;     | 40px  |
| px-10    | padding-left: 2.5rem; padding-right: 2.5rem;     | 40px  |
| py-11    | padding-top: 2.75rem; padding-bottom: 2.75rem;   | 44px  |
| px-11    | padding-left: 2.75rem; padding-right: 2.75rem;   | 44px  |
| py-12    | padding-top: 3rem; padding-bottom: 3rem;         | 48px  |
| px-12    | padding-left: 3rem; padding-right: 3rem;         | 48px  |
| py-14    | padding-top: 3.5rem; padding-bottom: 3.5rem;     | 56px  |
| px-14    | padding-left: 3.5rem; padding-right: 3.5rem;     | 56px  |
| py-16    | padding-top: 4rem; padding-bottom: 4rem;         | 64px  |
| px-16    | padding-left: 4rem; padding-right: 4rem;         | 64px  |
| py-20    | padding-top: 5rem; padding-bottom: 5rem;         | 80px  |
| px-20    | padding-left: 5rem; padding-right: 5rem;         | 80px  |
| py-24    | padding-top: 6rem; padding-bottom: 6rem;         | 96px  |
| px-24    | padding-left: 6rem; padding-right: 6rem;         | 96px  |
| py-28    | padding-top: 7rem; padding-bottom: 7rem;         | 112px |
| px-28    | padding-left: 7rem; padding-right: 7rem;         | 112px |
| py-32    | padding-top: 8rem; padding-bottom: 8rem;         | 128px |
| px-32    | padding-left: 8rem; padding-right: 8rem;         | 128px |
| py-36    | padding-top: 9rem; padding-bottom: 9rem;         | 144px |
| px-36    | padding-left: 9rem; padding-right: 9rem;         | 144px |
| py-40    | padding-top: 10rem; padding-bottom: 10rem;       | 160px |
| px-40    | padding-left: 10rem; padding-right: 10rem;       | 160px |
| py-44    | padding-top: 11rem; padding-bottom: 11rem;       | 176px |
| px-44    | padding-left: 11rem; padding-right: 11rem;       | 176px |
| py-48    | padding-top: 12rem; padding-bottom: 12rem;       | 192px |
| px-48    | padding-left: 12rem; padding-right: 12rem;       | 192px |
| py-52    | padding-top: 13rem; padding-bottom: 13rem;       | 208px |
| px-52    | padding-left: 13rem; padding-right: 13rem;       | 208px |
| py-56    | padding-top: 14rem; padding-bottom: 14rem;       | 224px |
| px-56    | padding-left: 14rem; padding-right: 14rem;       | 224px |
| py-60    | padding-top: 15rem; padding-bottom: 15rem;       | 240px |
| px-60    | padding-left: 15rem; padding-right: 15rem;       | 240px |
| py-64    | padding-top: 16rem; padding-bottom: 16rem;       | 256px |
| px-64    | padding-left: 16rem; padding-right: 16rem;       | 256px |
| py-70    | padding-top: 18rem; padding-bottom: 18rem;       | 280px |
| px-70    | padding-left: 18rem; padding-right: 18rem;       | 280px |
| py-80    | padding-top: 20rem; padding-bottom: 20rem;       | 320px |
| px-80    | padding-left: 20rem; padding-right: 20rem;       | 320px |
| py-96    | padding-top: 24rem; padding-bottom: 24rem;       | 384px |
| px-96    | padding-left: 24rem; padding-right: 24rem;       | 384px |
| py-px    | padding-top: 1px; padding-bottom: 1px;           |       |
| px-px    | padding-left: 1px; padding-right: 1px;           |       |
| pt-0     | padding-top: 0;                                  |       |
| pr-0     | padding-right: 0;                                |       |
| pb-0     | padding-bottom: 0;                               |       |
| pl-0     | padding-left: 0;                                 |       |
| pt-0.5   | padding-top: 0.125rem;                           | 2px   |
| pr-0.5   | padding-right: 0.125rem;                         | 2px   |
| pb-0.5   | padding-bottom: 0.125rem;                        | 2px   |
| pl-0.5   | padding-left: 0.125rem;                          | 2px   |
| pt-1     | padding-top: 0.25rem;                            | 4px   |
| pr-1     | padding-right: 0.25rem;                          | 4px   |
| pb-1     | padding-bottom: 0.25rem;                         | 4px   |
| pl-1     | padding-left: 0.25rem;                           | 4px   |
| pt-1.5   | padding-top: 0.375rem;                           | 6px   |
| pr-1.5   | padding-right: 0.375rem;                         | 6px   |
| pb-1.5   | padding-bottom: 0.375rem;                        | 6px   |
| pl-1.5   | padding-left: 0.375rem;                          | 6px   |
| pt-2     | padding-top: 0.5rem;                             | 8px   |
| pr-2     | padding-right: 0.5rem;                           | 8px   |
| pb-2     | padding-bottom: 0.5rem;                          | 8px   |
| pl-2     | padding-left: 0.5rem;                            | 8px   |
| pt-2.5   | padding-top: 0.625rem;                           | 10px  |
| pr-2.5   | padding-right: 0.625rem;                         | 10px  |
| pb-2.5   | padding-bottom: 0.625rem;                        | 10px  |
| pl-2.5   | padding-left: 0.625rem;                          | 10px  |
| pt-3     | padding-top: 0.75rem;                            | 12px  |
| pr-3     | padding-right: 0.75rem;                          | 12px  |
| pb-3     | padding-bottom: 0.75rem;                         | 12px  |
| pl-3     | padding-left: 0.75rem;                           | 12px  |
| pt-3.5   | padding-top: 0.875rem;                           | 14px  |
| pr-3.5   | padding-right: 0.875rem;                         | 14px  |
| pb-3.5   | padding-bottom: 0.875rem;                        | 14px  |
| pl-3.5   | padding-left: 0.875rem;                          | 14px  |
| pt-4     | padding-top: 1rem;                               | 16px  |
| pr-4     | padding-right: 1rem;                             | 16px  |
| pb-4     | padding-bottom: 1rem;                            | 16px  |
| pl-4     | padding-left: 1rem;                              | 16px  |
| pt-5     | padding-top: 1.25rem;                            | 20px  |
| pr-5     | padding-right: 1.25rem;                          | 20px  |
| pb-5     | padding-bottom: 1.25rem;                         | 20px  |
| pl-5     | padding-left: 1.25rem;                           | 20px  |
| pt-6     | padding-top: 1.5rem;                             | 24px  |
| pr-6     | padding-right: 1.5rem;                           | 24px  |
| pb-6     | padding-bottom: 1.5rem;                          | 24px  |
| pl-6     | padding-left: 1.5rem;                            | 24px  |
| pt-7     | padding-top: 1.75rem;                            | 28px  |
| pr-7     | padding-right: 1.75rem;                          | 28px  |
| pb-7     | padding-bottom: 1.75rem;                         | 28px  |
| pl-7     | padding-left: 1.75rem;                           | 28px  |
| pt-8     | padding-top: 2rem;                               | 32px  |
| pr-8     | padding-right: 2rem;                             | 32px  |
| pb-8     | padding-bottom: 2rem;                            | 32px  |
| pl-8     | padding-left: 2rem;                              | 32px  |
| pt-9     | padding-top: 2.25rem;                            | 36px  |
| pr-9     | padding-right: 2.25rem;                          | 36px  |
| pb-9     | padding-bottom: 2.25rem;                         | 36px  |
| pl-9     | padding-left: 2.25rem;                           | 36px  |
| pt-10    | padding-top: 2.5rem;                             | 40px  |
| pr-10    | padding-right: 2.5rem;                           | 40px  |
| pb-10    | padding-bottom: 2.5rem;                          | 40px  |
| pl-10    | padding-left: 2.5rem;                            | 40px  |
| pt-11    | padding-top: 2.75rem;                            | 44px  |
| pr-11    | padding-right: 2.75rem;                          | 44px  |
| pb-11    | padding-bottom: 2.75rem;                         | 44px  |
| pl-11    | padding-left: 2.75rem;                           | 44px  |
| pt-12    | padding-top: 3rem;                               | 48px  |
| pr-12    | padding-right: 3rem;                             | 48px  |
| pb-12    | padding-bottom: 3rem;                            | 48px  |
| pl-12    | padding-left: 3rem;                              | 48px  |
| pt-14    | padding-top: 3.5rem;                             | 56px  |
| pr-14    | padding-right: 3.5rem;                           | 56px  |
| pb-14    | padding-bottom: 3.5rem;                          | 56px  |
| pl-14    | padding-left: 3.5rem;                            | 56px  |
| pt-16    | padding-top: 4rem;                               | 64px  |
| pr-16    | padding-right: 4rem;                             | 64px  |
| pb-16    | padding-bottom: 4rem;                            | 64px  |
| pl-16    | padding-left: 4rem;                              | 64px  |
| pt-20    | padding-top: 5rem;                               | 80px  |
| pr-20    | padding-right: 5rem;                             | 80px  |
| pb-20    | padding-bottom: 5rem;                            | 80px  |
| pl-20    | padding-left: 5rem;                              | 80px  |
| pt-24    | padding-top: 6rem;                               | 96px  |
| pr-24    | padding-right: 6rem;                             | 96px  |
| pb-24    | padding-bottom: 6rem;                            | 96px  |
| pl-24    | padding-left: 6rem;                              | 96px  |
| pt-28    | padding-top: 7rem;                               | 112px |
| pr-28    | padding-right: 7rem;                             | 112px |
| pb-28    | padding-bottom: 7rem;                            | 112px |
| pl-28    | padding-left: 7rem;                              | 112px |
| pt-32    | padding-top: 8rem;                               | 128px |
| pr-32    | padding-right: 8rem;                             | 128px |
| pb-32    | padding-bottom: 8rem;                            | 128px |
| pl-32    | padding-left: 8rem;                              | 128px |
| pt-36    | padding-top: 9rem;                               | 144px |
| pr-36    | padding-right: 9rem;                             | 144px |
| pb-36    | padding-bottom: 9rem;                            | 144px |
| pl-36    | padding-left: 9rem;                              | 144px |
| pt-40    | padding-top: 10rem;                              | 160px |
| pr-40    | padding-right: 10rem;                            | 160px |
| pb-40    | padding-bottom: 10rem;                           | 160px |
| pl-40    | padding-left: 10rem;                             | 160px |
| pt-44    | padding-top: 11rem;                              | 176px |
| pr-44    | padding-right: 11rem;                            | 176px |
| pb-44    | padding-bottom: 11rem;                           | 176px |
| pl-44    | padding-left: 11rem;                             | 176px |
| pt-48    | padding-top: 12rem;                              | 192px |
| pr-48    | padding-right: 12rem;                            | 192px |
| pb-48    | padding-bottom: 12rem;                           | 192px |
| pl-48    | padding-left: 12rem;                             | 192px |
| pt-52    | padding-top: 13rem;                              | 208px |
| pr-52    | padding-right: 13rem;                            | 208px |
| pb-52    | padding-bottom: 13rem;                           | 208px |
| pl-52    | padding-left: 13rem;                             | 208px |
| pt-56    | padding-top: 14rem;                              | 224px |
| pr-56    | padding-right: 14rem;                            | 224px |
| pb-56    | padding-bottom: 14rem;                           | 224px |
| pl-56    | padding-left: 14rem;                             | 224px |
| pt-60    | padding-top: 15rem;                              | 240px |
| pr-60    | padding-right: 15rem;                            | 240px |
| pb-60    | padding-bottom: 15rem;                           | 240px |
| pl-60    | padding-left: 15rem;                             | 240px |
| pt-64    | padding-top: 16rem;                              | 256px |
| pr-64    | padding-right: 16rem;                            | 256px |
| pb-64    | padding-bottom: 16rem;                           | 256px |
| pl-64    | padding-left: 16rem;                             | 256px |
| pt-72    | padding-top: 18rem;                              | 288px |
| pr-72    | padding-right: 18rem;                            | 288px |
| pb-72    | padding-bottom: 18rem;                           | 288px |
| pl-72    | padding-left: 18rem;                             | 288px |
| pt-80    | padding-top: 20rem;                              | 320px |
| pr-80    | padding-right: 20rem;                            | 320px |
| pb-80    | padding-bottom: 20rem;                           | 320px |
| pl-80    | padding-left: 20rem;                             | 320px |
| pt-96    | padding-top: 24rem;                              | 384px |
| pr-96    | padding-right: 24rem;                            | 384px |
| pb-96    | padding-bottom: 24rem;                           | 384px |
| pl-96    | padding-left: 24rem;                             | 384px |
| pt-px    | padding-top: 1px;                                |       |
| pr-px    | padding-right: 1px;                              |       |
| pb-px    | padding-bottom: 1px;                             |       |
| pl-px    | padding-left: 1px;                               |       |




### Margin
Controls margin (and negative margin) in 0.25rem increments.

| Tailwind | Description                                      | Other |
| -------- | ------------------------------------------------ | ----- |
| m-0      | margin: 0;                                       |       |
| m-0.5    | margin: 0.125rem;                                | 2px   |
| m-1      | margin: 0.25rem;                                 | 4px   |
| m-1.5    | margin: 0.375rem;                                | 6px   |
| m-2      | margin: 0.5rem;                                  | 8px   |
| m-2.5    | margin: 0.625rem;                                | 10px  |
| m-3      | margin: 0.75rem;                                 | 12px  |
| m-3.5    | margin: 0.875rem;                                | 14px  |
| m-4      | margin: 1rem;                                    | 16px  |
| m-5      | margin: 1.25rem;                                 | 20px  |
| m-6      | margin: 1.5rem;                                  | 24px  |
| m-8      | margin: 2rem;                                    | 32px  |
| m-10     | margin: 2.5rem;                                  | 40px  |
| m-11     | margin: 2.75rem;                                 | 44px  |
| m-12     | margin: 3rem;                                    | 48px  |
| m-14     | margin: 3.5rem;                                  | 56px  |
| m-16     | margin: 4rem;                                    | 64px  |
| m-20     | margin: 5rem;                                    | 80px  |
| m-24     | margin: 6rem;                                    | 96px  |
| m-28     | margin: 7rem;                                    | 112px |
| m-32     | margin: 8rem;                                    | 128px |
| m-36     | margin: 9rem;                                    | 144px |
| m-40     | margin: 10rem;                                   | 160px |
| m-44     | margin: 11rem;                                   | 176px |
| m-48     | margin: 12rem;                                   | 192px |
| m-52     | margin: 13rem;                                   | 208px |
| m-56     | margin: 14rem;                                   | 224px |
| m-64     | margin: 16rem;                                   | 256px |
| m-72     | margin: 18rem;                                   | 288px |
| m-80     | margin: 20rem;                                   | 320px |
| m-96     | margin: 24rem;                                   | 384px |
| m-px     | margin: 1px;                                     |       |
| my-0     | margin-top: 0; margin-bottom: 0;                 |       |
| mx-0     | margin-left: 0; margin-right: 0;                 |       |
| my-0.5   | margin-top: 0.125rem; margin-bottom: 0.125rem;   | 2px   |
| mx-0.5   | margin-left: 0.125rem; margin-right: 0.125rem;   | 2px   |
| my-1     | margin-top: 0.25rem; margin-bottom: 0.25rem;     | 4px   |
| mx-1     | margin-left: 0.25rem; margin-right: 0.25rem;     | 4px   |
| my-1.5   | margin-top: 0.375rem; margin-bottom: 0.375rem;   | 6px   |
| mx-1.5   | margin-left: 0.375rem; margin-right: 0.375rem;   | 6px   |
| my-2     | margin-top: 0.5rem; margin-bottom: 0.5rem;       | 8px   |
| mx-2     | margin-left: 0.5rem; margin-right: 0.5rem;       | 8px   |
| my-2.5   | margin-top: 0.625rem; margin-bottom: 0.625rem;   | 10px  |
| mx-2.5   | margin-left: 0.625rem; margin-right: 0.625rem;   | 10px  |
| my-3     | margin-top: 0.75rem; margin-bottom: 0.75rem;     | 12px  |
| mx-3     | margin-left: 0.75rem; margin-right: 0.75rem;     | 12px  |
| my-3.5   | margin-top: 0.875rem; margin-bottom: 0.875rem;   | 14px  |
| mx-3.5   | margin-left: 0.875rem; margin-right: 0.875rem;   | 14px  |
| my-4     | margin-top: 1rem; margin-bottom: 1rem;           | 16px  |
| mx-4     | margin-left: 1rem; margin-right: 1rem;           | 16px  |
| my-5     | margin-top: 1.25rem; margin-bottom: 1.25rem;     | 20px  |
| mx-5     | margin-left: 1.25rem; margin-right: 1.25rem;     | 20px  |
| my-6     | margin-top: 1.5rem; margin-bottom: 1.5rem;       | 24px  |
| mx-6     | margin-left: 1.5rem; margin-right: 1.5rem;       | 24px  |
| my-7     | margin-top: 1.75rem; margin-bottom: 1.75rem;     | 24px  |
| mx-7     | margin-left: 1.75rem; margin-right: 1.75rem;     | 24px  |
| my-8     | margin-top: 2rem; margin-bottom: 2rem;           | 32px  |
| mx-8     | margin-left: 2rem; margin-right: 2rem;           | 32px  |
| my-9     | margin-top: 2.25rem; margin-bottom: 2.25rem;     | 36px  |
| mx-9     | margin-left: 2.25rem; margin-right: 2.25rem;     | 36px  |
| my-10    | margin-top: 2.5rem; margin-bottom: 2.5rem;       | 40px  |
| mx-10    | margin-left: 2.5rem; margin-right: 2.5rem;       | 40px  |
| my-11    | margin-top: 2.75rem; margin-bottom: 2.75rem;     | 44px  |
| mx-11    | margin-left: 2.75rem; margin-right: 2.75rem;     | 44px  |
| my-12    | margin-top: 3rem; margin-bottom: 3rem;           | 48px  |
| mx-12    | margin-left: 3rem; margin-right: 3rem;           | 48px  |
| my-14    | margin-top: 3.5rem; margin-bottom: 3.5rem;       | 56px  |
| mx-14    | margin-left: 3.5rem; margin-right: 3.5rem;       | 56px  |
| my-16    | margin-top: 4rem; margin-bottom: 4rem;           | 64px  |
| mx-16    | margin-left: 4rem; margin-right: 4rem;           | 64px  |
| my-20    | margin-top: 5rem; margin-bottom: 5rem;           | 80px  |
| mx-20    | margin-left: 5rem; margin-right: 5rem;           | 80px  |
| my-24    | margin-top: 6rem; margin-bottom: 6rem;           | 96px  |
| mx-24    | margin-left: 6rem; margin-right: 6rem;           | 96px  |
| my-28    | margin-top: 7rem; margin-bottom: 7rem;           | 112px |
| mx-28    | margin-left: 7rem; margin-right: 7rem;           | 112px |
| my-32    | margin-top: 8rem; margin-bottom: 8rem;           | 128px |
| mx-32    | margin-left: 8rem; margin-right: 8rem;           | 128px |
| my-36    | margin-top: 9rem; margin-bottom: 9rem;           | 144px |
| mx-36    | margin-left: 9rem; margin-right: 9rem;           | 144px |
| my-40    | margin-top: 10rem; margin-bottom: 10rem;         | 160px |
| mx-40    | margin-left: 10rem; margin-right: 10rem;         | 160px |
| my-44    | margin-top: 11rem; margin-bottom: 11rem;         | 176px |
| mx-44    | margin-left: 11rem; margin-right: 11rem;         | 176px |
| my-48    | margin-top: 12rem; margin-bottom: 12rem;         | 192px |
| mx-48    | margin-left: 12rem; margin-right: 12rem;         | 192px |
| my-52    | margin-top: 13rem; margin-bottom: 13rem;         | 208px |
| mx-52    | margin-left: 13rem; margin-right: 13rem;         | 208px |
| my-56    | margin-top: 14rem; margin-bottom: 14rem;         | 224px |
| mx-56    | margin-left: 14rem; margin-right: 14rem;         | 224px |
| my-60    | margin-top: 15rem; margin-bottom: 15rem;         | 240px |
| mx-60    | margin-left: 15rem; margin-right: 15rem;         | 240px |
| my-64    | margin-top: 16rem; margin-bottom: 16rem;         | 256px |
| mx-64    | margin-left: 16rem; margin-right: 16rem;         | 256px |
| my-70    | margin-top: 18rem; margin-bottom: 18rem;         | 280px |
| mx-70    | margin-left: 18rem; margin-right: 18rem;         | 280px |
| my-80    | margin-top: 20rem; margin-bottom: 20rem;         | 320px |
| mx-80    | margin-left: 20rem; margin-right: 20rem;         | 320px |
| my-96    | margin-top: 24rem; margin-bottom: 24rem;         | 384px |
| mx-96    | margin-left: 24rem; margin-right: 24rem;         | 384px |
| my-px    | margin-top: 1px; margin-bottom: 1px;             |       |
| mx-px    | margin-left: 1px; margin-right: 1px;             |       |
| mt-0     | margin-top: 0;                                   |       |
| mr-0     | margin-right: 0;                                 |       |
| mb-0     | margin-bottom: 0;                                |       |
| ml-0     | margin-left: 0;                                  |       |
| mt-0.5   | margin-top: 0.125rem;                            | 2px   |
| mr-0.5   | margin-right: 0.125rem;                          | 2px   |
| mb-0.5   | margin-bottom: 0.125rem;                         | 2px   |
| ml-0.5   | margin-left: 0.125rem;                           | 2px   |
| mt-1     | margin-top: 0.25rem;                             | 4px   |
| mr-1     | margin-right: 0.25rem;                           | 4px   |
| mb-1     | margin-bottom: 0.25rem;                          | 4px   |
| ml-1     | margin-left: 0.25rem;                            | 4px   |
| mt-1.5   | margin-top: 0.375rem;                            | 6px   |
| mr-1.5   | margin-right: 0.375rem;                          | 6px   |
| mb-1.5   | margin-bottom: 0.375rem;                         | 6px   |
| ml-1.5   | margin-left: 0.375rem;                           | 6px   |
| mt-2     | margin-top: 0.5rem;                              | 8px   |
| mr-2     | margin-right: 0.5rem;                            | 8px   |
| mb-2     | margin-bottom: 0.5rem;                           | 8px   |
| ml-2     | margin-left: 0.5rem;                             | 8px   |
| mt-2.5   | margin-top: 0.625rem;                            | 10px  |
| mr-2.5   | margin-right: 0.625rem;                          | 10px  |
| mb-2.5   | margin-bottom: 0.625rem;                         | 10px  |
| ml-2.5   | margin-left: 0.625rem;                           | 10px  |
| mt-3     | margin-top: 0.75rem;                             | 12px  |
| mr-3     | margin-right: 0.75rem;                           | 12px  |
| mb-3     | margin-bottom: 0.75rem;                          | 12px  |
| ml-3     | margin-left: 0.75rem;                            | 12px  |
| mt-3.5   | margin-top: 0.875rem;                            | 14px  |
| mr-3.5   | margin-right: 0.875rem;                          | 14px  |
| mb-3.5   | margin-bottom: 0.875rem;                         | 14px  |
| ml-3.5   | margin-left: 0.875rem;                           | 14px  |
| mt-4     | margin-top: 1rem;                                | 16px  |
| mr-4     | margin-right: 1rem;                              | 16px  |
| mb-4     | margin-bottom: 1rem;                             | 16px  |
| ml-4     | margin-left: 1rem;                               | 16px  |
| mt-5     | margin-top: 1.25rem;                             | 20px  |
| mr-5     | margin-right: 1.25rem;                           | 20px  |
| mb-5     | margin-bottom: 1.25rem;                          | 20px  |
| ml-5     | margin-left: 1.25rem;                            | 20px  |
| mt-6     | margin-top: 1.5rem;                              | 24px  |
| mr-6     | margin-right: 1.5rem;                            | 24px  |
| mb-6     | margin-bottom: 1.5rem;                           | 24px  |
| ml-6     | margin-left: 1.5rem;                             | 24px  |
| mt-7     | margin-top: 1.75rem;                             | 28px  |
| mr-7     | margin-right: 1.75rem;                           | 28px  |
| mb-7     | margin-bottom: 1.75rem;                          | 28px  |
| ml-7     | margin-left: 1.75rem;                            | 28px  |
| mt-8     | margin-top: 2rem;                                | 32px  |
| mr-8     | margin-right: 2rem;                              | 32px  |
| mb-8     | margin-bottom: 2rem;                             | 32px  |
| ml-8     | margin-left: 2rem;                               | 32px  |
| mt-9     | margin-top: 2.25rem;                             | 36px  |
| mr-9     | margin-right: 2.25rem;                           | 36px  |
| mb-9     | margin-bottom: 2.25rem;                          | 36px  |
| ml-9     | margin-left: 2.25rem;                            | 36px  |
| mt-10    | margin-top: 2.5rem;                              | 40px  |
| mr-10    | margin-right: 2.5rem;                            | 40px  |
| mb-10    | margin-bottom: 2.5rem;                           | 40px  |
| ml-10    | margin-left: 2.5rem;                             | 40px  |
| mt-11    | margin-top: 2.75rem;                             | 44px  |
| mr-11    | margin-right: 2.75rem;                           | 44px  |
| mb-11    | margin-bottom: 2.75rem;                          | 44px  |
| ml-11    | margin-left: 2.75rem;                            | 44px  |
| mt-12    | margin-top: 3rem;                                | 48px  |
| mr-12    | margin-right: 3rem;                              | 48px  |
| mb-12    | margin-bottom: 3rem;                             | 48px  |
| ml-12    | margin-left: 3rem;                               | 48px  |
| mt-14    | margin-top: 3.5rem;                              | 56px  |
| mr-14    | margin-right: 3.5rem;                            | 56px  |
| mb-14    | margin-bottom: 3.5rem;                           | 56px  |
| ml-14    | margin-left: 3.5rem;                             | 56px  |
| mt-16    | margin-top: 4rem;                                | 64px  |
| mr-16    | margin-right: 4rem;                              | 64px  |
| mb-16    | margin-bottom: 4rem;                             | 64px  |
| ml-16    | margin-left: 4rem;                               | 64px  |
| mt-20    | margin-top: 5rem;                                | 80px  |
| mr-20    | margin-right: 5rem;                              | 80px  |
| mb-20    | margin-bottom: 5rem;                             | 80px  |
| ml-20    | margin-left: 5rem;                               | 80px  |
| mt-24    | margin-top: 6rem;                                | 96px  |
| mr-24    | margin-right: 6rem;                              | 96px  |
| mb-24    | margin-bottom: 6rem;                             | 96px  |
| ml-24    | margin-left: 6rem;                               | 96px  |
| mt-28    | margin-top: 7rem;                                | 112px |
| mr-28    | margin-right: 7rem;                              | 112px |
| mb-28    | margin-bottom: 7rem;                             | 112px |
| ml-28    | margin-left: 7rem;                               | 112px |
| mt-32    | margin-top: 8rem;                                | 128px |
| mr-32    | margin-right: 8rem;                              | 128px |
| mb-32    | margin-bottom: 8rem;                             | 128px |
| ml-32    | margin-left: 8rem;                               | 128px |
| mt-36    | margin-top: 9rem;                                | 144px |
| mr-36    | margin-right: 9rem;                              | 144px |
| mb-36    | margin-bottom: 9rem;                             | 144px |
| ml-36    | margin-left: 9rem;                               | 144px |
| mt-40    | margin-top: 10rem;                               | 160px |
| mr-40    | margin-right: 10rem;                             | 160px |
| mb-40    | margin-bottom: 10rem;                            | 160px |
| ml-40    | margin-left: 10rem;                              | 160px |
| mt-44    | margin-top: 11rem;                               | 176px |
| mr-44    | margin-right: 11rem;                             | 176px |
| mb-44    | margin-bottom: 11rem;                            | 176px |
| ml-44    | margin-left: 11rem;                              | 176px |
| mt-48    | margin-top: 12rem;                               | 192px |
| mr-48    | margin-right: 12rem;                             | 192px |
| mb-48    | margin-bottom: 12rem;                            | 192px |
| ml-48    | margin-left: 12rem;                              | 192px |
| mt-52    | margin-top: 13rem;                               | 208px |
| mr-52    | margin-right: 13rem;                             | 208px |
| mb-52    | margin-bottom: 13rem;                            | 208px |
| ml-52    | margin-left: 13rem;                              | 208px |
| mt-56    | margin-top: 14rem;                               | 224px |
| mr-56    | margin-right: 14rem;                             | 224px |
| mb-56    | margin-bottom: 14rem;                            | 224px |
| ml-56    | margin-left: 14rem;                              | 224px |
| mt-60    | margin-top: 15rem;                               | 240px |
| mr-60    | margin-right: 15rem;                             | 240px |
| mb-60    | margin-bottom: 15rem;                            | 240px |
| ml-60    | margin-left: 15rem;                              | 240px |
| mt-64    | margin-top: 16rem;                               | 256px |
| mr-64    | margin-right: 16rem;                             | 256px |
| mb-64    | margin-bottom: 16rem;                            | 256px |
| ml-64    | margin-left: 16rem;                              | 256px |
| mt-72    | margin-top: 18rem;                               | 288px |
| mr-72    | margin-right: 18rem;                             | 288px |
| mb-72    | margin-bottom: 18rem;                            | 288px |
| ml-72    | margin-left: 18rem;                              | 288px |
| mt-80    | margin-top: 20rem;                               | 320px |
| mr-80    | margin-right: 20rem;                             | 320px |
| mb-80    | margin-bottom: 20rem;                            | 320px |
| ml-80    | margin-left: 20rem;                              | 320px |
| mt-96    | margin-top: 24rem;                               | 384px |
| mr-96    | margin-right: 24rem;                             | 384px |
| mb-96    | margin-bottom: 24rem;                            | 384px |
| ml-96    | margin-left: 24rem;                              | 384px |
| mt-px    | margin-top: 1px;                                 |       |
| mr-px    | margin-right: 1px;                               |       |
| mb-px    | margin-bottom: 1px;                              |       |
| ml-px    | margin-left: 1px;                                |       |
| -m-0     | margin: 0;                                       |       |
| -m-0.5   | margin: -0.125rem;                               | 2px   |
| -m-1     | margin: -0.25rem;                                | 4px   |
| -m-1.5   | margin: -0.375rem;                               | 6px   |
| -m-2     | margin: -0.5rem;                                 | 8px   |
| -m-2.5   | margin: -0.625rem;                               | 10px  |
| -m-3     | margin: -0.75rem;                                | 12px  |
| -m-3.5   | margin: -0.875rem;                               | 14px  |
| -m-4     | margin: -1rem;                                   | 16px  |
| -m-5     | margin: -1.25rem;                                | 20px  |
| -m-6     | margin: -1.5rem;                                 | 24px  |
| -m-8     | margin: -2rem;                                   | 32px  |
| -m-10    | margin: -2.5rem;                                 | 40px  |
| -m-11    | margin: -2.75rem;                                | 44px  |
| -m-12    | margin: -3rem;                                   | 48px  |
| -m-14    | margin: -3.5rem;                                 | 56px  |
| -m-16    | margin: -4rem;                                   | 64px  |
| -m-20    | margin: -5rem;                                   | 80px  |
| -m-24    | margin: -6rem;                                   | 96px  |
| -m-28    | margin: -7rem;                                   | 112px |
| -m-32    | margin: -8rem;                                   | 128px |
| -m-36    | margin: -9rem;                                   | 144px |
| -m-40    | margin: -10rem;                                  | 160px |
| -m-44    | margin: -11rem;                                  | 176px |
| -m-48    | margin: -12rem;                                  | 192px |
| -m-52    | margin: -13rem;                                  | 208px |
| -m-56    | margin: -14rem;                                  | 224px |
| -m-64    | margin: -16rem;                                  | 256px |
| -m-72    | margin: -18rem;                                  | 288px |
| -m-80    | margin: -20rem;                                  | 320px |
| -m-96    | margin: -24rem;                                  | 384px |
| -m-px    | margin: -1px;                                    |       |
| -my-0    | margin-top: 0; margin-bottom: 0;                 |       |
| -mx-0    | margin-left: 0; margin-right: 0;                 |       |
| -my-0.5  | margin-top: -0.125rem; margin-bottom: -0.125rem; | 2px   |
| -mx-0.5  | margin-left: -0.125rem; margin-right: -0.125rem; | 2px   |
| -my-1    | margin-top: -0.25rem; margin-bottom: -0.25rem;   | 4px   |
| -mx-1    | margin-left: -0.25rem; margin-right: -0.25rem;   | 4px   |
| -my-1.5  | margin-top: -0.375rem; margin-bottom: -0.375rem; | 6px   |
| -mx-1.5  | margin-left: -0.375rem; margin-right: -0.375rem; | 6px   |
| -my-2    | margin-top: -0.5rem; margin-bottom: -0.5rem;     | 8px   |
| -mx-2    | margin-left: -0.5rem; margin-right: -0.5rem;     | 8px   |
| -my-2.5  | margin-top: -0.625rem; margin-bottom: -0.625rem; | 10px  |
| -mx-2.5  | margin-left: -0.625rem; margin-right: -0.625rem; | 10px  |
| -my-3    | margin-top: -0.75rem; margin-bottom: -0.75rem;   | 12px  |
| -mx-3    | margin-left: -0.75rem; margin-right: -0.75rem;   | 12px  |
| -my-3.5  | margin-top: -0.875rem; margin-bottom: -0.875rem; | 14px  |
| -mx-3.5  | margin-left: -0.875rem; margin-right: -0.875rem; | 14px  |
| -my-4    | margin-top: -1rem; margin-bottom: -1rem;         | 16px  |
| -mx-4    | margin-left: -1rem; margin-right: -1rem;         | 16px  |
| -my-5    | margin-top: -1.25rem; margin-bottom: -1.25rem;   | 20px  |
| -mx-5    | margin-left: -1.25rem; margin-right: -1.25rem;   | 20px  |
| -my-6    | margin-top: -1.5rem; margin-bottom: -1.5rem;     | 24px  |
| -mx-6    | margin-left: -1.5rem; margin-right: -1.5rem;     | 24px  |
| -my-7    | margin-top: 1.75rem; margin-bottom: 1.75rem;     | 24px  |
| -mx-7    | margin-left: 1.75rem; margin-right: 1.75rem;     | 24px  |
| -my-8    | margin-top: -2rem; margin-bottom: -2rem;         | 32px  |
| -mx-8    | margin-left: -2rem; margin-right: -2rem;         | 32px  |
| -my-9    | margin-top: 2.25rem; margin-bottom: 2.25rem;     | 36px  |
| -mx-9    | margin-left: 2.25rem; margin-right: 2.25rem;     | 36px  |
| -my-10   | margin-top: -2.5rem; margin-bottom: -2.5rem;     | 40px  |
| -mx-10   | margin-left: -2.5rem; margin-right: -2.5rem;     | 40px  |
| -my-11   | margin-top: -2.75rem; margin-bottom: -2.75rem;   | 44px  |
| -mx-11   | margin-left: -2.75rem; margin-right: -2.75rem;   | 44px  |
| -my-12   | margin-top: -3rem; margin-bottom: -3rem;         | 48px  |
| -mx-12   | margin-left: -3rem; margin-right: -3rem;         | 48px  |
| -my-14   | margin-top: -3.5rem; margin-bottom: -3.5rem;     | 56px  |
| -mx-14   | margin-left: -3.5rem; margin-right: -3.5rem;     | 56px  |
| -my-16   | margin-top: -4rem; margin-bottom: -4rem;         | 64px  |
| -mx-16   | margin-left: -4rem; margin-right: -4rem;         | 64px  |
| -my-20   | margin-top: -5rem; margin-bottom: -5rem;         | 80px  |
| -mx-20   | margin-left: -5rem; margin-right: -5rem;         | 80px  |
| -my-24   | margin-top: -6rem; margin-bottom: -6rem;         | 96px  |
| -mx-24   | margin-left: -6rem; margin-right: -6rem;         | 96px  |
| -my-28   | margin-top: -7rem; margin-bottom: -7rem;         | 112px |
| -mx-28   | margin-left: -7rem; margin-right: -7rem;         | 112px |
| -my-32   | margin-top: -8rem; margin-bottom: -8rem;         | 128px |
| -mx-32   | margin-left: -8rem; margin-right: -8rem;         | 128px |
| -my-36   | margin-top: -9rem; margin-bottom: -9rem;         | 144px |
| -mx-36   | margin-left: -9rem; margin-right: -9rem;         | 144px |
| -my-40   | margin-top: -10rem; margin-bottom: -10rem;       | 160px |
| -mx-40   | margin-left: -10rem; margin-right: -10rem;       | 160px |
| -my-44   | margin-top: -11rem; margin-bottom: -11rem;       | 176px |
| -mx-44   | margin-left: -11rem; margin-right: -11rem;       | 176px |
| -my-48   | margin-top: -12rem; margin-bottom: -12rem;       | 192px |
| -mx-48   | margin-left: -12rem; margin-right: -12rem;       | 192px |
| -my-52   | margin-top: -13rem; margin-bottom: -13rem;       | 208px |
| -mx-52   | margin-left: -13rem; margin-right: -13rem;       | 208px |
| -my-56   | margin-top: -14rem; margin-bottom: -14rem;       | 224px |
| -mx-56   | margin-left: -14rem; margin-right: -14rem;       | 224px |
| -my-60   | margin-top: 15rem; margin-bottom: 15rem;         | 240px |
| -mx-60   | margin-left: 15rem; margin-right: 15rem;         | 240px |
| -my-64   | margin-top: -16rem; margin-bottom: -16rem;       | 256px |
| -mx-64   | margin-left: -16rem; margin-right: -16rem;       | 256px |
| -my-70   | margin-top: -18rem; margin-bottom: -18rem;       | 280px |
| -mx-70   | margin-left: -18rem; margin-right: -18rem;       | 280px |
| -my-80   | margin-top: -20rem; margin-bottom: -20rem;       | 320px |
| -mx-80   | margin-left: -20rem; margin-right: -20rem;       | 320px |
| -my-96   | margin-top: -24rem; margin-bottom: -24rem;       | 384px |
| -mx-96   | margin-left: -24rem; margin-right: -24rem;       | 384px |
| -my-px   | margin-top: -1px; margin-bottom: -1px;           |       |
| -mx-px   | margin-left: -1px; margin-right: -1px;           |       |
| -mt-0    | margin-top: 0;                                   |       |
| -mr-0    | margin-right: 0;                                 |       |
| -mb-0    | margin-bottom: 0;                                |       |
| -ml-0    | margin-left: 0;                                  |       |
| -mt-0.5  | margin-top: -0.125rem;                           | 2px   |
| -mr-0.5  | margin-right: -0.125rem;                         | 2px   |
| -mb-0.5  | margin-bottom: -0.125rem;                        | 2px   |
| -ml-0.5  | margin-left: -0.125rem;                          | 2px   |
| -mt-1    | margin-top: -0.25rem;                            | 4px   |
| -mr-1    | margin-right: -0.25rem;                          | 4px   |
| -mb-1    | margin-bottom: -0.25rem;                         | 4px   |
| -ml-1    | margin-left: -0.25rem;                           | 4px   |
| -mt-1.5  | margin-top: -0.375rem;                           | 6px   |
| -mr-1.5  | margin-right: -0.375rem;                         | 6px   |
| -mb-1.5  | margin-bottom: -0.375rem;                        | 6px   |
| -ml-1.5  | margin-left: -0.375rem;                          | 6px   |
| -mt-2    | margin-top: -0.5rem;                             | 8px   |
| -mr-2    | margin-right: -0.5rem;                           | 8px   |
| -mb-2    | margin-bottom: -0.5rem;                          | 8px   |
| -ml-2    | margin-left: -0.5rem;                            | 8px   |
| -mt-2.5  | margin-top: -0.625rem;                           | 10px  |
| -mr-2.5  | margin-right: -0.625rem;                         | 10px  |
| -mb-2.5  | margin-bottom: -0.625rem;                        | 10px  |
| -ml-2.5  | margin-left: -0.625rem;                          | 10px  |
| -mt-3    | margin-top: -0.75rem;                            | 12px  |
| -mr-3    | margin-right: -0.75rem;                          | 12px  |
| -mb-3    | margin-bottom: -0.75rem;                         | 12px  |
| -ml-3    | margin-left: -0.75rem;                           | 12px  |
| -mt-3.5  | margin-top: -0.875rem;                           | 14px  |
| -mr-3.5  | margin-right: -0.875rem;                         | 14px  |
| -mb-3.5  | margin-bottom: -0.875rem;                        | 14px  |
| -ml-3.5  | margin-left: -0.875rem;                          | 14px  |
| -mt-4    | margin-top: -1rem;                               | 16px  |
| -mr-4    | margin-right: -1rem;                             | 16px  |
| -mb-4    | margin-bottom: -1rem;                            | 16px  |
| -ml-4    | margin-left: -1rem;                              | 16px  |
| -mt-5    | margin-top: -1.25rem;                            | 20px  |
| -mr-5    | margin-right: -1.25rem;                          | 20px  |
| -mb-5    | margin-bottom: -1.25rem;                         | 20px  |
| -ml-5    | margin-left: -1.25rem;                           | 20px  |
| -mt-6    | margin-top: -1.5rem;                             | 24px  |
| -mr-6    | margin-right: -1.5rem;                           | 24px  |
| -mb-6    | margin-bottom: -1.5rem;                          | 24px  |
| -ml-6    | margin-left: -1.5rem;                            | 24px  |
| -mt-7    | margin-top: 1.75rem;                             | 28px  |
| -mr-7    | margin-right: 1.75rem;                           | 28px  |
| -mb-7    | margin-bottom: 1.75rem;                          | 28px  |
| -ml-7    | margin-left: 1.75rem;                            | 28px  |
| -mt-8    | margin-top: -2rem;                               | 32px  |
| -mr-8    | margin-right: -2rem;                             | 32px  |
| -mb-8    | margin-bottom: -2rem;                            | 32px  |
| -ml-8    | margin-left: -2rem;                              | 32px  |
| -mt-9    | margin-top: 2.25rem;                             | 36px  |
| -mr-9    | margin-right: 2.25rem;                           | 36px  |
| -mb-9    | margin-bottom: 2.25rem;                          | 36px  |
| -ml-9    | margin-left: 2.25rem;                            | 36px  |
| -mt-10   | margin-top: -2.5rem;                             | 40px  |
| -mr-10   | margin-right: -2.5rem;                           | 40px  |
| -mb-10   | margin-bottom: -2.5rem;                          | 40px  |
| -ml-10   | margin-left: -2.5rem;                            | 40px  |
| -mt-11   | margin-top: -2.75rem;                            | 44px  |
| -mr-11   | margin-right: -2.75rem;                          | 44px  |
| -mb-11   | margin-bottom: -2.75rem;                         | 44px  |
| -ml-11   | margin-left: -2.75rem;                           | 44px  |
| -mt-12   | margin-top: -3rem;                               | 48px  |
| -mr-12   | margin-right: -3rem;                             | 48px  |
| -mb-12   | margin-bottom: -3rem;                            | 48px  |
| -ml-12   | margin-left: -3rem;                              | 48px  |
| -mt-14   | margin-top: -3.5rem;                             | 56px  |
| -mr-14   | margin-right: -3.5rem;                           | 56px  |
| -mb-14   | margin-bottom: -3.5rem;                          | 56px  |
| -ml-14   | margin-left: -3.5rem;                            | 56px  |
| -mt-16   | margin-top: -4rem;                               | 64px  |
| -mr-16   | margin-right: -4rem;                             | 64px  |
| -mb-16   | margin-bottom: -4rem;                            | 64px  |
| -ml-16   | margin-left: -4rem;                              | 64px  |
| -mt-20   | margin-top: -5rem;                               | 80px  |
| -mr-20   | margin-right: -5rem;                             | 80px  |
| -mb-20   | margin-bottom: -5rem;                            | 80px  |
| -ml-20   | margin-left: -5rem;                              | 80px  |
| -mt-24   | margin-top: -6rem;                               | 96px  |
| -mr-24   | margin-right: -6rem;                             | 96px  |
| -mb-24   | margin-bottom: -6rem;                            | 96px  |
| -ml-24   | margin-left: -6rem;                              | 96px  |
| -mt-28   | margin-top: -7rem;                               | 112px |
| -mr-28   | margin-right: -7rem;                             | 112px |
| -mb-28   | margin-bottom: -7rem;                            | 112px |
| -ml-28   | margin-left: -7rem;                              | 112px |
| -mt-32   | margin-top: -8rem;                               | 128px |
| -mr-32   | margin-right: -8rem;                             | 128px |
| -mb-32   | margin-bottom: -8rem;                            | 128px |
| -ml-32   | margin-left: -8rem;                              | 128px |
| -mt-36   | margin-top: -9rem;                               | 144px |
| -mr-36   | margin-right: -9rem;                             | 144px |
| -mb-36   | margin-bottom: -9rem;                            | 144px |
| -ml-36   | margin-left: -9rem;                              | 144px |
| -mt-40   | margin-top: -10rem;                              | 160px |
| -mr-40   | margin-right: -10rem;                            | 160px |
| -mb-40   | margin-bottom: -10rem;                           | 160px |
| -ml-40   | margin-left: -10rem;                             | 160px |
| -mt-44   | margin-top: -11rem;                              | 176px |
| -mr-44   | margin-right: -11rem;                            | 176px |
| -mb-44   | margin-bottom: -11rem;                           | 176px |
| -ml-44   | margin-left: -11rem;                             | 176px |
| -mt-48   | margin-top: -12rem;                              | 192px |
| -mr-48   | margin-right: -12rem;                            | 192px |
| -mb-48   | margin-bottom: -12rem;                           | 192px |
| -ml-48   | margin-left: -12rem;                             | 192px |
| -mt-52   | margin-top: -13rem;                              | 208px |
| -mr-52   | margin-right: -13rem;                            | 208px |
| -mb-52   | margin-bottom: -13rem;                           | 208px |
| -ml-52   | margin-left: -13rem;                             | 208px |
| -mt-56   | margin-top: -14rem;                              | 224px |
| -mr-56   | margin-right: -14rem;                            | 224px |
| -mb-56   | margin-bottom: -14rem;                           | 224px |
| -ml-56   | margin-left: -14rem;                             | 224px |
| -mt-60   | margin-top: 15rem;                               | 240px |
| -mr-60   | margin-right: 15rem;                             | 240px |
| -mb-60   | margin-bottom: 15rem;                            | 240px |
| -ml-60   | margin-left: 15rem;                              | 240px |
| -mt-64   | margin-top: -16rem;                              | 256px |
| -mr-64   | margin-right: -16rem;                            | 256px |
| -mb-64   | margin-bottom: -16rem;                           | 256px |
| -ml-64   | margin-left: -16rem;                             | 256px |
| -mt-72   | margin-top: -18rem;                              | 288px |
| -mr-72   | margin-right: -18rem;                            | 288px |
| -mb-72   | margin-bottom: -18rem;                           | 288px |
| -ml-72   | margin-left: -18rem;                             | 288px |
| -mt-80   | margin-top: -20rem;                              | 320px |
| -mr-80   | margin-right: -20rem;                            | 320px |
| -mb-80   | margin-bottom: -20rem;                           | 320px |
| -ml-80   | margin-left: -20rem;                             | 320px |
| -mt-96   | margin-top: -24rem;                              | 384px |
| -mr-96   | margin-right: -24rem;                            | 384px |
| -mb-96   | margin-bottom: -24rem;                           | 384px |
| -ml-96   | margin-left: -24rem;                             | 384px |
| -mt-px   | margin-top: -1px;                                |       |
| -mr-px   | margin-right: -1px;                              |       |
| -mb-px   | margin-bottom: -1px;                             |       |
| -ml-px   | margin-left: -1px;                               |       |





### Space Between
Controls margin between child elements

| Tailwind        | Description             | Other |
| --------------- | ----------------------- | ----- |
| space-x-0       | margin-left: 0;         |       |
| space-x-0.5     | margin-left: 0.125rem;  |       |
| space-x-1       | margin-left: 0.25rem;   |       |
| space-x-1.5     | margin-left: 0.375rem;  |       |
| space-x-2       | margin-left: 0.5rem;    |       |
| space-x-2.5     | margin-left: 0.625rem;  |       |
| space-x-3       | margin-left: 0.75rem;   |       |
| space-x-3       | margin-left: 0.875rem;  |       |
| space-x-4       | margin-left: 1rem;      |       |
| space-x-5       | margin-left: 1.25rem;   |       |
| space-x-6       | margin-left: 1.5rem;    |       |
| space-x-7       | margin-left: 1.75rem;   |       |
| space-x-8       | margin-left: 2rem;      |       |
| space-x-9       | margin-left: 2.25rem;   |       |
| space-x-10      | margin-left: 2.5rem;    |       |
| space-x-11      | margin-left: 2.75rem;   |       |
| space-x-12      | margin-left: 3rem;      |       |
| space-x-14      | margin-left: 3.5rem;    |       |
| space-x-16      | margin-left: 4rem;      |       |
| space-x-20      | margin-left: 5rem;      |       |
| space-x-24      | margin-left: 6rem;      |       |
| space-x-28      | margin-left: 7rem;      |       |
| space-x-32      | margin-left: 8rem;      |       |
| space-x-36      | margin-left: 9rem;      |       |
| space-x-40      | margin-left: 10rem;     |       |
| space-x-44      | margin-left: 11rem;     |       |
| space-x-48      | margin-left: 12rem;     |       |
| space-x-52      | margin-left: 13rem;     |       |
| space-x-56      | margin-left: 14rem;     |       |
| space-x-60      | margin-left: 15rem;     |       |
| space-x-64      | margin-left: 16rem;     |       |
| space-x-72      | margin-left: 18rem;     |       |
| space-x-80      | margin-left: 20rem;     |       |
| space-x-96      | margin-left: 24rem;     |       |
| space-x-px      | margin-left: 1px;       |       |
| -space-x-0      | margin-left: 0;         |       |
| -space-x-0.5    | margin-left: -0.125rem; |       |
| -space-x-1      | margin-left: -0.25rem;  |       |
| -space-x-1.5    | margin-left: -0.375rem; |       |
| -space-x-2      | margin-left: -0.5rem;   |       |
| -space-x-2.5    | margin-left: -0.625rem; |       |
| -space-x-3      | margin-left: -0.75rem;  |       |
| -space-x-3      | margin-left: -0.875rem; |       |
| -space-x-4      | margin-left: -1rem;     |       |
| -space-x-5      | margin-left: -1.25rem;  |       |
| -space-x-6      | margin-left: -1.5rem;   |       |
| -space-x-7      | margin-left: -1.75rem;  |       |
| -space-x-8      | margin-left: -2rem;     |       |
| -space-x-9      | margin-left: -2.25rem;  |       |
| -space-x-10     | margin-left: -2.5rem;   |       |
| -space-x-11     | margin-left: -2.75rem;  |       |
| -space-x-12     | margin-left: -3rem;     |       |
| -space-x-14     | margin-left: -3.5rem;   |       |
| -space-x-16     | margin-left: -4rem;     |       |
| -space-x-20     | margin-left: -5rem;     |       |
| -space-x-24     | margin-left: -6rem;     |       |
| -space-x-28     | margin-left: -7rem;     |       |
| -space-x-32     | margin-left: -8rem;     |       |
| -space-x-36     | margin-left: -9rem;     |       |
| -space-x-40     | margin-left: -10rem;    |       |
| -space-x-44     | margin-left: -11rem;    |       |
| -space-x-48     | margin-left: -12rem;    |       |
| -space-x-52     | margin-left: -13rem;    |       |
| -space-x-56     | margin-left: -14rem;    |       |
| -space-x-60     | margin-left: -15rem;    |       |
| -space-x-64     | margin-left: -16rem;    |       |
| -space-x-72     | margin-left: -18rem;    |       |
| -space-x-80     | margin-left: -20rem;    |       |
| -space-x-96     | margin-left: -24rem;    |       |
| -space-x-px     | margin-left: -1px;      |       |
| space-y-0       | margin-top: 0;          |       |
| space-y-0.5     | margin-top: 0.125rem;   |       |
| space-y-1       | margin-top: 0.25rem;    |       |
| space-y-1.5     | margin-top: 0.375rem;   |       |
| space-y-2       | margin-top: 0.5rem;     |       |
| space-y-2.5     | margin-top: 0.625rem;   |       |
| space-y-3       | margin-top: 0.75rem;    |       |
| space-y-3       | margin-top: 0.875rem;   |       |
| space-y-4       | margin-top: 1rem;       |       |
| space-y-5       | margin-top: 1.25rem;    |       |
| space-y-6       | margin-top: 1.5rem;     |       |
| space-y-7       | margin-top: 1.75rem;    |       |
| space-y-8       | margin-top: 2rem;       |       |
| space-y-9       | margin-top: 2.25rem;    |       |
| space-y-10      | margin-top: 2.5rem;     |       |
| space-y-11      | margin-top: 2.75rem;    |       |
| space-y-12      | margin-top: 3rem;       |       |
| space-y-14      | margin-top: 3.5rem;     |       |
| space-y-16      | margin-top: 4rem;       |       |
| space-y-20      | margin-top: 5rem;       |       |
| space-y-24      | margin-top: 6rem;       |       |
| space-y-28      | margin-top: 7rem;       |       |
| space-y-32      | margin-top: 8rem;       |       |
| space-y-36      | margin-top: 9rem;       |       |
| space-y-40      | margin-top: 10rem;      |       |
| space-y-44      | margin-top: 11rem;      |       |
| space-y-48      | margin-top: 12rem;      |       |
| space-y-52      | margin-top: 13rem;      |       |
| space-y-56      | margin-top: 14rem;      |       |
| space-y-60      | margin-top: 15rem;      |       |
| space-y-64      | margin-top: 16rem;      |       |
| space-y-72      | margin-top: 18rem;      |       |
| space-y-80      | margin-top: 20rem;      |       |
| space-y-96      | margin-top: 24rem;      |       |
| space-y-px      | margin-top: 1px;        |       |
| -space-y-0      | margin-top: 0;          |       |
| -space-y-0.5    | margin-top: -0.125rem;  |       |
| -space-y-1      | margin-top: -0.25rem;   |       |
| -space-y-1.5    | margin-top: -0.375rem;  |       |
| -space-y-2      | margin-top: -0.5rem;    |       |
| -space-y-2.5    | margin-top: -0.625rem;  |       |
| -space-y-3      | margin-top: -0.75rem;   |       |
| -space-y-3      | margin-top: -0.875rem;  |       |
| -space-y-4      | margin-top: -1rem;      |       |
| -space-y-5      | margin-top: -1.25rem;   |       |
| -space-y-6      | margin-top: -1.5rem;    |       |
| -space-y-7      | margin-top: -1.75rem;   |       |
| -space-y-8      | margin-top: -2rem;      |       |
| -space-y-9      | margin-top: -2.25rem;   |       |
| -space-y-10     | margin-top: -2.5rem;    |       |
| -space-y-11     | margin-top: -2.75rem;   |       |
| -space-y-12     | margin-top: -3rem;      |       |
| -space-y-14     | margin-top: -3.5rem;    |       |
| -space-y-16     | margin-top: -4rem;      |       |
| -space-y-20     | margin-top: -5rem;      |       |
| -space-y-24     | margin-top: -6rem;      |       |
| -space-y-28     | margin-top: -7rem;      |       |
| -space-y-32     | margin-top: -8rem;      |       |
| -space-y-36     | margin-top: -9rem;      |       |
| -space-y-40     | margin-top: -10rem;     |       |
| -space-y-44     | margin-top: -11rem;     |       |
| -space-y-48     | margin-top: -12rem;     |       |
| -space-y-52     | margin-top: -13rem;     |       |
| -space-y-56     | margin-top: -14rem;     |       |
| -space-y-60     | margin-top: -15rem;     |       |
| -space-y-64     | margin-top: -16rem;     |       |
| -space-y-72     | margin-top: -18rem;     |       |
| -space-y-80     | margin-top: -20rem;     |       |
| -space-y-96     | margin-top: -24rem;     |       |
| -space-y-px     | margin-top: -1px;       |       |
| space-x-reverse | --space-x-reverse: 1    |       |
| space-y-reverse | --space-y-reverse: 1    |       |



---




## Typography


### Font Family
Sets the font family.

| Tailwind   | Description                                                                                                                                                                                                    | Other |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| font-sans  | font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"; |       |
| font-serif | font-family: Georgia, Cambria, "Times New Roman", Times, serif;                                                                                                                                                |       |
| font-mono  | font-family: Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;                                                                                                                             |       |




### Font Size
Sets the font size.

| Tailwind  | Description                                | Other |
| --------- | ------------------------------------------ | ----- |
| text-xs   | font-size: 0.75rem; line-height: 1rem;     | 12px  |
| text-sm   | font-size: 0.875rem; line-height: 1.25rem; | 14px  |
| text-base | font-size: 1rem; line-height: 1.5rem;      | 16px  |
| text-lg   | font-size: 1.125rem; line-height: 1.75rem; | 18px  |
| text-xl   | font-size: 1.25rem; line-height: 1.75rem;  | 20px  |
| text-2xl  | font-size: 1.5rem; line-height: 2rem;      | 24px  |
| text-3xl  | font-size: 1.875rem; line-height: 2.25rem; | 30px  |
| text-4xl  | font-size: 2.25rem; line-height: 2.5rem;   | 36px  |
| text-5xl  | font-size: 3rem; line-height: 1;           | 48px  |
| text-6xl  | font-size: 3.75rem; line-height: 1;        | 64px  |
| text-7xl  | font-size: 4.5rem; line-height: 1;         | 72px  |
| text-8xl  | font-size: 6rem; line-height: 1;           | 80px  |
| text-9xl  | font-size: 8rem; line-height: 1;           | 96px  |




### Font Smoothing

| Tailwind             | Description                                                              | Other |
| -------------------- | ------------------------------------------------------------------------ | ----- |
| antialiased          | -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; |       |
| subpixel-antialiased | -webkit-font-smoothing: auto; -moz-osx-font-smoothing: auto;             |       |




### Font Style

| Tailwind   | Description         | Other |
| ---------- | ------------------- | ----- |
| italic     | font-style: italic; |       |
| not-italic | font-style: normal; |       |




### Font Weight
Sets the font weight.

| Tailwind        | Description       | Other |
| --------------- | ----------------- | ----- |
| font-thin       | font-weight: 100; |       |
| font-extralight | font-weight: 200; |       |
| font-light      | font-weight: 300; |       |
| font-normal     | font-weight: 400; |       |
| font-medium     | font-weight: 500; |       |
| font-semibold   | font-weight: 600; |       |
| font-bold       | font-weight: 700; |       |
| font-extrabold  | font-weight: 800; |       |
| font-black      | font-weight: 900; |       |




### Font Variant Numeric
Utilities for controlling the variant of numbers.

| Tailwind           | Description                               | Other |
| ------------------ | ----------------------------------------- | ----- |
| normal-nums        | font-variant-numeric: normal;             |       |
| ordinal            | font-variant-numeric: ordinal;            |       |
| slashed-zero       | font-variant-numeric: slashed-zero;       |       |
| lining-nums        | font-variant-numeric: lining-nums;        |       |
| oldstyle-nums      | font-variant-numeric: oldstyle-nums;      |       |
| proportional-nums  | font-variant-numeric: proportional-nums;  |       |
| tabular-nums       | font-variant-numeric: tabular-nums;       |       |
| diagonal-fractions | font-variant-numeric: diagonal-fractions; |       |
| stacked-fractions  | font-variant-numeric: stacked-fractions;  |       |




### Letter Spacing
Sets the spacing between letters.

| Tailwind         | Description               | Other |
| ---------------- | ------------------------- | ----- |
| tracking-tighter | letter-spacing: -0.05em;  |       |
| tracking-tight   | letter-spacing: -0.025em; |       |
| tracking-normal  | letter-spacing: 0;        |       |
| tracking-wide    | letter-spacing: 0.025em;  |       |
| tracking-wider   | letter-spacing: 0.05em;   |       |
| tracking-widest  | letter-spacing: 0.1em;    |       |




### Line Height
Sets the line height.

| Tailwind        | Description           | Other |
| --------------- | --------------------- | ----- |
| leading-none    | line-height: 1;       |       |
| leading-tight   | line-height: 1.25;    |       |
| leading-snug    | line-height: 1.375;   |       |
| leading-normal  | line-height: 1.5;     |       |
| leading-relaxed | line-height: 1.625;   |       |
| leading-loose   | line-height: 2;       |       |
| leading-3       | line-height: .75rem;  | 12px  |
| leading-4       | line-height: 1rem;    | 16px  |
| leading-5       | line-height: 1.25rem; | 20px  |
| leading-6       | line-height: 1.5rem;  | 24px  |
| leading-7       | line-height: 1.75rem; | 28px  |
| leading-8       | line-height: 2rem;    | 32px  |
| leading-9       | line-height: 2.25rem; | 36px  |
| leading-10      | line-height: 2.5rem;  | 40px  |





### List Style Type
Sets the bullet style of a list.

| Tailwind     | Description               | Other |
| ------------ | ------------------------- | ----- |
| list-none    | list-style-type: none;    |       |
| list-disc    | list-style-type: disc;    |       |
| list-decimal | list-style-type: decimal; |       |




### List Style Position
Sets the position of a list's bullets.

| Tailwind     | Description                   | Other |
| ------------ | ----------------------------- | ----- |
| list-inside  | list-style-position: inside;  |       |
| list-outside | list-style-position: outside; |       |


### Text Align
Sets the alignment of text.

| Tailwind     | Description          | Other |
| ------------ | -------------------- | ----- |
| text-left    | text-align: left;    |       |
| text-center  | text-align: center;  |       |
| text-right   | text-align: right;   |       |
| text-justify | text-align: justify; |       |



### Text Color
Sets the text color.

| Tailwind         | Description           | Other |
| ---------------- | --------------------- | ----- |
| text-transparent | color: transparent; |       |
| text-current     | color: currentColor; |       |
| text-black       | color: `#000000;`     |       |
| text-white       | color: `#ffffff;`     |       |
| text-gray-50     | color: `#F9FAFB;`     |       |
| text-gray-100    | color: `#F3F4F6;`     |       |
| text-gray-200    | color: `#E5E7EB;`     |       |
| text-gray-300    | color: `#D1D5DB;`     |       |
| text-gray-400    | color: `#9CA3AF;`     |       |
| text-gray-500    | color: `#6B7280;`     |       |
| text-gray-600    | color: `#4B5563;`     |       |
| text-gray-700    | color: `#374151;`     |       |
| text-gray-800    | color: `#1F2937;`     |       |
| text-gray-900    | color: `#111827;`     |       |
| text-red-50      | color: `#FEF2F2;`     |       |
| text-red-100     | color: `#FEE2E2;`     |       |
| text-red-200     | color: `#FECACA;`     |       |
| text-red-300     | color: `#FCA5A5;`     |       |
| text-red-400     | color: `#F87171;`     |       |
| text-red-500     | color: `#EF4444;`     |       |
| text-red-600     | color: `#DC2626;`     |       |
| text-red-700     | color: `#B91C1C;`     |       |
| text-red-800     | color: `#991B1B;`     |       |
| text-red-900     | color: `#7F1D1D;`     |       |
| text-yellow-50   | color: `#FFFBEB;`     |       |
| text-yellow-100  | color: `#FEF3C7;`     |       |
| text-yellow-200  | color: `#FDE68A;`     |       |
| text-yellow-300  | color: `#FCD34D;`     |       |
| text-yellow-400  | color: `#FBBF24;`     |       |
| text-yellow-500  | color: `#F59E0B;`     |       |
| text-yellow-600  | color: `#D97706;`     |       |
| text-yellow-700  | color: `#B45309;`     |       |
| text-yellow-800  | color: `#92400E;`     |       |
| text-yellow-900  | color: `#78350F;`     |       |
| text-green-50    | color: `#ECFDF5;`     |       |
| text-green-100   | color: `#D1FAE5;`     |       |
| text-green-200   | color: `#A7F3D0;`     |       |
| text-green-300   | color: `#6EE7B7;`     |       |
| text-green-400   | color: `#34D399;`     |       |
| text-green-500   | color: `#10B981;`     |       |
| text-green-600   | color: `#059669;`     |       |
| text-green-700   | color: `#047857;`     |       |
| text-green-800   | color: `#065F46;`     |       |
| text-green-900   | color: `#064E3B;`     |       |
| text-blue-50     | color: `#EFF6FF;`     |       |
| text-blue-100    | color: `#DBEAFE;`     |       |
| text-blue-200    | color: `#BFDBFE;`     |       |
| text-blue-300    | color: `#93C5FD;`     |       |
| text-blue-400    | color: `#60A5FA;`     |       |
| text-blue-500    | color: `#3B82F6;`     |       |
| text-blue-600    | color: `#2563EB;`     |       |
| text-blue-700    | color: `#1D4ED8;`     |       |
| text-blue-800    | color: `#1E40AF;`     |       |
| text-blue-900    | color: `#1E3A8A;`     |       |
| text-indigo-50   | color: `#EEF2FF;`     |       |
| text-indigo-100  | color: `#E0E7FF;`     |       |
| text-indigo-200  | color: `#C7D2FE;`     |       |
| text-indigo-300  | color: `#A5B4FC;`     |       |
| text-indigo-400  | color: `#818CF8;`     |       |
| text-indigo-500  | color: `#6366F1;`     |       |
| text-indigo-600  | color: `#4F46E5;`     |       |
| text-indigo-700  | color: `#4338CA;`     |       |
| text-indigo-800  | color: `#3730A3;`     |       |
| text-indigo-900  | color: `#312E81;`     |       |
| text-purple-50   | color: `#F5F3FF;`     |       |
| text-purple-100  | color: `#EDE9FE;`     |       |
| text-purple-200  | color: `#DDD6FE;`     |       |
| text-purple-300  | color: `#C4B5FD;`     |       |
| text-purple-400  | color: `#A78BFA;`     |       |
| text-purple-500  | color: `#8B5CF6;`     |       |
| text-purple-600  | color: `#7C3AED;`     |       |
| text-purple-700  | color: `#6D28D9;`     |       |
| text-purple-800  | color: `#5B21B6;`     |       |
| text-purple-900  | color: `#4C1D95;`     |       |
| text-pink-50     | color: `#FDF2F8;`     |       |
| text-pink-100    | color: `#FCE7F3;`     |       |
| text-pink-200    | color: `#FBCFE8;`     |       |
| text-pink-300    | color: `#F9A8D4;`     |       |
| text-pink-400    | color: `#F472B6;`     |       |
| text-pink-500    | color: `#EC4899;`     |       |
| text-pink-600    | color: `#DB2777;`     |       |
| text-pink-700    | color: `#BE185D;`     |       |
| text-pink-800    | color: `#9D174D;`     |       |
| text-pink-900    | color: `#831843;`     |       |



### Text Decoration
Utilities for controlling the decoration of text.

| Tailwind     | Description                    | Other |
| ------------ | ------------------------------ | ----- |
| underline    | text-decoration: underline;    |       |
| overline     | text-decoration: overline;     |       |
| line-through | text-decoration: line-through; |       |
| no-underline | text-decoration: none;         |       |




### Text Decoration Style
Utilities for controlling the style of text decorations.

| Tailwind          | Description                    | Other |
| ----------------- | ------------------------------ | ----- |
| decoration-solid  | text-decoration-style: solid;  |       |
| decoration-double | text-decoration-style: double; |       |
| decoration-dotted | text-decoration-style: dotted; |       |
| decoration-dashed | text-decoration-style: dashed; |       |
| decoration-wavy   | text-decoration-style: wavy;   |       |





### Text Decoration Thickness
Utilities for controlling the thickness of text decorations.

| Tailwind             | Description                           | Other |
| -------------------- | ------------------------------------- | ----- |
| decoration-auto      | text-decoration-thickness: auto;      |       |
| decoration-from-font | text-decoration-thickness: from-font; |       |
| decoration-0         | text-decoration-thickness: 0px;       |       |
| decoration-1         | text-decoration-thickness: 1px;       |       |
| decoration-2         | text-decoration-thickness: 2px;       |       |
| decoration-4         | text-decoration-thickness: 4px;       |       |
| decoration-8         | text-decoration-thickness: 8px;       |       |





### Text Underline Offset
Utilities for controlling the offset of a text underline.

| Tailwind                   | Description                       | Other |
| -------------------------- | --------------------------------- | ----- |
| underline-offset-auto      | text-underline-offset: auto;      |       |
| underline-offset-from-font | text-underline-offset: from-font; |       |
| underline-offset-0         | text-underline-offset: 0px;       |       |
| underline-offset-1         | text-underline-offset: 1px;       |       |
| underline-offset-2         | text-underline-offset: 2px;       |       |
| underline-offset-4         | text-underline-offset: 4px;       |       |
| underline-offset-8         | text-underline-offset: 8px;       |       |



### Text Transform
Utilities for controlling the transformation of text.

| Tailwind    | Description                 | Other |
| ----------- | --------------------------- | ----- |
| uppercase   | text-transform: uppercase;  |       |
| lowercase   | text-transform: lowercase;  |       |
| capitalize  | text-transform: capitalize; |       |
| normal-case | text-transform: none;       |       |




### Text Overflow
Utilities for controlling text overflow in an element.

| Tailwind             | Description                         | Other |
| -------------------- | ----------------------------------- | ----- |
|truncate|	overflow: hidden; text-overflow: ellipsis; white-space: nowrap;	||
|text-ellipsis	|text-overflow: ellipsis;	||
|text-clip	|text-overflow: clip;||



### Text Indent
Utilities for controlling the amount of empty space shown before text in a block.

| Tailwind   | Description            | Other |
| ---------- | ---------------------- | ----- |
| indent-0   | text-indent: 0;        |       |
| indent-0.5 | text-indent: 0.125rem; | 2px   |
| indent-1   | text-indent: 0.25rem;  | 4px   |
| indent-1.5 | text-indent: 0.375rem; | 6px   |
| indent-2   | text-indent: 0.5rem;   | 8px   |
| indent-2.5 | text-indent: 0.625rem; | 10px  |
| indent-3   | text-indent: 0.75rem;  | 12px  |
| indent-3.5 | text-indent: 0.875rem; | 14px  |
| indent-4   | text-indent: 1rem;     | 16px  |
| indent-5   | text-indent: 1.25rem;  | 20px  |
| indent-6   | text-indent: 1.5rem;   | 24px  |
| indent-8   | text-indent: 2rem;     | 32px  |
| indent-10  | text-indent: 2.5rem;   | 40px  |
| indent-11  | text-indent: 2.75rem;  | 44px  |
| indent-12  | text-indent: 3rem;     | 48px  |
| indent-14  | text-indent: 3.5rem;   | 56px  |
| indent-16  | text-indent: 4rem;     | 64px  |
| indent-20  | text-indent: 5rem;     | 80px  |
| indent-24  | text-indent: 6rem;     | 96px  |
| indent-28  | text-indent: 7rem;     | 112px |
| indent-32  | text-indent: 8rem;     | 128px |
| indent-36  | text-indent: 9rem;     | 144px |
| indent-40  | text-indent: 10rem;    | 160px |
| indent-44  | text-indent: 11rem;    | 176px |
| indent-48  | text-indent: 12rem;    | 192px |
| indent-52  | text-indent: 13rem;    | 208px |
| indent-56  | text-indent: 14rem;    | 224px |
| indent-64  | text-indent: 16rem;    | 256px |
| indent-72  | text-indent: 18rem;    | 288px |
| indent-80  | text-indent: 20rem;    | 320px |
| indent-96  | text-indent: 24rem;    | 384px |
| indent-px  | text-indent: 1px;      |       |




### Vertical Align
Sets the vertical alignment of an inline or table-cell box.

| Tailwind          | Description                  | Other |
| ----------------- | ---------------------------- | ----- |
| align-baseline    | vertical-align: baseline;    |       |
| align-top         | vertical-align: top;         |       |
| align-middle      | vertical-align: middle;      |       |
| align-bottom      | vertical-align: bottom;      |       |
| align-text-top    | vertical-align: text-top;    |       |
| align-text-bottom | vertical-align: text-bottom; |       |
| align-sub         | vertical-align: sub;         |       |
| align-super       | vertical-align: super;       |       |




### White Space
Sets the whitespace of an element.

| Tailwind            | Description            | Other |
| ------------------- | ---------------------- | ----- |
| whitespace-normal   | white-space: normal;   |       |
| whitespace-nowrap   | white-space: nowrap;   |       |
| whitespace-pre      | white-space: pre;      |       |
| whitespace-pre-line | white-space: pre-line; |       |
| whitespace-pre-wrap | white-space: pre-wrap; |       |





### Word Break
Sets the word breaks of an element.

| Tailwind     | Description                                | Other |
| ------------ | ------------------------------------------ | ----- |
| break-normal | overflow-wrap: normal; word-break: normal; |       |
| break-words  | overflow-wrap: break-word;                 |       |
| break-all    | word-break: break-all;                     |       |



### Content
Utilities for controlling the content of the before and after pseudo-elements.

| Tailwind     | Description    | Other |
| ------------ | -------------- | ----- |
| content-none | content: none; |       |


----


## Interactivity 


### Appearance 
Disables native styling based on the operating system's theme.

| Tailwind        | Description       | Other |
| --------------- | ----------------- | ----- |
| appearance-none | appearance: none; |       |




### Cursor
Changes the cursor when hovering over an element.

| Tailwind             | Description            | Other |
| -------------------- | ---------------------- | ----- |
| cursor-auto          | cursor: auto;          |       |
| cursor-default       | cursor: default;       |       |
| cursor-pointer       | cursor: pointer;       |       |
| cursor-wait          | cursor: wait;          |       |
| cursor-text          | cursor: text;          |       |
| cursor-move          | cursor: move;          |       |
| cursor-help          | cursor: help;          |       |
| cursor-not-allowed   | cursor: not-allowed;   |       |
| cursor-none          | cursor: none;          |       |
| cursor-context-menu  | cursor: context-menu;  |       |
| cursor-progress      | cursor: progress;      |       |
| cursor-cell          | cursor: cell;          |       |
| cursor-crosshair     | cursor: crosshair;     |       |
| cursor-vertical-text | cursor: vertical-text; |       |
| cursor-alias         | cursor: alias;         |       |
| cursor-copy          | cursor: copy;          |       |
| cursor-no-drop       | cursor: no-drop;       |       |
| cursor-grab          | cursor: grab;          |       |
| cursor-grabbing      | cursor: grabbing;      |       |
| cursor-all-scroll    | cursor: all-scroll;    |       |
| cursor-col-resize    | cursor: col-resize;    |       |
| cursor-row-resize    | cursor: row-resize;    |       |
| cursor-n-resize      | cursor: n-resize;      |       |
| cursor-e-resize      | cursor: e-resize;      |       |
| cursor-s-resize      | cursor: s-resize;      |       |
| cursor-w-resize      | cursor: w-resize;      |       |
| cursor-ne-resize     | cursor: ne-resize;     |       |
| cursor-nw-resize     | cursor: nw-resize;     |       |
| cursor-se-resize     | cursor: se-resize;     |       |
| cursor-sw-resize     | cursor: sw-resize;     |       |
| cursor-ew-resize     | cursor: ew-resize;     |       |
| cursor-ns-resize     | cursor: ns-resize;     |       |
| cursor-nesw-resize   | cursor: nesw-resize;   |       |
| cursor-nwse-resize   | cursor: nwse-resize;   |       |
| cursor-zoom-in       | cursor: zoom-in;       |       |
| cursor-zoom-out      | cursor: zoom-out;      |       |





### Pointer Events
Specifies whether an element is the target of mouse events.

| Tailwind            | Description           | Other |
| ------------------- | --------------------- | ----- |
| pointer-events-none | pointer-events: none; |       |
| pointer-events-auto | pointer-events: auto; |       |




### Resize
Sets whether an element is resizable, along with direction.

| Tailwind    | Description         | Other |
| ----------- | ------------------- | ----- |
|             |                     |       |
| resize-none | resize: none;       |       |
| resize      | resize: both;       |       |
| resize-y    | resize: vertical;   |       |
| resize-x    | resize: horizontal; |       |




### Scroll Behavior
Utilities for controlling the scroll behavior of an element.

| Tailwind      | Description              | Other |
| ------------- | ------------------------ | ----- |
| scroll-auto   | scroll-behavior: auto;   |       |
| scroll-smooth | scroll-behavior: smooth; |       |




### Scroll Margin
Utilities for controlling the scroll offset around items in a snap container.

| Tailwind      | Description                                                  | Other |
| ------------- | ------------------------------------------------------------ | ----- |
| scroll-m-0    | scroll-margin: 0;                                            |       |
| scroll-m-0.5  | scroll-margin: 0.125rem;                                     | 2px   |
| scroll-m-1    | scroll-margin: 0.25rem;                                      | 4px   |
| scroll-m-1.5  | scroll-margin: 0.375rem;                                     | 6px   |
| scroll-m-2    | scroll-margin: 0.5rem;                                       | 8px   |
| scroll-m-2.5  | scroll-margin: 0.625rem;                                     | 10px  |
| scroll-m-3    | scroll-margin: 0.75rem;                                      | 12px  |
| scroll-m-3.5  | scroll-margin: 0.875rem;                                     | 14px  |
| scroll-m-4    | scroll-margin: 1rem;                                         | 16px  |
| scroll-m-5    | scroll-margin: 1.25rem;                                      | 20px  |
| scroll-m-6    | scroll-margin: 1.5rem;                                       | 24px  |
| scroll-m-8    | scroll-margin: 2rem;                                         | 32px  |
| scroll-m-10   | scroll-margin: 2.5rem;                                       | 40px  |
| scroll-m-11   | scroll-margin: 2.75rem;                                      | 44px  |
| scroll-m-12   | scroll-margin: 3rem;                                         | 48px  |
| scroll-m-14   | scroll-margin: 3.5rem;                                       | 56px  |
| scroll-m-16   | scroll-margin: 4rem;                                         | 64px  |
| scroll-m-20   | scroll-margin: 5rem;                                         | 80px  |
| scroll-m-24   | scroll-margin: 6rem;                                         | 96px  |
| scroll-m-28   | scroll-margin: 7rem;                                         | 112px |
| scroll-m-32   | scroll-margin: 8rem;                                         | 128px |
| scroll-m-36   | scroll-margin: 9rem;                                         | 144px |
| scroll-m-40   | scroll-margin: 10rem;                                        | 160px |
| scroll-m-44   | scroll-margin: 11rem;                                        | 176px |
| scroll-m-48   | scroll-margin: 12rem;                                        | 192px |
| scroll-m-52   | scroll-margin: 13rem;                                        | 208px |
| scroll-m-56   | scroll-margin: 14rem;                                        | 224px |
| scroll-m-64   | scroll-margin: 16rem;                                        | 256px |
| scroll-m-72   | scroll-margin: 18rem;                                        | 288px |
| scroll-m-80   | scroll-margin: 20rem;                                        | 320px |
| scroll-m-96   | scroll-margin: 24rem;                                        | 384px |
| scroll-m-px   | scroll-margin: 1px;                                          |       |
| scroll-my-0   | scroll-margin-top: 0; scroll-margin-bottom: 0;               |       |
| scroll-mx-0   | scroll-margin-left: 0; scroll-margin-right: 0;               |       |
| scroll-my-0.5 | scroll-margin-top: 0.125rem; scroll-margin-bottom: 0.125rem; | 2px   |
| scroll-mx-0.5 | scroll-margin-left: 0.125rem; scroll-margin-right: 0.125rem; | 2px   |
| scroll-my-1   | scroll-margin-top: 0.25rem; scroll-margin-bottom: 0.25rem;   | 4px   |
| scroll-mx-1   | scroll-margin-left: 0.25rem; scroll-margin-right: 0.25rem;   | 4px   |
| scroll-my-1.5 | scroll-margin-top: 0.375rem; scroll-margin-bottom: 0.375rem; | 6px   |
| scroll-mx-1.5 | scroll-margin-left: 0.375rem; scroll-margin-right: 0.375rem; | 6px   |
| scroll-my-2   | scroll-margin-top: 0.5rem; scroll-margin-bottom: 0.5rem;     | 8px   |
| scroll-mx-2   | scroll-margin-left: 0.5rem; scroll-margin-right: 0.5rem;     | 8px   |
| scroll-my-2.5 | scroll-margin-top: 0.625rem; scroll-margin-bottom: 0.625rem; | 10px  |
| scroll-mx-2.5 | scroll-margin-left: 0.625rem; scroll-margin-right: 0.625rem; | 10px  |
| scroll-my-3   | scroll-margin-top: 0.75rem; scroll-margin-bottom: 0.75rem;   | 12px  |
| scroll-mx-3   | scroll-margin-left: 0.75rem; scroll-margin-right: 0.75rem;   | 12px  |
| scroll-my-3.5 | scroll-margin-top: 0.875rem; scroll-margin-bottom: 0.875rem; | 14px  |
| scroll-mx-3.5 | scroll-margin-left: 0.875rem; scroll-margin-right: 0.875rem; | 14px  |
| scroll-my-4   | scroll-margin-top: 1rem; scroll-margin-bottom: 1rem;         | 16px  |
| scroll-mx-4   | scroll-margin-left: 1rem; scroll-margin-right: 1rem;         | 16px  |
| scroll-my-5   | scroll-margin-top: 1.25rem; scroll-margin-bottom: 1.25rem;   | 20px  |
| scroll-mx-5   | scroll-margin-left: 1.25rem; scroll-margin-right: 1.25rem;   | 20px  |
| scroll-my-6   | scroll-margin-top: 1.5rem; scroll-margin-bottom: 1.5rem;     | 24px  |
| scroll-mx-6   | scroll-margin-left: 1.5rem; scroll-margin-right: 1.5rem;     | 24px  |
| scroll-my-7   | scroll-margin-top: 1.75rem; scroll-margin-bottom: 1.75rem;   | 24px  |
| scroll-mx-7   | scroll-margin-left: 1.75rem; scroll-margin-right: 1.75rem;   | 24px  |
| scroll-my-8   | scroll-margin-top: 2rem; scroll-margin-bottom: 2rem;         | 32px  |
| scroll-mx-8   | scroll-margin-left: 2rem; scroll-margin-right: 2rem;         | 32px  |
| scroll-my-9   | scroll-margin-top: 2.25rem; scroll-margin-bottom: 2.25rem;   | 36px  |
| scroll-mx-9   | scroll-margin-left: 2.25rem; scroll-margin-right: 2.25rem;   | 36px  |
| scroll-my-10  | scroll-margin-top: 2.5rem; scroll-margin-bottom: 2.5rem;     | 40px  |
| scroll-mx-10  | scroll-margin-left: 2.5rem; scroll-margin-right: 2.5rem;     | 40px  |
| scroll-my-11  | scroll-margin-top: 2.75rem; scroll-margin-bottom: 2.75rem;   | 44px  |
| scroll-mx-11  | scroll-margin-left: 2.75rem; scroll-margin-right: 2.75rem;   | 44px  |
| scroll-my-12  | scroll-margin-top: 3rem; scroll-margin-bottom: 3rem;         | 48px  |
| scroll-mx-12  | scroll-margin-left: 3rem; scroll-margin-right: 3rem;         | 48px  |
| scroll-my-14  | scroll-margin-top: 3.5rem; scroll-margin-bottom: 3.5rem;     | 56px  |
| scroll-mx-14  | scroll-margin-left: 3.5rem; scroll-margin-right: 3.5rem;     | 56px  |
| scroll-my-16  | scroll-margin-top: 4rem; scroll-margin-bottom: 4rem;         | 64px  |
| scroll-mx-16  | scroll-margin-left: 4rem; scroll-margin-right: 4rem;         | 64px  |
| scroll-my-20  | scroll-margin-top: 5rem; scroll-margin-bottom: 5rem;         | 80px  |
| scroll-mx-20  | scroll-margin-left: 5rem; scroll-margin-right: 5rem;         | 80px  |
| scroll-my-24  | scroll-margin-top: 6rem; scroll-margin-bottom: 6rem;         | 96px  |
| scroll-mx-24  | scroll-margin-left: 6rem; scroll-margin-right: 6rem;         | 96px  |
| scroll-my-28  | scroll-margin-top: 7rem; scroll-margin-bottom: 7rem;         | 112px |
| scroll-mx-28  | scroll-margin-left: 7rem; scroll-margin-right: 7rem;         | 112px |
| scroll-my-32  | scroll-margin-top: 8rem; scroll-margin-bottom: 8rem;         | 128px |
| scroll-mx-32  | scroll-margin-left: 8rem; scroll-margin-right: 8rem;         | 128px |
| scroll-my-36  | scroll-margin-top: 9rem; scroll-margin-bottom: 9rem;         | 144px |
| scroll-mx-36  | scroll-margin-left: 9rem; scroll-margin-right: 9rem;         | 144px |
| scroll-my-40  | scroll-margin-top: 10rem; scroll-margin-bottom: 10rem;       | 160px |
| scroll-mx-40  | scroll-margin-left: 10rem; scroll-margin-right: 10rem;       | 160px |
| scroll-my-44  | scroll-margin-top: 11rem; scroll-margin-bottom: 11rem;       | 176px |
| scroll-mx-44  | scroll-margin-left: 11rem; scroll-margin-right: 11rem;       | 176px |
| scroll-my-48  | scroll-margin-top: 12rem; scroll-margin-bottom: 12rem;       | 192px |
| scroll-mx-48  | scroll-margin-left: 12rem; scroll-margin-right: 12rem;       | 192px |
| scroll-my-52  | scroll-margin-top: 13rem; scroll-margin-bottom: 13rem;       | 208px |
| scroll-mx-52  | scroll-margin-left: 13rem; scroll-margin-right: 13rem;       | 208px |
| scroll-my-56  | scroll-margin-top: 14rem; scroll-margin-bottom: 14rem;       | 224px |
| scroll-mx-56  | scroll-margin-left: 14rem; scroll-margin-right: 14rem;       | 224px |
| scroll-my-60  | scroll-margin-top: 15rem; scroll-margin-bottom: 15rem;       | 240px |
| scroll-mx-60  | scroll-margin-left: 15rem; scroll-margin-right: 15rem;       | 240px |
| scroll-my-64  | scroll-margin-top: 16rem; scroll-margin-bottom: 16rem;       | 256px |
| scroll-mx-64  | scroll-margin-left: 16rem; scroll-margin-right: 16rem;       | 256px |
| scroll-my-70  | scroll-margin-top: 18rem; scroll-margin-bottom: 18rem;       | 280px |
| scroll-mx-70  | scroll-margin-left: 18rem; scroll-margin-right: 18rem;       | 280px |
| scroll-my-80  | scroll-margin-top: 20rem; scroll-margin-bottom: 20rem;       | 320px |
| scroll-mx-80  | scroll-margin-left: 20rem; scroll-margin-right: 20rem;       | 320px |
| scroll-my-96  | scroll-margin-top: 24rem; scroll-margin-bottom: 24rem;       | 384px |
| scroll-mx-96  | scroll-margin-left: 24rem; scroll-margin-right: 24rem;       | 384px |
| scroll-my-px  | scroll-margin-top: 1px; scroll-margin-bottom: 1px;           |       |
| scroll-mx-px  | scroll-margin-left: 1px; scroll-margin-right: 1px;           |       |
| scroll-mt-0   | scroll-margin-top: 0;                                        |       |
| scroll-mr-0   | scroll-margin-right: 0;                                      |       |
| scroll-mb-0   | scroll-margin-bottom: 0;                                     |       |
| scroll-ml-0   | scroll-margin-left: 0;                                       |       |
| scroll-mt-0.5 | scroll-margin-top: 0.125rem;                                 | 2px   |
| scroll-mr-0.5 | scroll-margin-right: 0.125rem;                               | 2px   |
| scroll-mb-0.5 | scroll-margin-bottom: 0.125rem;                              | 2px   |
| scroll-ml-0.5 | scroll-margin-left: 0.125rem;                                | 2px   |
| scroll-mt-1   | scroll-margin-top: 0.25rem;                                  | 4px   |
| scroll-mr-1   | scroll-margin-right: 0.25rem;                                | 4px   |
| scroll-mb-1   | scroll-margin-bottom: 0.25rem;                               | 4px   |
| scroll-ml-1   | scroll-margin-left: 0.25rem;                                 | 4px   |
| scroll-mt-1.5 | scroll-margin-top: 0.375rem;                                 | 6px   |
| scroll-mr-1.5 | scroll-margin-right: 0.375rem;                               | 6px   |
| scroll-mb-1.5 | scroll-margin-bottom: 0.375rem;                              | 6px   |
| scroll-ml-1.5 | scroll-margin-left: 0.375rem;                                | 6px   |
| scroll-mt-2   | scroll-margin-top: 0.5rem;                                   | 8px   |
| scroll-mr-2   | scroll-margin-right: 0.5rem;                                 | 8px   |
| scroll-mb-2   | scroll-margin-bottom: 0.5rem;                                | 8px   |
| scroll-ml-2   | scroll-margin-left: 0.5rem;                                  | 8px   |
| scroll-mt-2.5 | scroll-margin-top: 0.625rem;                                 | 10px  |
| scroll-mr-2.5 | scroll-margin-right: 0.625rem;                               | 10px  |
| scroll-mb-2.5 | scroll-margin-bottom: 0.625rem;                              | 10px  |
| scroll-ml-2.5 | scroll-margin-left: 0.625rem;                                | 10px  |
| scroll-mt-3   | scroll-margin-top: 0.75rem;                                  | 12px  |
| scroll-mr-3   | scroll-margin-right: 0.75rem;                                | 12px  |
| scroll-mb-3   | scroll-margin-bottom: 0.75rem;                               | 12px  |
| scroll-ml-3   | scroll-margin-left: 0.75rem;                                 | 12px  |
| scroll-mt-3.5 | scroll-margin-top: 0.875rem;                                 | 14px  |
| scroll-mr-3.5 | scroll-margin-right: 0.875rem;                               | 14px  |
| scroll-mb-3.5 | scroll-margin-bottom: 0.875rem;                              | 14px  |
| scroll-ml-3.5 | scroll-margin-left: 0.875rem;                                | 14px  |
| scroll-mt-4   | scroll-margin-top: 1rem;                                     | 16px  |
| scroll-mr-4   | scroll-margin-right: 1rem;                                   | 16px  |
| scroll-mb-4   | scroll-margin-bottom: 1rem;                                  | 16px  |
| scroll-ml-4   | scroll-margin-left: 1rem;                                    | 16px  |
| scroll-mt-5   | scroll-margin-top: 1.25rem;                                  | 20px  |
| scroll-mr-5   | scroll-margin-right: 1.25rem;                                | 20px  |
| scroll-mb-5   | scroll-margin-bottom: 1.25rem;                               | 20px  |
| scroll-ml-5   | scroll-margin-left: 1.25rem;                                 | 20px  |
| scroll-mt-6   | scroll-margin-top: 1.5rem;                                   | 24px  |
| scroll-mr-6   | scroll-margin-right: 1.5rem;                                 | 24px  |
| scroll-mb-6   | scroll-margin-bottom: 1.5rem;                                | 24px  |
| scroll-ml-6   | scroll-margin-left: 1.5rem;                                  | 24px  |
| scroll-mt-7   | scroll-margin-top: 1.75rem;                                  | 28px  |
| scroll-mr-7   | scroll-margin-right: 1.75rem;                                | 28px  |
| scroll-mb-7   | scroll-margin-bottom: 1.75rem;                               | 28px  |
| scroll-ml-7   | scroll-margin-left: 1.75rem;                                 | 28px  |
| scroll-mt-8   | scroll-margin-top: 2rem;                                     | 32px  |
| scroll-mr-8   | scroll-margin-right: 2rem;                                   | 32px  |
| scroll-mb-8   | scroll-margin-bottom: 2rem;                                  | 32px  |
| scroll-ml-8   | scroll-margin-left: 2rem;                                    | 32px  |
| scroll-mt-9   | scroll-margin-top: 2.25rem;                                  | 36px  |
| scroll-mr-9   | scroll-margin-right: 2.25rem;                                | 36px  |
| scroll-mb-9   | scroll-margin-bottom: 2.25rem;                               | 36px  |
| scroll-ml-9   | scroll-margin-left: 2.25rem;                                 | 36px  |
| scroll-mt-10  | scroll-margin-top: 2.5rem;                                   | 40px  |
| scroll-mr-10  | scroll-margin-right: 2.5rem;                                 | 40px  |
| scroll-mb-10  | scroll-margin-bottom: 2.5rem;                                | 40px  |
| scroll-ml-10  | scroll-margin-left: 2.5rem;                                  | 40px  |
| scroll-mt-11  | scroll-margin-top: 2.75rem;                                  | 44px  |
| scroll-mr-11  | scroll-margin-right: 2.75rem;                                | 44px  |
| scroll-mb-11  | scroll-margin-bottom: 2.75rem;                               | 44px  |
| scroll-ml-11  | scroll-margin-left: 2.75rem;                                 | 44px  |
| scroll-mt-12  | scroll-margin-top: 3rem;                                     | 48px  |
| scroll-mr-12  | scroll-margin-right: 3rem;                                   | 48px  |
| scroll-mb-12  | scroll-margin-bottom: 3rem;                                  | 48px  |
| scroll-ml-12  | scroll-margin-left: 3rem;                                    | 48px  |
| scroll-mt-14  | scroll-margin-top: 3.5rem;                                   | 56px  |
| scroll-mr-14  | scroll-margin-right: 3.5rem;                                 | 56px  |
| scroll-mb-14  | scroll-margin-bottom: 3.5rem;                                | 56px  |
| scroll-ml-14  | scroll-margin-left: 3.5rem;                                  | 56px  |
| scroll-mt-16  | scroll-margin-top: 4rem;                                     | 64px  |
| scroll-mr-16  | scroll-margin-right: 4rem;                                   | 64px  |
| scroll-mb-16  | scroll-margin-bottom: 4rem;                                  | 64px  |
| scroll-ml-16  | scroll-margin-left: 4rem;                                    | 64px  |
| scroll-mt-20  | scroll-margin-top: 5rem;                                     | 80px  |
| scroll-mr-20  | scroll-margin-right: 5rem;                                   | 80px  |
| scroll-mb-20  | scroll-margin-bottom: 5rem;                                  | 80px  |
| scroll-ml-20  | scroll-margin-left: 5rem;                                    | 80px  |
| scroll-mt-24  | scroll-margin-top: 6rem;                                     | 96px  |
| scroll-mr-24  | scroll-margin-right: 6rem;                                   | 96px  |
| scroll-mb-24  | scroll-margin-bottom: 6rem;                                  | 96px  |
| scroll-ml-24  | scroll-margin-left: 6rem;                                    | 96px  |
| scroll-mt-28  | scroll-margin-top: 7rem;                                     | 112px |
| scroll-mr-28  | scroll-margin-right: 7rem;                                   | 112px |
| scroll-mb-28  | scroll-margin-bottom: 7rem;                                  | 112px |
| scroll-ml-28  | scroll-margin-left: 7rem;                                    | 112px |
| scroll-mt-32  | scroll-margin-top: 8rem;                                     | 128px |
| scroll-mr-32  | scroll-margin-right: 8rem;                                   | 128px |
| scroll-mb-32  | scroll-margin-bottom: 8rem;                                  | 128px |
| scroll-ml-32  | scroll-margin-left: 8rem;                                    | 128px |
| scroll-mt-36  | scroll-margin-top: 9rem;                                     | 144px |
| scroll-mr-36  | scroll-margin-right: 9rem;                                   | 144px |
| scroll-mb-36  | scroll-margin-bottom: 9rem;                                  | 144px |
| scroll-ml-36  | scroll-margin-left: 9rem;                                    | 144px |
| scroll-mt-40  | scroll-margin-top: 10rem;                                    | 160px |
| scroll-mr-40  | scroll-margin-right: 10rem;                                  | 160px |
| scroll-mb-40  | scroll-margin-bottom: 10rem;                                 | 160px |
| scroll-ml-40  | scroll-margin-left: 10rem;                                   | 160px |
| scroll-mt-44  | scroll-margin-top: 11rem;                                    | 176px |
| scroll-mr-44  | scroll-margin-right: 11rem;                                  | 176px |
| scroll-mb-44  | scroll-margin-bottom: 11rem;                                 | 176px |
| scroll-ml-44  | scroll-margin-left: 11rem;                                   | 176px |
| scroll-mt-48  | scroll-margin-top: 12rem;                                    | 192px |
| scroll-mr-48  | scroll-margin-right: 12rem;                                  | 192px |
| scroll-mb-48  | scroll-margin-bottom: 12rem;                                 | 192px |
| scroll-ml-48  | scroll-margin-left: 12rem;                                   | 192px |
| scroll-mt-52  | scroll-margin-top: 13rem;                                    | 208px |
| scroll-mr-52  | scroll-margin-right: 13rem;                                  | 208px |
| scroll-mb-52  | scroll-margin-bottom: 13rem;                                 | 208px |
| scroll-ml-52  | scroll-margin-left: 13rem;                                   | 208px |
| scroll-mt-56  | scroll-margin-top: 14rem;                                    | 224px |
| scroll-mr-56  | scroll-margin-right: 14rem;                                  | 224px |
| scroll-mb-56  | scroll-margin-bottom: 14rem;                                 | 224px |
| scroll-ml-56  | scroll-margin-left: 14rem;                                   | 224px |
| scroll-mt-60  | scroll-margin-top: 15rem;                                    | 240px |
| scroll-mr-60  | scroll-margin-right: 15rem;                                  | 240px |
| scroll-mb-60  | scroll-margin-bottom: 15rem;                                 | 240px |
| scroll-ml-60  | scroll-margin-left: 15rem;                                   | 240px |
| scroll-mt-64  | scroll-margin-top: 16rem;                                    | 256px |
| scroll-mr-64  | scroll-margin-right: 16rem;                                  | 256px |
| scroll-mb-64  | scroll-margin-bottom: 16rem;                                 | 256px |
| scroll-ml-64  | scroll-margin-left: 16rem;                                   | 256px |
| scroll-mt-72  | scroll-margin-top: 18rem;                                    | 288px |
| scroll-mr-72  | scroll-margin-right: 18rem;                                  | 288px |
| scroll-mb-72  | scroll-margin-bottom: 18rem;                                 | 288px |
| scroll-ml-72  | scroll-margin-left: 18rem;                                   | 288px |
| scroll-mt-80  | scroll-margin-top: 20rem;                                    | 320px |
| scroll-mr-80  | scroll-margin-right: 20rem;                                  | 320px |
| scroll-mb-80  | scroll-margin-bottom: 20rem;                                 | 320px |
| scroll-ml-80  | scroll-margin-left: 20rem;                                   | 320px |
| scroll-mt-96  | scroll-margin-top: 24rem;                                    | 384px |
| scroll-mr-96  | scroll-margin-right: 24rem;                                  | 384px |
| scroll-mb-96  | scroll-margin-bottom: 24rem;                                 | 384px |
| scroll-ml-96  | scroll-margin-left: 24rem;                                   | 384px |
| scroll-mt-px  | scroll-margin-top: 1px;                                      |       |
| scroll-mr-px  | scroll-margin-right: 1px;                                    |       |
| scroll-mb-px  | scroll-margin-bottom: 1px;                                   |       |
| scroll-ml-px  | scroll-margin-left: 1px;                                     |       |





### Scroll Padding
Utilities for controlling an element's scroll offset within a snap container.

| Tailwind      | Description                                                    | Other |
| ------------- | -------------------------------------------------------------- | ----- |
| scroll-p-0    | scroll-padding: 0;                                             |       |
| scroll-p-0.5  | scroll-padding: 0.125rem;                                      | 2px   |
| scroll-p-1    | scroll-padding: 0.25rem;                                       | 4px   |
| scroll-p-1.5  | scroll-padding: 0.375rem;                                      | 6px   |
| scroll-p-2    | scroll-padding: 0.5rem;                                        | 8px   |
| scroll-p-2.5  | scroll-padding: 0.625rem;                                      | 10px  |
| scroll-p-3    | scroll-padding: 0.75rem;                                       | 12px  |
| scroll-p-3.5  | scroll-padding: 0.875rem;                                      | 14px  |
| scroll-p-4    | scroll-padding: 1rem;                                          | 16px  |
| scroll-p-5    | scroll-padding: 1.25rem;                                       | 20px  |
| scroll-p-6    | scroll-padding: 1.5rem;                                        | 24px  |
| scroll-p-8    | scroll-padding: 2rem;                                          | 32px  |
| scroll-p-10   | scroll-padding: 2.5rem;                                        | 40px  |
| scroll-p-11   | scroll-padding: 2.75rem;                                       | 44px  |
| scroll-p-12   | scroll-padding: 3rem;                                          | 48px  |
| scroll-p-14   | scroll-padding: 3.5rem;                                        | 56px  |
| scroll-p-16   | scroll-padding: 4rem;                                          | 64px  |
| scroll-p-20   | scroll-padding: 5rem;                                          | 80px  |
| scroll-p-24   | scroll-padding: 6rem;                                          | 96px  |
| scroll-p-28   | scroll-padding: 7rem;                                          | 112px |
| scroll-p-32   | scroll-padding: 8rem;                                          | 128px |
| scroll-p-36   | scroll-padding: 9rem;                                          | 144px |
| scroll-p-40   | scroll-padding: 10rem;                                         | 160px |
| scroll-p-44   | scroll-padding: 11rem;                                         | 176px |
| scroll-p-48   | scroll-padding: 12rem;                                         | 192px |
| scroll-p-52   | scroll-padding: 13rem;                                         | 208px |
| scroll-p-56   | scroll-padding: 14rem;                                         | 224px |
| scroll-p-64   | scroll-padding: 16rem;                                         | 256px |
| scroll-p-72   | scroll-padding: 18rem;                                         | 288px |
| scroll-p-80   | scroll-padding: 20rem;                                         | 320px |
| scroll-p-96   | scroll-padding: 24rem;                                         | 384px |
| scroll-p-px   | scroll-padding: 1px;                                           |       |
| scroll-py-0   | scroll-padding-top: 0; scroll-padding-bottom: 0;               |       |
| scroll-px-0   | scroll-padding-left: 0; scroll-padding-right: 0;               |       |
| scroll-py-0.5 | scroll-padding-top: 0.125rem; scroll-padding-bottom: 0.125rem; | 2px   |
| scroll-px-0.5 | scroll-padding-left: 0.125rem; scroll-padding-right: 0.125rem; | 2px   |
| scroll-py-1   | scroll-padding-top: 0.25rem; scroll-padding-bottom: 0.25rem;   | 4px   |
| scroll-px-1   | scroll-padding-left: 0.25rem; scroll-padding-right: 0.25rem;   | 4px   |
| scroll-py-1.5 | scroll-padding-top: 0.375rem; scroll-padding-bottom: 0.375rem; | 6px   |
| scroll-px-1.5 | scroll-padding-left: 0.375rem; scroll-padding-right: 0.375rem; | 6px   |
| scroll-py-2   | scroll-padding-top: 0.5rem; scroll-padding-bottom: 0.5rem;     | 8px   |
| scroll-px-2   | scroll-padding-left: 0.5rem; scroll-padding-right: 0.5rem;     | 8px   |
| scroll-py-2.5 | scroll-padding-top: 0.625rem; scroll-padding-bottom: 0.625rem; | 10px  |
| scroll-px-2.5 | scroll-padding-left: 0.625rem; scroll-padding-right: 0.625rem; | 10px  |
| scroll-py-3   | scroll-padding-top: 0.75rem; scroll-padding-bottom: 0.75rem;   | 12px  |
| scroll-px-3   | scroll-padding-left: 0.75rem; scroll-padding-right: 0.75rem;   | 12px  |
| scroll-py-3.5 | scroll-padding-top: 0.875rem; scroll-padding-bottom: 0.875rem; | 14px  |
| scroll-px-3.5 | scroll-padding-left: 0.875rem; scroll-padding-right: 0.875rem; | 14px  |
| scroll-py-4   | scroll-padding-top: 1rem; scroll-padding-bottom: 1rem;         | 16px  |
| scroll-px-4   | scroll-padding-left: 1rem; scroll-padding-right: 1rem;         | 16px  |
| scroll-py-5   | scroll-padding-top: 1.25rem; scroll-padding-bottom: 1.25rem;   | 20px  |
| scroll-px-5   | scroll-padding-left: 1.25rem; scroll-padding-right: 1.25rem;   | 20px  |
| scroll-py-6   | scroll-padding-top: 1.5rem; scroll-padding-bottom: 1.5rem;     | 24px  |
| scroll-px-6   | scroll-padding-left: 1.5rem; scroll-padding-right: 1.5rem;     | 24px  |
| scroll-py-7   | scroll-padding-top: 1.75rem; scroll-padding-bottom: 1.75rem;   | 24px  |
| scroll-px-7   | scroll-padding-left: 1.75rem; scroll-padding-right: 1.75rem;   | 24px  |
| scroll-py-8   | scroll-padding-top: 2rem; scroll-padding-bottom: 2rem;         | 32px  |
| scroll-px-8   | scroll-padding-left: 2rem; scroll-padding-right: 2rem;         | 32px  |
| scroll-py-9   | scroll-padding-top: 2.25rem; scroll-padding-bottom: 2.25rem;   | 36px  |
| scroll-px-9   | scroll-padding-left: 2.25rem; scroll-padding-right: 2.25rem;   | 36px  |
| scroll-py-10  | scroll-padding-top: 2.5rem; scroll-padding-bottom: 2.5rem;     | 40px  |
| scroll-px-10  | scroll-padding-left: 2.5rem; scroll-padding-right: 2.5rem;     | 40px  |
| scroll-py-11  | scroll-padding-top: 2.75rem; scroll-padding-bottom: 2.75rem;   | 44px  |
| scroll-px-11  | scroll-padding-left: 2.75rem; scroll-padding-right: 2.75rem;   | 44px  |
| scroll-py-12  | scroll-padding-top: 3rem; scroll-padding-bottom: 3rem;         | 48px  |
| scroll-px-12  | scroll-padding-left: 3rem; scroll-padding-right: 3rem;         | 48px  |
| scroll-py-14  | scroll-padding-top: 3.5rem; scroll-padding-bottom: 3.5rem;     | 56px  |
| scroll-px-14  | scroll-padding-left: 3.5rem; scroll-padding-right: 3.5rem;     | 56px  |
| scroll-py-16  | scroll-padding-top: 4rem; scroll-padding-bottom: 4rem;         | 64px  |
| scroll-px-16  | scroll-padding-left: 4rem; scroll-padding-right: 4rem;         | 64px  |
| scroll-py-20  | scroll-padding-top: 5rem; scroll-padding-bottom: 5rem;         | 80px  |
| scroll-px-20  | scroll-padding-left: 5rem; scroll-padding-right: 5rem;         | 80px  |
| scroll-py-24  | scroll-padding-top: 6rem; scroll-padding-bottom: 6rem;         | 96px  |
| scroll-px-24  | scroll-padding-left: 6rem; scroll-padding-right: 6rem;         | 96px  |
| scroll-py-28  | scroll-padding-top: 7rem; scroll-padding-bottom: 7rem;         | 112px |
| scroll-px-28  | scroll-padding-left: 7rem; scroll-padding-right: 7rem;         | 112px |
| scroll-py-32  | scroll-padding-top: 8rem; scroll-padding-bottom: 8rem;         | 128px |
| scroll-px-32  | scroll-padding-left: 8rem; scroll-padding-right: 8rem;         | 128px |
| scroll-py-36  | scroll-padding-top: 9rem; scroll-padding-bottom: 9rem;         | 144px |
| scroll-px-36  | scroll-padding-left: 9rem; scroll-padding-right: 9rem;         | 144px |
| scroll-py-40  | scroll-padding-top: 10rem; scroll-padding-bottom: 10rem;       | 160px |
| scroll-px-40  | scroll-padding-left: 10rem; scroll-padding-right: 10rem;       | 160px |
| scroll-py-44  | scroll-padding-top: 11rem; scroll-padding-bottom: 11rem;       | 176px |
| scroll-px-44  | scroll-padding-left: 11rem; scroll-padding-right: 11rem;       | 176px |
| scroll-py-48  | scroll-padding-top: 12rem; scroll-padding-bottom: 12rem;       | 192px |
| scroll-px-48  | scroll-padding-left: 12rem; scroll-padding-right: 12rem;       | 192px |
| scroll-py-52  | scroll-padding-top: 13rem; scroll-padding-bottom: 13rem;       | 208px |
| scroll-px-52  | scroll-padding-left: 13rem; scroll-padding-right: 13rem;       | 208px |
| scroll-py-56  | scroll-padding-top: 14rem; scroll-padding-bottom: 14rem;       | 224px |
| scroll-px-56  | scroll-padding-left: 14rem; scroll-padding-right: 14rem;       | 224px |
| scroll-py-60  | scroll-padding-top: 15rem; scroll-padding-bottom: 15rem;       | 240px |
| scroll-px-60  | scroll-padding-left: 15rem; scroll-padding-right: 15rem;       | 240px |
| scroll-py-64  | scroll-padding-top: 16rem; scroll-padding-bottom: 16rem;       | 256px |
| scroll-px-64  | scroll-padding-left: 16rem; scroll-padding-right: 16rem;       | 256px |
| scroll-py-70  | scroll-padding-top: 18rem; scroll-padding-bottom: 18rem;       | 280px |
| scroll-px-70  | scroll-padding-left: 18rem; scroll-padding-right: 18rem;       | 280px |
| scroll-py-80  | scroll-padding-top: 20rem; scroll-padding-bottom: 20rem;       | 320px |
| scroll-px-80  | scroll-padding-left: 20rem; scroll-padding-right: 20rem;       | 320px |
| scroll-py-96  | scroll-padding-top: 24rem; scroll-padding-bottom: 24rem;       | 384px |
| scroll-px-96  | scroll-padding-left: 24rem; scroll-padding-right: 24rem;       | 384px |
| scroll-py-px  | scroll-padding-top: 1px; scroll-padding-bottom: 1px;           |       |
| scroll-px-px  | scroll-padding-left: 1px; scroll-padding-right: 1px;           |       |
| scroll-pt-0   | scroll-padding-top: 0;                                         |       |
| scroll-pr-0   | scroll-padding-right: 0;                                       |       |
| scroll-pb-0   | scroll-padding-bottom: 0;                                      |       |
| scroll-pl-0   | scroll-padding-left: 0;                                        |       |
| scroll-pt-0.5 | scroll-padding-top: 0.125rem;                                  | 2px   |
| scroll-pr-0.5 | scroll-padding-right: 0.125rem;                                | 2px   |
| scroll-pb-0.5 | scroll-padding-bottom: 0.125rem;                               | 2px   |
| scroll-pl-0.5 | scroll-padding-left: 0.125rem;                                 | 2px   |
| scroll-pt-1   | scroll-padding-top: 0.25rem;                                   | 4px   |
| scroll-pr-1   | scroll-padding-right: 0.25rem;                                 | 4px   |
| scroll-pb-1   | scroll-padding-bottom: 0.25rem;                                | 4px   |
| scroll-pl-1   | scroll-padding-left: 0.25rem;                                  | 4px   |
| scroll-pt-1.5 | scroll-padding-top: 0.375rem;                                  | 6px   |
| scroll-pr-1.5 | scroll-padding-right: 0.375rem;                                | 6px   |
| scroll-pb-1.5 | scroll-padding-bottom: 0.375rem;                               | 6px   |
| scroll-pl-1.5 | scroll-padding-left: 0.375rem;                                 | 6px   |
| scroll-pt-2   | scroll-padding-top: 0.5rem;                                    | 8px   |
| scroll-pr-2   | scroll-padding-right: 0.5rem;                                  | 8px   |
| scroll-pb-2   | scroll-padding-bottom: 0.5rem;                                 | 8px   |
| scroll-pl-2   | scroll-padding-left: 0.5rem;                                   | 8px   |
| scroll-pt-2.5 | scroll-padding-top: 0.625rem;                                  | 10px  |
| scroll-pr-2.5 | scroll-padding-right: 0.625rem;                                | 10px  |
| scroll-pb-2.5 | scroll-padding-bottom: 0.625rem;                               | 10px  |
| scroll-pl-2.5 | scroll-padding-left: 0.625rem;                                 | 10px  |
| scroll-pt-3   | scroll-padding-top: 0.75rem;                                   | 12px  |
| scroll-pr-3   | scroll-padding-right: 0.75rem;                                 | 12px  |
| scroll-pb-3   | scroll-padding-bottom: 0.75rem;                                | 12px  |
| scroll-pl-3   | scroll-padding-left: 0.75rem;                                  | 12px  |
| scroll-pt-3.5 | scroll-padding-top: 0.875rem;                                  | 14px  |
| scroll-pr-3.5 | scroll-padding-right: 0.875rem;                                | 14px  |
| scroll-pb-3.5 | scroll-padding-bottom: 0.875rem;                               | 14px  |
| scroll-pl-3.5 | scroll-padding-left: 0.875rem;                                 | 14px  |
| scroll-pt-4   | scroll-padding-top: 1rem;                                      | 16px  |
| scroll-pr-4   | scroll-padding-right: 1rem;                                    | 16px  |
| scroll-pb-4   | scroll-padding-bottom: 1rem;                                   | 16px  |
| scroll-pl-4   | scroll-padding-left: 1rem;                                     | 16px  |
| scroll-pt-5   | scroll-padding-top: 1.25rem;                                   | 20px  |
| scroll-pr-5   | scroll-padding-right: 1.25rem;                                 | 20px  |
| scroll-pb-5   | scroll-padding-bottom: 1.25rem;                                | 20px  |
| scroll-pl-5   | scroll-padding-left: 1.25rem;                                  | 20px  |
| scroll-pt-6   | scroll-padding-top: 1.5rem;                                    | 24px  |
| scroll-pr-6   | scroll-padding-right: 1.5rem;                                  | 24px  |
| scroll-pb-6   | scroll-padding-bottom: 1.5rem;                                 | 24px  |
| scroll-pl-6   | scroll-padding-left: 1.5rem;                                   | 24px  |
| scroll-pt-7   | scroll-padding-top: 1.75rem;                                   | 28px  |
| scroll-pr-7   | scroll-padding-right: 1.75rem;                                 | 28px  |
| scroll-pb-7   | scroll-padding-bottom: 1.75rem;                                | 28px  |
| scroll-pl-7   | scroll-padding-left: 1.75rem;                                  | 28px  |
| scroll-pt-8   | scroll-padding-top: 2rem;                                      | 32px  |
| scroll-pr-8   | scroll-padding-right: 2rem;                                    | 32px  |
| scroll-pb-8   | scroll-padding-bottom: 2rem;                                   | 32px  |
| scroll-pl-8   | scroll-padding-left: 2rem;                                     | 32px  |
| scroll-pt-9   | scroll-padding-top: 2.25rem;                                   | 36px  |
| scroll-pr-9   | scroll-padding-right: 2.25rem;                                 | 36px  |
| scroll-pb-9   | scroll-padding-bottom: 2.25rem;                                | 36px  |
| scroll-pl-9   | scroll-padding-left: 2.25rem;                                  | 36px  |
| scroll-pt-10  | scroll-padding-top: 2.5rem;                                    | 40px  |
| scroll-pr-10  | scroll-padding-right: 2.5rem;                                  | 40px  |
| scroll-pb-10  | scroll-padding-bottom: 2.5rem;                                 | 40px  |
| scroll-pl-10  | scroll-padding-left: 2.5rem;                                   | 40px  |
| scroll-pt-11  | scroll-padding-top: 2.75rem;                                   | 44px  |
| scroll-pr-11  | scroll-padding-right: 2.75rem;                                 | 44px  |
| scroll-pb-11  | scroll-padding-bottom: 2.75rem;                                | 44px  |
| scroll-pl-11  | scroll-padding-left: 2.75rem;                                  | 44px  |
| scroll-pt-12  | scroll-padding-top: 3rem;                                      | 48px  |
| scroll-pr-12  | scroll-padding-right: 3rem;                                    | 48px  |
| scroll-pb-12  | scroll-padding-bottom: 3rem;                                   | 48px  |
| scroll-pl-12  | scroll-padding-left: 3rem;                                     | 48px  |
| scroll-pt-14  | scroll-padding-top: 3.5rem;                                    | 56px  |
| scroll-pr-14  | scroll-padding-right: 3.5rem;                                  | 56px  |
| scroll-pb-14  | scroll-padding-bottom: 3.5rem;                                 | 56px  |
| scroll-pl-14  | scroll-padding-left: 3.5rem;                                   | 56px  |
| scroll-pt-16  | scroll-padding-top: 4rem;                                      | 64px  |
| scroll-pr-16  | scroll-padding-right: 4rem;                                    | 64px  |
| scroll-pb-16  | scroll-padding-bottom: 4rem;                                   | 64px  |
| scroll-pl-16  | scroll-padding-left: 4rem;                                     | 64px  |
| scroll-pt-20  | scroll-padding-top: 5rem;                                      | 80px  |
| scroll-pr-20  | scroll-padding-right: 5rem;                                    | 80px  |
| scroll-pb-20  | scroll-padding-bottom: 5rem;                                   | 80px  |
| scroll-pl-20  | scroll-padding-left: 5rem;                                     | 80px  |
| scroll-pt-24  | scroll-padding-top: 6rem;                                      | 96px  |
| scroll-pr-24  | scroll-padding-right: 6rem;                                    | 96px  |
| scroll-pb-24  | scroll-padding-bottom: 6rem;                                   | 96px  |
| scroll-pl-24  | scroll-padding-left: 6rem;                                     | 96px  |
| scroll-pt-28  | scroll-padding-top: 7rem;                                      | 112px |
| scroll-pr-28  | scroll-padding-right: 7rem;                                    | 112px |
| scroll-pb-28  | scroll-padding-bottom: 7rem;                                   | 112px |
| scroll-pl-28  | scroll-padding-left: 7rem;                                     | 112px |
| scroll-pt-32  | scroll-padding-top: 8rem;                                      | 128px |
| scroll-pr-32  | scroll-padding-right: 8rem;                                    | 128px |
| scroll-pb-32  | scroll-padding-bottom: 8rem;                                   | 128px |
| scroll-pl-32  | scroll-padding-left: 8rem;                                     | 128px |
| scroll-pt-36  | scroll-padding-top: 9rem;                                      | 144px |
| scroll-pr-36  | scroll-padding-right: 9rem;                                    | 144px |
| scroll-pb-36  | scroll-padding-bottom: 9rem;                                   | 144px |
| scroll-pl-36  | scroll-padding-left: 9rem;                                     | 144px |
| scroll-pt-40  | scroll-padding-top: 10rem;                                     | 160px |
| scroll-pr-40  | scroll-padding-right: 10rem;                                   | 160px |
| scroll-pb-40  | scroll-padding-bottom: 10rem;                                  | 160px |
| scroll-pl-40  | scroll-padding-left: 10rem;                                    | 160px |
| scroll-pt-44  | scroll-padding-top: 11rem;                                     | 176px |
| scroll-pr-44  | scroll-padding-right: 11rem;                                   | 176px |
| scroll-pb-44  | scroll-padding-bottom: 11rem;                                  | 176px |
| scroll-pl-44  | scroll-padding-left: 11rem;                                    | 176px |
| scroll-pt-48  | scroll-padding-top: 12rem;                                     | 192px |
| scroll-pr-48  | scroll-padding-right: 12rem;                                   | 192px |
| scroll-pb-48  | scroll-padding-bottom: 12rem;                                  | 192px |
| scroll-pl-48  | scroll-padding-left: 12rem;                                    | 192px |
| scroll-pt-52  | scroll-padding-top: 13rem;                                     | 208px |
| scroll-pr-52  | scroll-padding-right: 13rem;                                   | 208px |
| scroll-pb-52  | scroll-padding-bottom: 13rem;                                  | 208px |
| scroll-pl-52  | scroll-padding-left: 13rem;                                    | 208px |
| scroll-pt-56  | scroll-padding-top: 14rem;                                     | 224px |
| scroll-pr-56  | scroll-padding-right: 14rem;                                   | 224px |
| scroll-pb-56  | scroll-padding-bottom: 14rem;                                  | 224px |
| scroll-pl-56  | scroll-padding-left: 14rem;                                    | 224px |
| scroll-pt-60  | scroll-padding-top: 15rem;                                     | 240px |
| scroll-pr-60  | scroll-padding-right: 15rem;                                   | 240px |
| scroll-pb-60  | scroll-padding-bottom: 15rem;                                  | 240px |
| scroll-pl-60  | scroll-padding-left: 15rem;                                    | 240px |
| scroll-pt-64  | scroll-padding-top: 16rem;                                     | 256px |
| scroll-pr-64  | scroll-padding-right: 16rem;                                   | 256px |
| scroll-pb-64  | scroll-padding-bottom: 16rem;                                  | 256px |
| scroll-pl-64  | scroll-padding-left: 16rem;                                    | 256px |
| scroll-pt-72  | scroll-padding-top: 18rem;                                     | 288px |
| scroll-pr-72  | scroll-padding-right: 18rem;                                   | 288px |
| scroll-pb-72  | scroll-padding-bottom: 18rem;                                  | 288px |
| scroll-pl-72  | scroll-padding-left: 18rem;                                    | 288px |
| scroll-pt-80  | scroll-padding-top: 20rem;                                     | 320px |
| scroll-pr-80  | scroll-padding-right: 20rem;                                   | 320px |
| scroll-pb-80  | scroll-padding-bottom: 20rem;                                  | 320px |
| scroll-pl-80  | scroll-padding-left: 20rem;                                    | 320px |
| scroll-pt-96  | scroll-padding-top: 24rem;                                     | 384px |
| scroll-pr-96  | scroll-padding-right: 24rem;                                   | 384px |
| scroll-pb-96  | scroll-padding-bottom: 24rem;                                  | 384px |
| scroll-pl-96  | scroll-padding-left: 24rem;                                    | 384px |
| scroll-pt-px  | scroll-padding-top: 1px;                                       |       |
| scroll-pr-px  | scroll-padding-right: 1px;                                     |       |
| scroll-pb-px  | scroll-padding-bottom: 1px;                                    |       |
| scroll-pl-px  | scroll-padding-left: 1px;                                      |       |





### Scroll Snap Align
Utilities for controlling the scroll snap alignment of an element.

| Tailwind        | Description                    | Other |
| --------------- | ------------------------------ | ----- |
| snap-start      | scroll-snap-align: start;      |       |
| snap-end        | scroll-snap-align: end;        |       |
| snap-center     | scroll-snap-align: center;     |       |
| snap-align-none | scroll-snap-align: align-none; |       |




### Scroll Snap Stop
Utilities for controlling whether you can skip past possible snap positions..

| Tailwind    | Description               | Other |
| ----------- | ------------------------- | ----- |
| snap-normal | scroll-snap-stop: normal; |       |
| snap-always | scroll-snap-stop: always; |       |




### Scroll Snap Type
Utilities for controlling how strictly snap points are enforced in a snap container.

| Tailwind       | Description                                              | Other |
| -------------- | -------------------------------------------------------- | ----- |
| snap-none      | scroll-snap-type: none;                                  |       |
| snap-x         | scroll-snap-type: x var(--tw-scroll-snap-strictness);    |       |
| snap-y         | scroll-snap-type: y var(--tw-scroll-snap-strictness);    |       |
| snap-both      | scroll-snap-type: both var(--tw-scroll-snap-strictness); |       |
| snap-mandatory | --tw-scroll-snap-strictness: mandatory;                  |       |
| snap-proximity | --tw-scroll-snap-strictness: proximity;                  |       |




### Touch Action
Utilities for controlling how an element can be scrolled and zoomed on touchscreens.

| Tailwind           | Description                 | Other |
| ------------------ | --------------------------- | ----- |
| touch-auto         | touch-action: auto;         |       |
| touch-none         | touch-action: none;         |       |
| touch-pan-x        | touch-action: pan-x;        |       |
| touch-pan-left     | touch-action: pan-left;     |       |
| touch-pan-right    | touch-action: pan-right;    |       |
| touch-pan-y        | touch-action: pan-y;        |       |
| touch-pan-up       | touch-action: pan-up;       |       |
| touch-pan-down     | touch-action: pan-down;     |       |
| touch-pinch-zoom   | touch-action: pinch-zoom;   |       |
| touch-manipulation | touch-action: manipulation; |       |




### User Select
Controls whether the user can select text.

| Tailwind    | Description        | Other |
| ----------- | ------------------ | ----- |
| select-none | user-select: none; |       |
| select-text | user-select: text; |       |
| select-all  | user-select: all;  |       |
| select-auto | user-select: auto; |       |




### Will Change
Utilities for optimizing upcoming animations of elements that are expected to change.

| Tailwind              | Description                   | Other |
| --------------------- | ----------------------------- | ----- |
| will-change-auto      | will-change: auto;            |       |
| will-change-scroll    | will-change: scroll-position; |       |
| will-change-contents  | will-change: contents;        |       |
| will-change-transform | will-change: transform;       |       |



---

## Filters


### Blur
Utilities for applying blur filters to an element.

| Tailwind  | Description       | Other |
| --------- | ----------------- | ----- |
| blur-none | blur: blur(0);    |       |
| blur-sm   | blur: blur(4px);  |       |
| blur      | blur: blur(8px);  |       |
| blur-md   | blur: blur(12px); |       |
| blur-lg   | blur: blur(16px); |       |
| blur-xl   | blur: blur(24px); |       |
| blur-2xl  | blur: blur(40px); |       |
| blur-3xl  | blur: blur(64px); |       |




### Brightness
Utilities for applying brightness filters to an element.

| Tailwind       | Description                   | Other |
| -------------- | ----------------------------- | ----- |
| brightness-0   | brightness: brightness(0);    |       |
| brightness-50  | brightness: brightness(.5);   |       |
| brightness-75  | brightness: brightness(.75);  |       |
| brightness-90  | brightness: brightness(.9);   |       |
| brightness-95  | brightness: brightness(.95);  |       |
| brightness-100 | brightness: brightness(1);    |       |
| brightness-105 | brightness: brightness(1.05); |       |
| brightness-110 | brightness: brightness(1.1);  |       |
| brightness-125 | brightness: brightness(1.25); |       |
| brightness-150 | brightness: brightness(1.5);  |       |
| brightness-200 | brightness: brightness(2);    |       |




### Contrast
Utilities for applying contrast filters to an element.

| Tailwind     | Description               | Other |
| ------------ | ------------------------- | ----- |
| contrast-0   | contrast: contrast(0);    |       |
| contrast-50  | contrast: contrast(.5);   |       |
| contrast-75  | contrast: contrast(.75);  |       |
| contrast-100 | contrast: contrast(1);    |       |
| contrast-125 | contrast: contrast(1.25); |       |
| contrast-150 | contrast: contrast(1.5);  |       |
| contrast-200 | contrast: contrast(2);    |       |




### Drop Shadow
Utilities for applying drop-shadow filters to an element.

| Tailwind         | Description                                                                                           | Other |
| ---------------- | ----------------------------------------------------------------------------------------------------- | ----- |
| drop-shadow-sm   | drop-shadow: drop-shadow(0 1px 1px rgba(0,0,0,0.05));                                                 |       |
| drop-shadow      | drop-shadow: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.1)) drop-shadow(0 1px 1px rgba(0, 0, 0, 0.06));    |       |
| drop-shadow-md   | drop-shadow: drop-shadow(0 4px 3px rgba(0, 0, 0, 0.07)) drop-shadow(0 2px 2px rgba(0, 0, 0, 0.06));   |       |
| drop-shadow-lg   | drop-shadow: drop-shadow(0 10px 8px rgba(0, 0, 0, 0.04)) drop-shadow(0 4px 3px rgba(0, 0, 0, 0.1));   |       |
| drop-shadow-xl   | drop-shadow: drop-shadow(0 20px 13px rgba(0, 0, 0, 0.03)) drop-shadow(0 8px 5px rgba(0, 0, 0, 0.08)); |       |
| drop-shadow-2xl  | drop-shadow: drop-shadow: drop-shadow(0 25px 25px rgba(0, 0, 0, 0.15));                               |       |
| drop-shadow-none | drop-shadow: drop-shadow: drop-shadow(0 0 #0000);                                                     |       |




### Grayscale
Utilities for applying grayscale filters to an element.

| Tailwind | Description | Other |
| -------- | ----------- | ----- |
|grayscale-0|	grayscale: grayscale(0);	||
|grayscale|	grayscale: grayscale(1);||




### Hue Rotate
Utilities for applying hue-rotate filters to an element.

| Tailwind       | Description                     | Other |
| -------------- | ------------------------------- | ----- |
| hue-rotate-0   | hue-rotate: hue-rotate(0deg);   |       |
| hue-rotate-15  | hue-rotate: hue-rotate(15deg);  |       |
| hue-rotate-30  | hue-rotate: hue-rotate(30deg);  |       |
| hue-rotate-60  | hue-rotate: hue-rotate(60deg);  |       |
| hue-rotate-90  | hue-rotate: hue-rotate(90deg);  |       |
| hue-rotate-180 | hue-rotate: hue-rotate(180deg); |       |




### Invert
Utilities for applying invert filters to an element.

| Tailwind | Description        | Other |
| -------- | ------------------ | ----- |
| invert-0 | invert: invert(0); |       |
| invert   | invert: invert(1); |       |



### Saturate
Utilities for applying saturation filters to an element.

| Tailwind     | Description               | Other |
| ------------ | ------------------------- | ----- |
| saturate-0   | saturate: saturate(0);    |       |
| saturate-50  | saturate: saturate(.5);   |       |
| saturate-100 | saturate: saturate(1);    |       |
| saturate-150 | saturate: saturate(1.50); |       |
| saturate-200 | saturate: saturate(2);    |       |



### Sepia
Utilities for applying sepia filters to an element.

| Tailwind | Description      | Other |
| -------- | ---------------- | ----- |
| sepia-0  | sepia: sepia(0); |       |
| sepia    | sepia: sepia(1); |       |




### Backdrop Blur
Utilities for applying backdrop blur filters to an element.

| Tailwind | Description | Other |
| -------- | ----------- | ----- |
|backdrop-blur-none	|backdrop-blur: blur(0);	||
|backdrop-blur-sm|	backdrop-blur: blur(4px);	||
|backdrop-blur	|backdrop-blur: blur(8px);	||
|backdrop-blur-md|	backdrop-blur: blur(12px);||	
|backdrop-blur-lg	|backdrop-blur: blur(16px);	||
|backdrop-blur-xl	|backdrop-blur: blur(24px);	||
|backdrop-blur-2xl|	backdrop-blur: blur(40px);||	
|backdrop-blur-3xl|	backdrop-blur: blur(64px);||



### Backdrop Brightness
Utilities for applying Backdrop Brightness filters to an element.

| Tailwind                | Description                            | Other |
| ----------------------- | -------------------------------------- | ----- |
| backdrop-brightness-0   | backdrop-brightness: brightness(0);    |       |
| backdrop-brightness-sm  | backdrop-brightness: brightness(4px);  |       |
| backdrop-brightness     | backdrop-brightness: brightness(8px);  |       |
| backdrop-brightness-md  | backdrop-brightness: brightness(12px); |       |
| backdrop-brightness-lg  | backdrop-brightness: brightness(16px); |       |
| backdrop-brightness-xl  | backdrop-brightness: brightness(24px); |       |
| backdrop-brightness-2xl | backdrop-brightness: brightness(40px); |       |
| backdrop-brightness-3xl | backdrop-brightness: brightness(64px); |       |


### Backdrop Contrast
Utilities for applying backdrop contrast filters to an element.

| Tailwind              | Description                        | Other |
| --------------------- | ---------------------------------- | ----- |
| backdrop-contrast-0   | backdrop-contrast: contrast(0);    |       |
| backdrop-contrast-50  | backdrop-contrast: contrast(.5);   |       |
| backdrop-contrast-75  | backdrop-contrast: contrast(.75);  |       |
| backdrop-contrast-100 | backdrop-contrast: contrast(1);    |       |
| backdrop-contrast-125 | backdrop-contrast: contrast(1.25); |       |
| backdrop-contrast-150 | backdrop-contrast: contrast(1.5);  |       |
| backdrop-contrast-200 | backdrop-contrast: contrast(2);    |       |



### Backdrop Grayscale
Utilities for applying backdrop grayscale filters to an element.

| Tailwind             | Description                       | Other |
| -------------------- | --------------------------------- | ----- |
| backdrop-grayscale-0 | backdrop-grayscale: grayscale(0); |       |
| backdrop-grayscale   | backdrop-grayscale: grayscale(1); |       |



### Backdrop Hue Rotate
Utilities for applying backdrop hue-rotate filters to an element.

| Tailwind                | Description                              | Other |
| ----------------------- | ---------------------------------------- | ----- |
| backdrop-hue-rotate-0   | backdrop-hue-rotate: hue-rotate(0deg);   |       |
| backdrop-hue-rotate-15  | backdrop-hue-rotate: hue-rotate(15deg);  |       |
| backdrop-hue-rotate-30  | backdrop-hue-rotate: hue-rotate(30deg);  |       |
| backdrop-hue-rotate-60  | backdrop-hue-rotate: hue-rotate(60deg);  |       |
| backdrop-hue-rotate-90  | backdrop-hue-rotate: hue-rotate(90deg);  |       |
| backdrop-hue-rotate-180 | backdrop-hue-rotate: hue-rotate(180deg); |       |



### Backdrop Invert
Utilities for applying backdrop invert filters to an element.

| Tailwind          | Description                 | Other |
| ----------------- | --------------------------- | ----- |
| backdrop-invert-0 | backdrop-invert: invert(0); |       |
| backdrop-invert   | backdrop-invert: invert(1); |       |




### Backdrop Opacity
Utilities for applying backdrop opacity filters to an element.

| Tailwind             | Description                      | Other |
| -------------------- | -------------------------------- | ----- |
| backdrop-opacity-0   | backdrop-opacity: opacity(0);    |       |
| backdrop-opacity-5   | backdrop-opacity: opacity(0.05); |       |
| backdrop-opacity-10  | backdrop-opacity: opacity(0.1);  |       |
| backdrop-opacity-20  | backdrop-opacity: opacity(0.2);  |       |
| backdrop-opacity-25  | backdrop-opacity: opacity(0.25); |       |
| backdrop-opacity-30  | backdrop-opacity: opacity(0.3);  |       |
| backdrop-opacity-40  | backdrop-opacity: opacity(0.4);  |       |
| backdrop-opacity-50  | backdrop-opacity: opacity(0.5);  |       |
| backdrop-opacity-60  | backdrop-opacity: opacity(0.6);  |       |
| backdrop-opacity-70  | backdrop-opacity: opacity(0.7);  |       |
| backdrop-opacity-75  | backdrop-opacity: opacity(0.75); |       |
| backdrop-opacity-80  | backdrop-opacity: opacity(0.8);  |       |
| backdrop-opacity-90  | backdrop-opacity: opacity(0.9);  |       |
| backdrop-opacity-95  | backdrop-opacity: opacity(0.95); |       |
| backdrop-opacity-100 | backdrop-opacity: opacity(1);    |       |




### Backdrop Saturate
Utilities for applying backdrop saturation filters to an element.

| Tailwind              | Description                        | Other |
| --------------------- | ---------------------------------- | ----- |
| backdrop-saturate-0   | backdrop-saturate: saturate(0);    |       |
| backdrop-saturate-50  | backdrop-saturate: saturate(.5);   |       |
| backdrop-saturate-100 | backdrop-saturate: saturate(1);    |       |
| backdrop-saturate-150 | backdrop-saturate: saturate(1.50); |       |
| backdrop-saturate-200 | backdrop-saturate: saturate(2);    |       |



### Backdrop Sepia
Utilities for applying backdrop sepia filters to an element.

| Tailwind         | Description               | Other |
| ---------------- | ------------------------- | ----- |
| backdrop-sepia-0 | backdrop-sepia: sepia(0); |       |
| backdrop-sepia   | backdrop-sepia: sepia(1); |       |


---

## Flexbox & Grid


### Flex Basis
Utilities for controlling the initial size of flex items.

| Tailwind    | Description             | Other |
| ----------- | ----------------------- | ----- |
| basis-0     | flex-basis: 0px;        |       |
| basis-0.5   | flex-basis: 0.125rem;   | 2px   |
| basis-1     | flex-basis: 0.25rem;    | 4px   |
| basis-1.5   | flex-basis: 0.375rem;   | 6px   |
| basis-2     | flex-basis: 0.5rem;     | 8px   |
| basis-2.5   | flex-basis: 0.625rem;   | 10px  |
| basis-3     | flex-basis: 0.75rem;    | 12px  |
| basis-3.5   | flex-basis: 0.875rem;   | 14px  |
| basis-4     | flex-basis: 1rem;       | 16px  |
| basis-5     | flex-basis: 1.25rem;    | 20px  |
| basis-6     | flex-basis: 1.5rem;     | 24px  |
| basis-7     | flex-basis: 1.75rem;    | 28px  |
| basis-8     | flex-basis: 2rem;       | 32px  |
| basis-9     | flex-basis: 2.25rem;    | 36px  |
| basis-10    | flex-basis: 2.5rem;     | 40px  |
| basis-11    | flex-basis: 2.75rem;    | 44px  |
| basis-12    | flex-basis: 3rem;       | 48px  |
| basis-14    | flex-basis: 3.5rem;     | 56px  |
| basis-16    | flex-basis: 4rem;       | 64px  |
| basis-20    | flex-basis: 5rem;       | 80px  |
| basis-24    | flex-basis: 6rem;       | 96px  |
| basis-28    | flex-basis: 7rem;       | 112px |
| basis-32    | flex-basis: 8rem;       | 128px |
| basis-36    | flex-basis: 9rem;       | 144px |
| basis-40    | flex-basis: 10rem;      | 160px |
| basis-44    | flex-basis: 11rem;      | 176px |
| basis-48    | flex-basis: 12rem;      | 192px |
| basis-52    | flex-basis: 13rem;      | 208px |
| basis-56    | flex-basis: 14rem;      | 224px |
| basis-60    | flex-basis: 15rem;      | 240px |
| basis-64    | flex-basis: 16rem;      | 256px |
| basis-72    | flex-basis: 18rem;      | 288px |
| basis-80    | flex-basis: 20rem;      | 320px |
| basis-96    | flex-basis: 24rem;      | 384px |
| basis-auto  | flex-basis: auto;       |       |
| basis-px    | flex-basis: 1px;        |       |
| basis-1/2   | flex-basis: 50%;        |       |
| basis-1/3   | flex-basis: 33.333333%; |       |
| basis-2/3   | flex-basis: 66.666667%; |       |
| basis-1/4   | flex-basis: 25%;        |       |
| basis-2/4   | flex-basis: 50%;        |       |
| basis-3/4   | flex-basis: 75%;        |       |
| basis-1/5   | flex-basis: 20%;        |       |
| basis-2/5   | flex-basis: 40%;        |       |
| basis-3/5   | flex-basis: 60%;        |       |
| basis-4/5   | flex-basis: 80%;        |       |
| basis-1/6   | flex-basis: 16.666667%; |       |
| basis-2/6   | flex-basis: 33.333333%; |       |
| basis-3/6   | flex-basis: 50%;        |       |
| basis-4/6   | flex-basis: 66.666667%; |       |
| basis-5/6   | flex-basis: 83.333333%; |       |
| basis-1/12  | flex-basis: 8.333333%;  |       |
| basis-2/12  | flex-basis: 16.666667%; |       |
| basis-3/12  | flex-basis: 25%;        |       |
| basis-4/12  | flex-basis: 33.333333%; |       |
| basis-5/12  | flex-basis: 41.666667%; |       |
| basis-6/12  | flex-basis: 50%;        |       |
| basis-7/12  | flex-basis: 58.333333%; |       |
| basis-8/12  | flex-basis: 66.666667%; |       |
| basis-9/12  | flex-basis: 75%;        |       |
| basis-10/12 | flex-basis: 83.333333%; |       |
| basis-11/12 | flex-basis: 91.666667%; |       |
| basis-full  | flex-basis: 100%;       |       |




### Flex Direction
Sets direction of flex items.

| Tailwind         | Description                     | Other |
| ---------------- | ------------------------------- | ----- |
| flex-row         | flex-direction: row;            |       |
| flex-row-reverse | flex-direction: row-reverse;    |       |
| flex-col         | flex-direction: column;         |       |
| flex-col-reverse | flex-direction: column-reverse; |       |



### Flex Wrap
Creates how flex items wrap.

| Tailwind          | Description              | Other |
| ----------------- | ------------------------ | ----- |
| flex-nowrap       | flex-wrap: nowrap;       |       |
| flex-wrap         | flex-wrap: wrap;         |       |
| flex-wrap-reverse | flex-wrap: wrap-reverse; |       |



### Flex
Controls how flex items grow and shrink.

| Tailwind     | Description     | Other |
| ------------ | --------------- | ----- |
| flex-1       | flex: 1 1 0%;   |       |
| flex-auto    | flex: 1 1 auto; |       |
| flex-initial | flex: 0 1 auto; |       |
| flex-none    | flex: none;     |       |


### Flex Grow
Controls how flex items grow.

| Tailwind  | Description   | Other |
| --------- | ------------- | ----- |
| flex-grow | flex-grow: 1; |       |
| grow-0    | flex-grow: 0; |       |



### Flex Shrink
Controls how flex items shrink.

| Tailwind | Description | Other |
| -------- | ----------- | ----- |
| shrink   | shrink: 1;  |       |
| shrink-0 | shrink: 0;  |       |





### Order
Controls how flex items are ordered.

| Tailwind    | Description   | Other |
| ----------- | ------------- | ----- |
| order-first | order: -9999; |       |
| order-last  | order: 9999;  |       |
| order-none  | order: 0;     |       |
| order-1     | order: 1;     |       |
| order-2     | order: 2;     |       |
| order-3     | order: 3;     |       |
| order-4     | order: 4;     |       |
| order-5     | order: 5;     |       |
| order-6     | order: 6;     |       |
| order-7     | order: 7;     |       |
| order-8     | order: 8;     |       |
| order-9     | order: 9;     |       |
| order-10    | order: 10;    |       |
| order-11    | order: 11;    |       |
| order-12    | order: 12;    |       |



### Grid Template Columns
Defines columns for grid layout.

| Tailwind       | Description                                        | Other |
| -------------- | -------------------------------------------------- | ----- |
| grid-cols-1    | grid-template-columns: repeat(1, minmax(0, 1fr));  |       |
| grid-cols-2    | grid-template-columns: repeat(2, minmax(0, 1fr));  |       |
| grid-cols-3    | grid-template-columns: repeat(3, minmax(0, 1fr));  |       |
| grid-cols-4    | grid-template-columns: repeat(4, minmax(0, 1fr));  |       |
| grid-cols-5    | grid-template-columns: repeat(5, minmax(0, 1fr));  |       |
| grid-cols-6    | grid-template-columns: repeat(6, minmax(0, 1fr));  |       |
| grid-cols-7    | grid-template-columns: repeat(7, minmax(0, 1fr));  |       |
| grid-cols-8    | grid-template-columns: repeat(8, minmax(0, 1fr));  |       |
| grid-cols-9    | grid-template-columns: repeat(9, minmax(0, 1fr));  |       |
| grid-cols-10   | grid-template-columns: repeat(10, minmax(0, 1fr)); |       |
| grid-cols-11   | grid-template-columns: repeat(11, minmax(0, 1fr)); |       |
| grid-cols-12   | grid-template-columns: repeat(12, minmax(0, 1fr)); |       |
| grid-cols-none | grid-template-columns: none;                       |       |



### Grid Column, start/end
Sets a grid item size and location within the grid column.

| Tailwind       | Description                     | Other |
| -------------- | ------------------------------- | ----- |
| col-auto       | grid-column: auto;              |       |
| col-span-1     | grid-column: span 1 / span 1;   |       |
| col-span-2     | grid-column: span 2 / span 2;   |       |
| col-span-3     | grid-column: span 3 / span 3;   |       |
| col-span-4     | grid-column: span 4 / span 4;   |       |
| col-span-5     | grid-column: span 5 / span 5;   |       |
| col-span-6     | grid-column: span 6 / span 6;   |       |
| col-span-7     | grid-column: span 7 / span 7;   |       |
| col-span-8     | grid-column: span 8 / span 8;   |       |
| col-span-9     | grid-column: span 9 / span 9;   |       |
| col-span-10    | grid-column: span 10 / span 10; |       |
| col-span-11    | grid-column: span 11 / span 11; |       |
| col-span-12    | grid-column: span 12 / span 12; |       |
| col-start-1    | grid-column-start: 1;           |       |
| col-start-2    | grid-column-start: 2;           |       |
| col-start-3    | grid-column-start: 3;           |       |
| col-start-4    | grid-column-start: 4;           |       |
| col-start-5    | grid-column-start: 5;           |       |
| col-start-6    | grid-column-start: 6;           |       |
| col-start-7    | grid-column-start: 7;           |       |
| col-start-8    | grid-column-start: 8;           |       |
| col-start-9    | grid-column-start: 9;           |       |
| col-start-10   | grid-column-start: 10;          |       |
| col-start-11   | grid-column-start: 11;          |       |
| col-start-12   | grid-column-start: 12;          |       |
| col-start-13   | grid-column-start: 13;          |       |
| col-start-auto | grid-column-start: auto;        |       |
| col-end-1      | grid-column-end: 1;             |       |
| col-end-2      | grid-column-end: 2;             |       |
| col-end-3      | grid-column-end: 3;             |       |
| col-end-4      | grid-column-end: 4;             |       |
| col-end-5      | grid-column-end: 5;             |       |
| col-end-6      | grid-column-end: 6;             |       |
| col-end-7      | grid-column-end: 7;             |       |
| col-end-8      | grid-column-end: 8;             |       |
| col-end-9      | grid-column-end: 9;             |       |
| col-end-10     | grid-column-end: 10;            |       |
| col-end-11     | grid-column-end: 11;            |       |
| col-end-12     | grid-column-end: 12;            |       |
| col-end-13     | grid-column-end: 13;            |       |
| col-end-auto   | grid-column-end: auto;          |       |



### Grid Template Rows
Defines rows for grid layout.

| Tailwind       | Description                                    | Other |
| -------------- | ---------------------------------------------- | ----- |
| grid-rows-1    | grid-template-rows: repeat(1, minmax(0, 1fr)); |       |
| grid-rows-2    | grid-template-rows: repeat(2, minmax(0, 1fr)); |       |
| grid-rows-3    | grid-template-rows: repeat(3, minmax(0, 1fr)); |       |
| grid-rows-4    | grid-template-rows: repeat(4, minmax(0, 1fr)); |       |
| grid-rows-5    | grid-template-rows: repeat(5, minmax(0, 1fr)); |       |
| grid-rows-6    | grid-template-rows: repeat(6, minmax(0, 1fr)); |       |
| grid-rows-none | grid-template-rows: none;                      |       |



### Grid Row, start/end
Sets a grid item size and location within the grid row.

| Tailwind       | Description                | Other |
| -------------- | -------------------------- | ----- |
| row-auto       | grid-row: auto;            |       |
| row-span-1     | grid-row: span 1 / span 1; |       |
| row-span-2     | grid-row: span 2 / span 2; |       |
| row-span-3     | grid-row: span 3 / span 3; |       |
| row-span-4     | grid-row: span 4 / span 4; |       |
| row-span-5     | grid-row: span 5 / span 5; |       |
| row-span-6     | grid-row: span 6 / span 6; |       |
| row-start-1    | grid-row-start: 1;         |       |
| row-start-2    | grid-row-start: 2;         |       |
| row-start-3    | grid-row-start: 3;         |       |
| row-start-4    | grid-row-start: 4;         |       |
| row-start-5    | grid-row-start: 5;         |       |
| row-start-6    | grid-row-start: 6;         |       |
| row-start-7    | grid-row-start: 7;         |       |
| row-start-auto | grid-row-start: auto;      |       |
| row-end-1      | grid-row-end: 1;           |       |
| row-end-2      | grid-row-end: 2;           |       |
| row-end-3      | grid-row-end: 3;           |       |
| row-end-4      | grid-row-end: 4;           |       |
| row-end-5      | grid-row-end: 5;           |       |
| row-end-6      | grid-row-end: 6;           |       |
| row-end-7      | grid-row-end: 7;           |       |
| row-end-auto   | grid-row-end: auto;        |       |




### Grid Auto Flow
Controls the auto placement of grid elements.

| Tailwind            | Description                   | Other |
| ------------------- | ----------------------------- | ----- |
| grid-flow-row       | grid-auto-flow: row;          |       |
| grid-flow-col       | grid-auto-flow: column;       |       |
| grid-flow-row-dense | grid-auto-flow: row dense;    |       |
| grid-flow-col-dense | grid-auto-flow: column dense; |       |




### Grid Auto Columns
Utilities for controlling the size of implicitly-created grid columns.

| Tailwind       | Description                        | Other |
| -------------- | ---------------------------------- | ----- |
| auto-cols-auto | grid-auto-columns: auto;           |       |
| auto-cols-min  | grid-auto-columns: min;            |       |
| auto-cols-max  | grid-auto-columns: max;            |       |
| auto-cols-fr   | grid-auto-columns: minmax(0, 1fr); |       |




### Grid Auto Rows
Utilities for controlling the size of implicitly-created grid rows.

| Tailwind       | Description                     | Other |
| -------------- | ------------------------------- | ----- |
| auto-rows-auto | grid-auto-rows: auto;           |       |
| auto-rows-min  | grid-auto-rows: min;            |       |
| auto-rows-max  | grid-auto-rows: max;            |       |
| auto-rows-fr   | grid-auto-rows: minmax(0, 1fr); |       |



### Gap
Sets the gaps (gutters) between rows and columns.

| Tailwind | Description | Other |
| -------- | ----------- | ----- |
|gap-0|gap: 0;||
|gap-0.5|gap: 0.125rem;|2px|
|gap-1|gap: 0.25rem;|4px|
|gap-1.5|gap: 0.375rem;|6px|
|gap-2|gap: 0.5rem;|8px|
|gap-2.5|gap: 0.625rem;|10px|
|gap-3|gap: 0.75rem;|12px|
|gap-3.5|gap: 0.875rem;|14px|
|gap-4|gap: 1rem;|16px|
|gap-5|gap: 1.25rem;|20px|
|gap-6|gap: 1.5rem;|24px|
|gap-8|gap: 2rem;|32px|
|gap-10|gap: 2.5rem;|40px|
|gap-11|gap: 2.75rem;|44px|
|gap-12|gap: 3rem;|48px|
|gap-14|gap: 3.5rem;|56px|
|gap-16|gap: 4rem;|64px|
|gap-20|gap: 5rem;|80px|
|gap-24|gap: 6rem;|96px|
|gap-28|gap: 7rem;|112px|
|gap-32|gap: 8rem;|128px|
|gap-36|gap: 9rem;|144px|
|gap-40|gap: 10rem;|160px|
|gap-44|gap: 11rem;|176px|
|gap-48|gap: 12rem;|192px|
|gap-52|gap: 13rem;|208px|
|gap-56|gap: 14rem;|224px|
|gap-64|gap: 16rem;|256px|
|gap-72|gap: 18rem;|288px|
|gap-80|gap: 20rem;|320px|
|gap-96|gap: 24rem;|384px|
|gap-px|gap: 1px;||
|gap-x-0|column-gap: 0;||
|gap-x-0.5|column-gap: 0.125rem;|2px|
|gap-x-1|column-gap: 0.25rem;|4px|
|gap-x-1.5|column-gap: 0.375rem;|6px|
|gap-x-2|column-gap: 0.5rem;|8px|
|gap-x-2.5|column-gap: 0.625rem;|10px|
|gap-x-3|column-gap: 0.75rem;|12px|
|gap-x-3.5|column-gap: 0.875rem;|14px|
|gap-x-4|column-gap: 1rem;|16px|
|gap-x-5|column-gap: 1.25rem;|20px|
|gap-x-6|column-gap: 1.5rem;|24px|
|gap-x-8|column-gap: 2rem;|32px|
|gap-x-10|column-gap: 2.5rem;|40px|
|gap-x-11|column-gap: 2.75rem;|44px|
|gap-x-12|column-gap: 3rem;|48px|
|gap-x-14|column-gap: 3.5rem;|56px|
|gap-x-16|column-gap: 4rem;|64px|
|gap-x-20|column-gap: 5rem;|80px|
|gap-x-24|column-gap: 6rem;|96px|
|gap-x-28|column-gap: 7rem;|112px|
|gap-x-32|column-gap: 8rem;|128px|
|gap-x-36|column-gap: 9rem;|144px|
|gap-x-40|column-gap: 10rem;|160px|
|gap-x-44|column-gap: 11rem;|176px|
|gap-x-48|column-gap: 12rem;|192px|
|gap-x-52|column-gap: 13rem;|208px|
|gap-x-56|column-gap: 14rem;|224px|
|gap-x-64|column-gap: 16rem;|256px|
|gap-x-72|column-gap: 18rem;|288px|
|gap-x-80|column-gap: 20rem;|320px|
|gap-x-96|column-gap: 24rem;|384px|
|gap-x-px|column-gap: 1px;||
|gap-y-0|row-gap: 0;||
|gap-y-0.5|row-gap: 0.125rem;|2px|
|gap-y-1|row-gap: 0.25rem;|4px|
|gap-y-1.5|row-gap: 0.375rem;|6px|
|gap-y-2|row-gap: 0.5rem;|8px|
|gap-y-2.5|row-gap: 0.625rem;|10px|
|gap-y-3|row-gap: 0.75rem;|12px|
|gap-y-3.5|row-gap: 0.875rem;|14px|
|gap-y-4|row-gap: 1rem;|16px|
|gap-y-5|row-gap: 1.25rem;|20px|
|gap-y-6|row-gap: 1.5rem;|24px|
|gap-y-8|row-gap: 2rem;|32px|
|gap-y-10|row-gap: 2.5rem;|40px|
|gap-y-11|row-gap: 2.75rem;|44px|
|gap-y-12|row-gap: 3rem;|48px|
|gap-y-14|row-gap: 3.5rem;|56px|
|gap-y-16|row-gap: 4rem;|64px|
|gap-y-20|row-gap: 5rem;|80px|
|gap-y-24|row-gap: 6rem;|96px|
|gap-y-28|row-gap: 7rem;|112px|
|gap-y-32|row-gap: 8rem;|128px|
|gap-y-36|row-gap: 9rem;|144px|
|gap-y-40|row-gap: 10rem;|160px|
|gap-y-44|row-gap: 11rem;|176px|
|gap-y-48|row-gap: 12rem;|192px|
|gap-y-52|row-gap: 13rem;|208px|
|gap-y-56|row-gap: 14rem;|224px|
|gap-y-64|row-gap: 16rem;|256px|
|gap-y-72|row-gap: 18rem;|288px|
|gap-y-80|row-gap: 20rem;|320px|
|gap-y-96|row-gap: 24rem;|384px|
|gap-y-px|row-gap: 1px;||








### Justify Content
Utilities for controlling how flex and grid items are positioned along a container's main axis.

| Tailwind        | Description                     | Other |
| --------------- | ------------------------------- | ----- |
| justify-start   | justify-content: flex-start;    |       |
| justify-center  | justify-content: center;        |       |
| justify-end     | justify-content: flex-end;      |       |
| justify-between | justify-content: space-between; |       |
| justify-around  | justify-content: space-around;  |       |
| justify-evenly  | justify-content: space-evenly;  |       |




### Justify Items
Utilities for controlling how grid items are aligned along their inline axis.

| Tailwind              | Description             | Other |
| --------------------- | ----------------------- | ----- |
| justify-items-stretch | justify-items: stretch; |       |
| justify-items-start   | justify-items: start;   |       |
| justify-items-center  | justify-items: center;  |       |
| justify-items-end     | justify-items: end;     |       |



### Justify Self
Utilities for controlling how an individual grid item is aligned along its inline axis.

| Tailwind             | Description            | Other |
| -------------------- | ---------------------- | ----- |
| justify-self-stretch | justify-self: stretch; |       |
| justify-self-start   | justify-self: start;   |       |
| justify-self-center  | justify-self: center;  |       |
| justify-self-end     | justify-self: end;     |       |
| justify-self-auto    | justify-self: auto;    |       |



### Align Content
Utilities for controlling how rows are positioned in multi-row flex and grid containers.

| Tailwind        | Description                   | Other |
| --------------- | ----------------------------- | ----- |
| content-start   | align-content: flex-start;    |       |
| content-center  | align-content: center;        |       |
| content-end     | align-content: flex-end;      |       |
| content-between | align-content: space-between; |       |
| content-around  | align-content: space-around;  |       |
| content-evenly  | align-content: space-evenly;  |       |




### Align Items
Sets flex items position along a contrainer's cross axis.

| Tailwind       | Description              | Other |
| -------------- | ------------------------ | ----- |
| items-stretch  | align-items: stretch;    |       |
| items-start    | align-items: flex-start; |       |
| items-center   | align-items: center;     |       |
| items-end      | align-items: flex-end;   |       |
| items-baseline | align-items: baseline;   |       |



### Align Self
Controls how an individual flex item is positioned along container's cross axis.

| Tailwind      | Description             | Other |
| ------------- | ----------------------- | ----- |
| self-auto     | align-self: auto;       |       |
| self-start    | align-self: flex-start; |       |
| self-center   | align-self: center;     |       |
| self-end      | align-self: flex-end;   |       |
| self-stretch  | align-self: stretch;    |       |
| self-baseline | align-self: baseline;   |       |




### Place Content
Utilities for controlling how content is justified and aligned at the same time.

| Tailwind              | Description                   | Other |
| --------------------- | ----------------------------- | ----- |
| place-content-start   | place-content: start;         |       |
| place-content-center  | place-content: center;        |       |
| place-content-end     | place-content: end;           |       |
| place-content-between | place-content: space-between; |       |
| place-content-around  | place-content: space-around;  |       |
| place-content-evenly  | place-content: space-evenly;  |       |
| place-content-stretch | place-content: space-stretch; |       |




### Place Items
Utilities for controlling how items are justified and aligned at the same time.

| Tailwind            | Description           | Other |
| ------------------- | --------------------- | ----- |
| place-items-stretch | place-items: stretch; |       |
| place-items-start   | place-items: start;   |       |
| place-items-center  | place-items: center;  |       |
| place-items-end     | place-items: end;     |       |




### Place Self
Utilities for controlling how an individual item is justified and aligned at the same time.

| Tailwind           | Description          | Other |
| ------------------ | -------------------- | ----- |
| place-self-auto    | place-self: auto;    |       |
| place-self-start   | place-self: start;   |       |
| place-self-center  | place-self: center;  |       |
| place-self-end     | place-self: end;     |       |
| place-self-stretch | place-self: stretch; |       |

---

## Backgrounds


### Background Attachment
Sets behavior of background images when scrolling.

| Tailwind  | Description                    | Other |
| --------- | ------------------------------ | ----- |
| bg-fixed  | background-attachment: fixed;  |       |
| bg-local  | background-attachment: local;  |       |
| bg-scroll | background-attachment: scroll; |       |



### Background Clip
Sets behavior of Utilities for controlling the bounding box of an element's background.

| Tailwind        | Description                   | Other |
| --------------- | ----------------------------- | ----- |
| bg-clip-border  | background-clip: border-box;  |       |
| bg-clip-padding | background-clip: padding-box; |       |
| bg-clip-content | background-clip: content-box; |       |
| bg-clip-text    | background-clip: text;        |       |



### Background Color
Sets background color.

| Tailwind       | Description                      | Other |
| -------------- | -------------------------------- | ----- |
| bg-transparent | background-color: transparent;   |       |
| bg-current     | background-color: currentColor;  |       |
| bg-black       | background-color: `#000000;`     |       |
| bg-white       | background-color: `#ffffff;`     |       |
| bg-gray-50     | background-color: `#F9FAFB;`     |       |
| bg-gray-100    | background-color: `#F3F4F6;`     |       |
| bg-gray-200    | background-color: `#E5E7EB;`     |       |
| bg-gray-300    | background-color: `#D1D5DB;`     |       |
| bg-gray-400    | background-color: `#9CA3AF;`     |       |
| bg-gray-500    | background-color: `#6B7280;`     |       |
| bg-gray-600    | background-color: `#6B7280;`     |       |
| bg-gray-700    | background-color: `#374151;`     |       |
| bg-gray-800    | background-color: `#1F2937;`     |       |
| bg-gray-900    | background-color: `#111827;`     |       |
| bg-red-50      | background-color: `#FEF2F2;`     |       |
| bg-red-100     | background-color: `#FEE2E2;`     |       |
| bg-red-200     | background-color: `#FECACA;`     |       |
| bg-red-300     | background-color: `#FCA5A5;`     |       |
| bg-red-400     | background-color: `#F87171;`     |       |
| bg-red-500     | background-color: `#EF4444;`     |       |
| bg-red-600     | background-color: `#DC2626;`     |       |
| bg-red-700     | background-color: `#B91C1C;`     |       |
| bg-red-800     | background-color: `#991B1B;`     |       |
| bg-red-900     | background-color: `#7F1D1D;`     |       |
| bg-yellow-50   | background-color: `#FFFBEB;`     |       |
| bg-yellow-100  | background-color: `#FEF3C7;`     |       |
| bg-yellow-200  | background-color: `#FDE68A;`     |       |
| bg-yellow-300  | background-color: `#FCD34D;`     |       |
| bg-yellow-400  | background-color: `#FBBF24;`     |       |
| bg-yellow-500  | background-color: `#F59E0B;`     |       |
| bg-yellow-600  | background-color: `#D97706;`     |       |
| bg-yellow-700  | background-color: `#B45309;`     |       |
| bg-yellow-800  | background-color: `#92400E;`     |       |
| bg-yellow-900  | background-color: `#78350F;`     |       |
| bg-green-50    | background-color: `#ECFDF5;`     |       |
| bg-green-100   | background-color: `#D1FAE5;`     |       |
| bg-green-200   | background-color: `#A7F3D0;`     |       |
| bg-green-300   | background-color: `#6EE7B7;`     |       |
| bg-green-400   | background-color: `#34D399;`     |       |
| bg-green-500   | background-color: `#10B981;`     |       |
| bg-green-600   | background-color: `#059669;`     |       |
| bg-green-700   | background-color: `#047857;`     |       |
| bg-green-800   | background-color: `#065F46;`     |       |
| bg-green-900   | background-color: `#064E3B;`     |       |
| bg-blue-50     | background-color: `#EFF6FF;`     |       |
| bg-blue-100    | background-color: `#DBEAFE;`     |       |
| bg-blue-200    | background-color: `#BFDBFE;`     |       |
| bg-blue-300    | background-color: `#93C5FD;`     |       |
| bg-blue-400    | background-color: `#60A5FA;`     |       |
| bg-blue-500    | background-color: `#3B82F6;`     |       |
| bg-blue-600    | background-color: `#2563EB;`     |       |
| bg-blue-700    | background-color: `#1D4ED8;`     |       |
| bg-blue-800    | background-color: `#1E40AF;`     |       |
| bg-blue-900    | background-color: `#1E3A8A;`     |       |
| bg-indigo-50   | background-color: `#EEF2FF;`     |       |
| bg-indigo-100  | background-color: `#E0E7FF;`     |       |
| bg-indigo-200  | background-color: `#C7D2FE;`     |       |
| bg-indigo-300  | background-color: `#A5B4FC;`     |       |
| bg-indigo-400  | background-color: `#818CF8;`     |       |
| bg-indigo-500  | background-color: `#6366F1;`     |       |
| bg-indigo-600  | background-color: `#4F46E5;`     |       |
| bg-indigo-700  | background-color: `#4338CA;`     |       |
| bg-indigo-800  | background-color: `#3730A3;`     |       |
| bg-indigo-900  | background-color: `#312E81;`     |       |
| bg-purple-50   | background-color: `#F5F3FF;`     |       |
| bg-purple-100  | background-color: `#EDE9FE;`     |       |
| bg-purple-200  | background-color: `#DDD6FE;`     |       |
| bg-purple-300  | background-color: `#C4B5FD;`     |       |
| bg-purple-400  | background-color: `#A78BFA;`     |       |
| bg-purple-500  | background-color: `#8B5CF6;`     |       |
| bg-purple-600  | background-color: `#7C3AED;`     |       |
| bg-purple-700  | background-color: `#6D28D9;`     |       |
| bg-purple-800  | background-color: `#5B21B6;`     |       |
| bg-purple-900  | background-color: `#4C1D95;`     |       |
| bg-pink-50     | background-color: `#FDF2F8;`     |       |
| bg-pink-100    | background-color: `#FCE7F3;`     |       |
| bg-pink-200    | background-color: `#FBCFE8;`     |       |
| bg-pink-300    | background-color: `#F9A8D4;`     |       |
| bg-pink-400    | background-color: `#F472B6;`     |       |
| bg-pink-500    | background-color: `#EC4899;`     |       |
| bg-pink-600    | background-color: `#DB2777;`     |       |
| bg-pink-700    | background-color: `#BE185D;`     |       |
| bg-pink-800    | background-color: `#9D174D;`     |       |
| bg-pink-900    | background-color: `#831843;`     |       |



















### Background Opacity
Sets background opacity.

| Tailwind       | Description         | Other |
| -------------- | ------------------- | ----- |
| bg-opacity-0   | --bg-opacity: 0;    |       |
| bg-opacity-5   | --bg-opacity: 0.5;  |       |
| bg-opacity-10  | --bg-opacity: 0.1;  |       |
| bg-opacity-20  | --bg-opacity: 0.2;  |       |
| bg-opacity-25  | --bg-opacity: 0.25; |       |
| bg-opacity-30  | --bg-opacity: 0.3;  |       |
| bg-opacity-40  | --bg-opacity: 0.4;  |       |
| bg-opacity-50  | --bg-opacity: 0.5;  |       |
| bg-opacity-60  | --bg-opacity: 0.6;  |       |
| bg-opacity-70  | --bg-opacity: 0.7;  |       |
| bg-opacity-75  | --bg-opacity: 0.75; |       |
| bg-opacity-80  | --bg-opacity: 0.8;  |       |
| bg-opacity-90  | --bg-opacity: 0.9;  |       |
| bg-opacity-95  | --bg-opacity: 0.95; |       |
| bg-opacity-100 | --bg-opacity: 1;    |       |



### Background Origin
Utilities for controlling how an element's background is positioned relative to borders, padding, and content.

| Tailwind          | Description                     | Other |
| ----------------- | ------------------------------- | ----- |
| bg-origin-border  | background-origin: border-box;  |       |
| bg-origin-padding | background-origin: padding-box; |       |
| bg-origin-content | background-origin: content-box; |       |



### Background Position
Sets position of a background image.

| Tailwind        | Description                        | Other |
| --------------- | ---------------------------------- | ----- |
| bg-bottom       | background-position: bottom;       |       |
| bg-center       | background-position: center;       |       |
| bg-left         | background-position: left;         |       |
| bg-left-bottom  | background-position: left bottom;  |       |
| bg-left-top     | background-position: left top;     |       |
| bg-right        | background-position: right;        |       |
| bg-right-bottom | background-position: right bottom; |       |
| bg-right-top    | background-position: right top;    |       |
| bg-top          | background-position: top;          |       |




### Background Repeat
Sets repetition of a background image.

| Tailwind        | Description                   | Other |
| --------------- | ----------------------------- | ----- |
| bg-repeat       | background-repeat: repeat;    |       |
| bg-no-repeat    | background-repeat: no-repeat; |       |
| bg-repeat-x     | background-repeat: repeat-x;  |       |
| bg-repeat-y     | background-repeat: repeat-y;  |       |
| bg-repeat-round | background-repeat: round;     |       |
| bg-repeat-space | background-repeat: space;     |       |




## Background Size
Sets background size of a background image.

| Tailwind   | Description               | Other |
| ---------- | ------------------------- | ----- |
| bg-auto    | background-size: auto;    |       |
| bg-cover   | background-size: cover;   |       |
| bg-contain | background-size: contain; |       |




### Background Image
Utilities for controlling an element's background image.

| Tailwind          | Description                                                                                             | Other |
| ----------------- | ------------------------------------------------------------------------------------------------------- | ----- |
| bg-none           | background-image: none;                                                                                 |       |
| bg-gradient-to-t  | background-image:background-image: background-image: linear-gradient(to top, var(--tw-gradient-stops)); |       |
| bg-gradient-to-tr | background-image: background-image: linear-gradient(to top right, var(--tw-gradient-stops));            |       |
| bg-gradient-to-r  | background-image: background-image: linear-gradient(to right, var(--tw-gradient-stops));                |       |
| bg-gradient-to-br | background-image: background-image: linear-gradient(to bottom right, var(--tw-gradient-stops));         |       |
| bg-gradient-to-b  | background-image: background-image: linear-gradient(to bottom, var(--tw-gradient-stops));               |       |
| bg-gradient-to-bl | background-image: background-image: linear-gradient(to bottom left, var(--tw-gradient-stops));          |       |
| bg-gradient-to-l  | background-image: background-image: linear-gradient(to left, var(--tw-gradient-stops));                 |       |
| bg-gradient-to-tl | background-image: background-image: linear-gradient(to top left, var(--tw-gradient-stops));             |       |



### Gradient Color Stops
Utilities for controlling the color stops in background gradients.

| Tailwind         | Description                      | Other |
| ---------------- | -------------------------------- | ----- |
| from-transparent | background-color: transparent;   |       |
| from-current     | background-color: currentColor;  |       |
| from-black       | background-color: `#000000;`     |       |
| from-white       | background-color: `#ffffff;`     |       |
| from-gray-50     | background-color: `#F9FAFB;`     |       |
| from-gray-100    | background-color: `#F3F4F6;`     |       |
| from-gray-200    | background-color: `#E5E7EB;`     |       |
| from-gray-300    | background-color: `#D1D5DB;`     |       |
| from-gray-400    | background-color: `#9CA3AF;`     |       |
| from-gray-500    | background-color: `#6B7280;`     |       |
| from-gray-600    | background-color: `#6B7280;`     |       |
| from-gray-700    | background-color: `#374151;`     |       |
| from-gray-800    | background-color: `#1F2937;`     |       |
| from-gray-900    | background-color: `#111827;`     |       |
| from-red-50      | background-color: `#FEF2F2;`     |       |
| from-red-100     | background-color: `#FEE2E2;`     |       |
| from-red-200     | background-color: `#FECACA;`     |       |
| from-red-300     | background-color: `#FCA5A5;`     |       |
| from-red-400     | background-color: `#F87171;`     |       |
| from-red-500     | background-color: `#EF4444;`     |       |
| from-red-600     | background-color: `#DC2626;`     |       |
| from-red-700     | background-color: `#B91C1C;`     |       |
| from-red-800     | background-color: `#991B1B;`     |       |
| from-red-900     | background-color: `#7F1D1D;`     |       |
| from-yellow-50   | background-color: `#FFFBEB;`     |       |
| from-yellow-100  | background-color: `#FEF3C7;`     |       |
| from-yellow-200  | background-color: `#FDE68A;`     |       |
| from-yellow-300  | background-color: `#FCD34D;`     |       |
| from-yellow-400  | background-color: `#FBBF24;`     |       |
| from-yellow-500  | background-color: `#F59E0B;`     |       |
| from-yellow-600  | background-color: `#D97706;`     |       |
| from-yellow-700  | background-color: `#B45309;`     |       |
| from-yellow-800  | background-color: `#92400E;`     |       |
| from-yellow-900  | background-color: `#78350F;`     |       |
| from-green-50    | background-color: `#ECFDF5;`     |       |
| from-green-100   | background-color: `#D1FAE5;`     |       |
| from-green-200   | background-color: `#A7F3D0;`     |       |
| from-green-300   | background-color: `#6EE7B7;`     |       |
| from-green-400   | background-color: `#34D399;`     |       |
| from-green-500   | background-color: `#10B981;`     |       |
| from-green-600   | background-color: `#059669;`     |       |
| from-green-700   | background-color: `#047857;`     |       |
| from-green-800   | background-color: `#065F46;`     |       |
| from-green-900   | background-color: `#064E3B;`     |       |
| from-blue-50     | background-color: `#EFF6FF;`     |       |
| from-blue-100    | background-color: `#DBEAFE;`     |       |
| from-blue-200    | background-color: `#BFDBFE;`     |       |
| from-blue-300    | background-color: `#93C5FD;`     |       |
| from-blue-400    | background-color: `#60A5FA;`     |       |
| from-blue-500    | background-color: `#3B82F6;`     |       |
| from-blue-600    | background-color: `#2563EB;`     |       |
| from-blue-700    | background-color: `#1D4ED8;`     |       |
| from-blue-800    | background-color: `#1E40AF;`     |       |
| from-blue-900    | background-color: `#1E3A8A;`     |       |
| from-indigo-50   | background-color: `#EEF2FF;`     |       |
| from-indigo-100  | background-color: `#E0E7FF;`     |       |
| from-indigo-200  | background-color: `#C7D2FE;`     |       |
| from-indigo-300  | background-color: `#A5B4FC;`     |       |
| from-indigo-400  | background-color: `#818CF8;`     |       |
| from-indigo-500  | background-color: `#6366F1;`     |       |
| from-indigo-600  | background-color: `#4F46E5;`     |       |
| from-indigo-700  | background-color: `#4338CA;`     |       |
| from-indigo-800  | background-color: `#3730A3;`     |       |
| from-indigo-900  | background-color: `#312E81;`     |       |
| from-purple-50   | background-color: `#F5F3FF;`     |       |
| from-purple-100  | background-color: `#EDE9FE;`     |       |
| from-purple-200  | background-color: `#DDD6FE;`     |       |
| from-purple-300  | background-color: `#C4B5FD;`     |       |
| from-purple-400  | background-color: `#A78BFA;`     |       |
| from-purple-500  | background-color: `#8B5CF6;`     |       |
| from-purple-600  | background-color: `#7C3AED;`     |       |
| from-purple-700  | background-color: `#6D28D9;`     |       |
| from-purple-800  | background-color: `#5B21B6;`     |       |
| from-purple-900  | background-color: `#4C1D95;`     |       |
| from-pink-50     | background-color: `#FDF2F8;`     |       |
| from-pink-100    | background-color: `#FCE7F3;`     |       |
| from-pink-200    | background-color: `#FBCFE8;`     |       |
| from-pink-300    | background-color: `#F9A8D4;`     |       |
| from-pink-400    | background-color: `#F472B6;`     |       |
| from-pink-500    | background-color: `#EC4899;`     |       |
| from-pink-600    | background-color: `#DB2777;`     |       |
| from-pink-700    | background-color: `#BE185D;`     |       |
| from-pink-800    | background-color: `#9D174D;`     |       |
| from-pink-900    | background-color: `#831843;`     |       |
| via-transparent  | background-color: transparent;`  |       |
| via-current      | background-color: currentColor;` |       |
| via-black        | background-color: `#000000;`     |       |
| via-white        | background-color: `#ffffff;`     |       |
| via-gray-50      | background-color: `#F9FAFB;`     |       |
| via-gray-100     | background-color: `#F3F4F6;`     |       |
| via-gray-200     | background-color: `#E5E7EB;`     |       |
| via-gray-300     | background-color: `#D1D5DB;`     |       |
| via-gray-400     | background-color: `#9CA3AF;`     |       |
| via-gray-500     | background-color: `#6B7280;`     |       |
| via-gray-600     | background-color: `#6B7280;`     |       |
| via-gray-700     | background-color: `#374151;`     |       |
| via-gray-800     | background-color: `#1F2937;`     |       |
| via-gray-900     | background-color: `#111827;`     |       |
| via-red-50       | background-color: `#FEF2F2;`     |       |
| via-red-100      | background-color: `#FEE2E2;`     |       |
| via-red-200      | background-color: `#FECACA;`     |       |
| via-red-300      | background-color: `#FCA5A5;`     |       |
| via-red-400      | background-color: `#F87171;`     |       |
| via-red-500      | background-color: `#EF4444;`     |       |
| via-red-600      | background-color: `#DC2626;`     |       |
| via-red-700      | background-color: `#B91C1C;`     |       |
| via-red-800      | background-color: `#991B1B;`     |       |
| via-red-900      | background-color: `#7F1D1D;`     |       |
| via-yellow-50    | background-color: `#FFFBEB;`     |       |
| via-yellow-100   | background-color: `#FEF3C7;`     |       |
| via-yellow-200   | background-color: `#FDE68A;`     |       |
| via-yellow-300   | background-color: `#FCD34D;`     |       |
| via-yellow-400   | background-color: `#FBBF24;`     |       |
| via-yellow-500   | background-color: `#F59E0B;`     |       |
| via-yellow-600   | background-color: `#D97706;`     |       |
| via-yellow-700   | background-color: `#B45309;`     |       |
| via-yellow-800   | background-color: `#92400E;`     |       |
| via-yellow-900   | background-color: `#78350F;`     |       |
| via-green-50     | background-color: `#ECFDF5;`     |       |
| via-green-100    | background-color: `#D1FAE5;`     |       |
| via-green-200    | background-color: `#A7F3D0;`     |       |
| via-green-300    | background-color: `#6EE7B7;`     |       |
| via-green-400    | background-color: `#34D399;`     |       |
| via-green-500    | background-color: `#10B981;`     |       |
| via-green-600    | background-color: `#059669;`     |       |
| via-green-700    | background-color: `#047857;`     |       |
| via-green-800    | background-color: `#065F46;`     |       |
| via-green-900    | background-color: `#064E3B;`     |       |
| via-blue-50      | background-color: `#EFF6FF;`     |       |
| via-blue-100     | background-color: `#DBEAFE;`     |       |
| via-blue-200     | background-color: `#BFDBFE;`     |       |
| via-blue-300     | background-color: `#93C5FD;`     |       |
| via-blue-400     | background-color: `#60A5FA;`     |       |
| via-blue-500     | background-color: `#3B82F6;`     |       |
| via-blue-600     | background-color: `#2563EB;`     |       |
| via-blue-700     | background-color: `#1D4ED8;`     |       |
| via-blue-800     | background-color: `#1E40AF;`     |       |
| via-blue-900     | background-color: `#1E3A8A;`     |       |
| via-indigo-50    | background-color: `#EEF2FF;`     |       |
| via-indigo-100   | background-color: `#E0E7FF;`     |       |
| via-indigo-200   | background-color: `#C7D2FE;`     |       |
| via-indigo-300   | background-color: `#A5B4FC;`     |       |
| via-indigo-400   | background-color: `#818CF8;`     |       |
| via-indigo-500   | background-color: `#6366F1;`     |       |
| via-indigo-600   | background-color: `#4F46E5;`     |       |
| via-indigo-700   | background-color: `#4338CA;`     |       |
| via-indigo-800   | background-color: `#3730A3;`     |       |
| via-indigo-900   | background-color: `#312E81;`     |       |
| via-purple-50    | background-color: `#F5F3FF;`     |       |
| via-purple-100   | background-color: `#EDE9FE;`     |       |
| via-purple-200   | background-color: `#DDD6FE;`     |       |
| via-purple-300   | background-color: `#C4B5FD;`     |       |
| via-purple-400   | background-color: `#A78BFA;`     |       |
| via-purple-500   | background-color: `#8B5CF6;`     |       |
| via-purple-600   | background-color: `#7C3AED;`     |       |
| via-purple-700   | background-color: `#6D28D9;`     |       |
| via-purple-800   | background-color: `#5B21B6;`     |       |
| via-purple-900   | background-color: `#4C1D95;`     |       |
| via-pink-50      | background-color: `#FDF2F8;`     |       |
| via-pink-100     | background-color: `#FCE7F3;`     |       |
| via-pink-200     | background-color: `#FBCFE8;`     |       |
| via-pink-300     | background-color: `#F9A8D4;`     |       |
| via-pink-400     | background-color: `#F472B6;`     |       |
| via-pink-500     | background-color: `#EC4899;`     |       |
| via-pink-600     | background-color: `#DB2777;`     |       |
| via-pink-700     | background-color: `#BE185D;`     |       |
| via-pink-800     | background-color: `#9D174D;`     |       |
| via-pink-900     | background-color: `#831843;`     |       |
| to-transparent   | background-color: transparent;`  |       |
| to-current       | background-color: currentColor;` |       |
| to-black         | background-color: `#000000;`     |       |
| to-white         | background-color: `#ffffff;`     |       |
| to-gray-50       | background-color: `#F9FAFB;`     |       |
| to-gray-100      | background-color: `#F3F4F6;`     |       |
| to-gray-200      | background-color: `#E5E7EB;`     |       |
| to-gray-300      | background-color: `#D1D5DB;`     |       |
| to-gray-400      | background-color: `#9CA3AF;`     |       |
| to-gray-500      | background-color: `#6B7280;`     |       |
| to-gray-600      | background-color: `#6B7280;`     |       |
| to-gray-700      | background-color: `#374151;`     |       |
| to-gray-800      | background-color: `#1F2937;`     |       |
| to-gray-900      | background-color: `#111827;`     |       |
| to-red-50        | background-color: `#FEF2F2;`     |       |
| to-red-100       | background-color: `#FEE2E2;`     |       |
| to-red-200       | background-color: `#FECACA;`     |       |
| to-red-300       | background-color: `#FCA5A5;`     |       |
| to-red-400       | background-color: `#F87171;`     |       |
| to-red-500       | background-color: `#EF4444;`     |       |
| to-red-600       | background-color: `#DC2626;`     |       |
| to-red-700       | background-color: `#B91C1C;`     |       |
| to-red-800       | background-color: `#991B1B;`     |       |
| to-red-900       | background-color: `#7F1D1D;`     |       |
| to-yellow-50     | background-color: `#FFFBEB;`     |       |
| to-yellow-100    | background-color: `#FEF3C7;`     |       |
| to-yellow-200    | background-color: `#FDE68A;`     |       |
| to-yellow-300    | background-color: `#FCD34D;`     |       |
| to-yellow-400    | background-color: `#FBBF24;`     |       |
| to-yellow-500    | background-color: `#F59E0B;`     |       |
| to-yellow-600    | background-color: `#D97706;`     |       |
| to-yellow-700    | background-color: `#B45309;`     |       |
| to-yellow-800    | background-color: `#92400E;`     |       |
| to-yellow-900    | background-color: `#78350F;`     |       |
| to-green-50      | background-color: `#ECFDF5;`     |       |
| to-green-100     | background-color: `#D1FAE5;`     |       |
| to-green-200     | background-color: `#A7F3D0;`     |       |
| to-green-300     | background-color: `#6EE7B7;`     |       |
| to-green-400     | background-color: `#34D399;`     |       |
| to-green-500     | background-color: `#10B981;`     |       |
| to-green-600     | background-color: `#059669;`     |       |
| to-green-700     | background-color: `#047857;`     |       |
| to-green-800     | background-color: `#065F46;`     |       |
| to-green-900     | background-color: `#064E3B;`     |       |
| to-blue-50       | background-color: `#EFF6FF;`     |       |
| to-blue-100      | background-color: `#DBEAFE;`     |       |
| to-blue-200      | background-color: `#BFDBFE;`     |       |
| to-blue-300      | background-color: `#93C5FD;`     |       |
| to-blue-400      | background-color: `#60A5FA;`     |       |
| to-blue-500      | background-color: `#3B82F6;`     |       |
| to-blue-600      | background-color: `#2563EB;`     |       |
| to-blue-700      | background-color: `#1D4ED8;`     |       |
| to-blue-800      | background-color: `#1E40AF;`     |       |
| to-blue-900      | background-color: `#1E3A8A;`     |       |
| to-indigo-50     | background-color: `#EEF2FF;`     |       |
| to-indigo-100    | background-color: `#E0E7FF;`     |       |
| to-indigo-200    | background-color: `#C7D2FE;`     |       |
| to-indigo-300    | background-color: `#A5B4FC;`     |       |
| to-indigo-400    | background-color: `#818CF8;`     |       |
| to-indigo-500    | background-color: `#6366F1;`     |       |
| to-indigo-600    | background-color: `#4F46E5;`     |       |
| to-indigo-700    | background-color: `#4338CA;`     |       |
| to-indigo-800    | background-color: `#3730A3;`     |       |
| to-indigo-900    | background-color: `#312E81;`     |       |
| to-purple-50     | background-color: `#F5F3FF;`     |       |
| to-purple-100    | background-color: `#EDE9FE;`     |       |
| to-purple-200    | background-color: `#DDD6FE;`     |       |
| to-purple-300    | background-color: `#C4B5FD;`     |       |
| to-purple-400    | background-color: `#A78BFA;`     |       |
| to-purple-500    | background-color: `#8B5CF6;`     |       |
| to-purple-600    | background-color: `#7C3AED;`     |       |
| to-purple-700    | background-color: `#6D28D9;`     |       |
| to-purple-800    | background-color: `#5B21B6;`     |       |
| to-purple-900    | background-color: `#4C1D95;`     |       |
| to-pink-50       | background-color: `#FDF2F8;`     |       |
| to-pink-100      | background-color: `#FCE7F3;`     |       |
| to-pink-200      | background-color: `#FBCFE8;`     |       |
| to-pink-300      | background-color: `#F9A8D4;`     |       |
| to-pink-400      | background-color: `#F472B6;`     |       |
| to-pink-500      | background-color: `#EC4899;`     |       |
| to-pink-600      | background-color: `#DB2777;`     |       |
| to-pink-700      | background-color: `#BE185D;`     |       |
| to-pink-800      | background-color: `#9D174D;`     |       |
| to-pink-900      | background-color: `#831843;`     |       |
































---

## SVG


### Fill
Utilities for styling the fill of SVG elements.

| Tailwind     | Description         | Other |
| ------------ | ------------------- | ----- |
| fill-current | fill: currentColor; |       |




### Stroke
Utilities for styling the stroke of SVG elements.

| Tailwind       | Description           | Other |
| -------------- | --------------------- | ----- |
| stroke-current | stroke: currentColor; |       |



### Stroke Width
Utilities for styling the stroke width of SVG elements.

| Tailwind | Description      | Other |
| -------- | ---------------- | ----- |
| stroke-0 | stroke-width: 0; |       |
| stroke-1 | stroke-width: 1; |       |
| stroke-2 | stroke-width: 2; |       |

---


## Accessibility 


### Screen Readers
Utilities for improving accessibility with screen readers.

| Tailwind    | Description                                                                                                                                            | Other |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----- |
| sr-only     | position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border-width: 0; |       |
| not-sr-only | position: static; width: auto; height: auto; padding: 0; margin: 0; overflow: visible; clip: auto; white-space: normal;                                |       |


---


## Borders 


### Border Radius
Sets border radius.

| Tailwind        | Description                                                                | Other |
| --------------- | -------------------------------------------------------------------------- | ----- |
| rounded-none    | border-radius: 0;                                                          |       |
| rounded-sm      | border-radius: 0.125rem;                                                   | 2px   |
| rounded         | border-radius: 0.25rem;                                                    | 4px   |
| rounded-md      | border-radius: 0.375rem;                                                   | 6px   |
| rounded-lg      | border-radius: 0.5rem;                                                     | 8px   |
| rounded-xl      | border-radius: 0.75rem;                                                    | 10px  |
| rounded-2xl     | border-radius: 1rem;                                                       | 12px  |
| rounded-3xl     | border-radius: 1.5rem;                                                     | 16px  |
| rounded-full    | border-radius: 9999px;                                                     |       |
| rounded-t-none  | border-top-left-radius: 0; border-top-right-radius: 0;                     |       |
| rounded-r-none  | border-top-right-radius: 0; border-bottom-right-radius: 0;                 |       |
| rounded-b-none  | border-bottom-right-radius: 0; border-bottom-left-radius: 0;               |       |
| rounded-l-none  | border-top-left-radius: 0; border-bottom-left-radius: 0;                   |       |
| rounded-t-sm    | border-top-left-radius: 0.125rem; border-top-right-radius: 0.125rem;       | 2px   |
| rounded-r-sm    | border-top-right-radius: 0.125rem; border-bottom-right-radius: 0.125rem;   | 2px   |
| rounded-b-sm    | border-bottom-right-radius: 0.125rem; border-bottom-left-radius: 0.125rem; | 2px   |
| rounded-l-sm    | border-top-left-radius: 0.125rem; border-bottom-left-radius: 0.125rem;     | 2px   |
| rounded-t       | border-top-left-radius: 0.25rem; border-top-right-radius: 0.25rem;         | 4px   |
| rounded-r       | border-top-right-radius: 0.25rem; border-bottom-right-radius: 0.25rem;     | 4px   |
| rounded-b       | border-bottom-right-radius: 0.25rem; border-bottom-left-radius: 0.25rem;   | 4px   |
| rounded-l       | border-top-left-radius: 0.25rem; border-bottom-left-radius: 0.25rem;       | 4px   |
| rounded-t-md    | border-top-left-radius: 0.375rem; border-top-right-radius: 0.375rem;       | 6px   |
| rounded-r-md    | border-top-right-radius: 0.375rem; border-bottom-right-radius: 0.375rem;   | 6px   |
| rounded-b-md    | border-bottom-right-radius: 0.375rem; border-bottom-left-radius: 0.375rem; | 6px   |
| rounded-l-md    | border-top-left-radius: 0.375rem; border-bottom-left-radius: 0.375rem;     | 6px   |
| rounded-t-lg    | border-top-left-radius: 0.5rem; border-top-right-radius: 0.5rem;           | 8px   |
| rounded-r-lg    | border-top-right-radius: 0.5rem; border-bottom-right-radius: 0.5rem;       | 8px   |
| rounded-b-lg    | border-bottom-right-radius: 0.5rem; border-bottom-left-radius: 0.5rem;     | 8px   |
| rounded-l-lg    | border-top-left-radius: 0.5rem; border-bottom-left-radius: 0.5rem;         | 8px   |
| rounded-t-xl    | border-top-left-radius: 0.75rem; border-top-right-radius: 0.75rem;         | 10px  |
| rounded-r-xl    | border-top-right-radius: 0.75rem; border-bottom-right-radius: 0.75rem;     | 10px  |
| rounded-b-xl    | border-bottom-right-radius: 0.75rem; border-bottom-left-radius: 0.75rem;   | 10px  |
| rounded-l-xl    | border-top-left-radius: 0.75rem; border-bottom-left-radius: 0.75rem;       | 10px  |
| rounded-t-2xl   | border-top-left-radius: 1rem; border-top-right-radius: 1rem;               | 12px  |
| rounded-r-2xl   | border-top-right-radius: 1rem; border-bottom-right-radius: 1rem;           | 12px  |
| rounded-b-2xl   | border-bottom-right-radius: 1rem; border-bottom-left-radius: 1rem;         | 12px  |
| rounded-l-2xl   | border-top-left-radius: 1rem; border-bottom-left-radius: 1rem;             | 12px  |
| rounded-t-3xl   | border-top-left-radius: 1.5rem; border-top-right-radius: 1.5rem;           | 16px  |
| rounded-r-3xl   | border-top-right-radius: 1.5rem; border-bottom-right-radius: 1.5rem;       | 16px  |
| rounded-b-3xl   | border-bottom-right-radius: 1.5rem; border-bottom-left-radius: 1.5rem;     | 16px  |
| rounded-l-3xl   | border-top-left-radius: 1.5rem; border-bottom-left-radius: 1.5rem;         | 16px  |
| rounded-t-full  | border-top-left-radius: 9999px; border-top-right-radius: 9999px;           |       |
| rounded-r-full  | border-top-right-radius: 9999px; border-bottom-right-radius: 9999px;       |       |
| rounded-b-full  | border-bottom-right-radius: 9999px; border-bottom-left-radius: 9999px;     |       |
| rounded-l-full  | border-top-left-radius: 9999px; border-bottom-left-radius: 9999px;         |       |
| rounded-tl-none | border-top-left-radius: 0;                                                 |       |
| rounded-tr-none | border-top-right-radius: 0;                                                |       |
| rounded-br-none | border-bottom-right-radius: 0;                                             |       |
| rounded-bl-none | border-bottom-left-radius: 0;                                              |       |
| rounded-tl-sm   | border-top-left-radius: 0.125rem;                                          | 2px   |
| rounded-tr-sm   | border-top-right-radius: 0.125rem;                                         | 2px   |
| rounded-br-sm   | border-bottom-right-radius: 0.125rem;                                      | 2px   |
| rounded-bl-sm   | border-bottom-left-radius: 0.125rem;                                       | 2px   |
| rounded-tl      | border-top-left-radius: 0.25rem;                                           | 4px   |
| rounded-tr      | border-top-right-radius: 0.25rem;                                          | 4px   |
| rounded-br      | border-bottom-right-radius: 0.25rem;                                       | 4px   |
| rounded-bl      | border-bottom-left-radius: 0.25rem;                                        | 4px   |
| rounded-tl-md   | border-top-left-radius: 0.375rem;                                          | 6px   |
| rounded-tr-md   | border-top-right-radius: 0.375rem;                                         | 6px   |
| rounded-br-md   | border-bottom-right-radius: 0.375rem;                                      | 6px   |
| rounded-bl-md   | border-bottom-left-radius: 0.375rem;                                       | 6px   |
| rounded-tl-lg   | border-top-left-radius: 0.5rem;                                            | 8px   |
| rounded-tr-lg   | border-top-right-radius: 0.5rem;                                           | 8px   |
| rounded-br-lg   | border-bottom-right-radius: 0.5rem;                                        | 8px   |
| rounded-bl-lg   | border-bottom-left-radius: 0.5rem;                                         | 8px   |
| rounded-tl-xl   | border-top-left-radius: 0.75rem;                                           | 10px  |
| rounded-tr-xl   | border-top-right-radius: 0.75rem;                                          | 10px  |
| rounded-br-xl   | border-bottom-right-radius: 0.75rem;                                       | 10px  |
| rounded-bl-xl   | border-bottom-left-radius: 0.75rem;                                        | 10px  |
| rounded-tl-2xl  | border-top-left-radius: 1rem;                                              | 12px  |
| rounded-tr-2xl  | border-top-right-radius: 1rem;                                             | 12px  |
| rounded-br-2xl  | border-bottom-right-radius: 1rem;                                          | 12px  |
| rounded-bl-2xl  | border-bottom-left-radius: 1rem;                                           | 12px  |
| rounded-tl-3xl  | border-top-left-radius: 1.5rem;                                            | 16px  |
| rounded-tr-3xl  | border-top-right-radius: 1.5rem;                                           | 16px  |
| rounded-br-3xl  | border-bottom-right-radius: 1.5rem;                                        | 16px  |
| rounded-bl-3xl  | border-bottom-left-radius: 1.5rem;                                         | 16px  |
| rounded-tl-full | border-top-left-radius: 9999px;                                            |       |
| rounded-tr-full | border-top-right-radius: 9999px;                                           |       |
| rounded-br-full | border-bottom-right-radius: 9999px;                                        |       |
| rounded-bl-full | border-bottom-left-radius: 9999px;                                         |       |














### Border Width
Sets width for borders in increments of 1px.

| Tailwind   | Description               | Other |
| ---------- | ------------------------- | ----- |
| border     | border-width: 1px;        |       |
| border-0   | border-width: 0;          |       |
| border-2   | border-width: 2px;        |       |
| border-4   | border-width: 4px;        |       |
| border-8   | border-width: 8px;        |       |
| border-t   | border-top-width: 1px;    |       |
| border-t-0 | border-top-width: 0;      |       |
| border-t-2 | border-top-width: 2px;    |       |
| border-t-4 | border-top-width: 4px;    |       |
| border-t-8 | border-top-width: 8px;    |       |
| border-r   | border-right-width: 1px;  |       |
| border-r-0 | border-right-width: 0;    |       |
| border-r-2 | border-right-width: 2px;  |       |
| border-r-4 | border-right-width: 4px;  |       |
| border-r-8 | border-right-width: 8px;  |       |
| border-b   | border-bottom-width: 1px; |       |
| border-b-0 | border-bottom-width: 0;   |       |
| border-b-2 | border-bottom-width: 2px; |       |
| border-b-4 | border-bottom-width: 4px; |       |
| border-b-8 | border-bottom-width: 8px; |       |
| border-l   | border-left-width: 1px;   |       |
| border-l-0 | border-left-width: 0;     |       |
| border-l-2 | border-left-width: 2px;   |       |
| border-l-4 | border-left-width: 4px;   |       |
| border-l-8 | border-left-width: 8px;   |       |



### Border Color
Sets color for borders.

| Tailwind           | Description                  | Other |
| ------------------ | ---------------------------- | ----- |
| border-transparent | border-color: transparent;   |       |
| border-current     | border-color: currentColor;  |       |
| border-black       | border-color: `#000000;`     |       |
| border-white       | border-color: `#ffffff;`     |       |
| border-gray-50     | border-color: `#F9FAFB;`     |       |
| border-gray-100    | border-color: `#F3F4F6;`     |       |
| border-gray-200    | border-color: `#E5E7EB;`     |       |
| border-gray-300    | border-color: `#D1D5DB;`     |       |
| border-gray-400    | border-color: `#9CA3AF;`     |       |
| border-gray-500    | border-color: `#6B7280;`     |       |
| border-gray-600    | border-color: `#4B5563;`     |       |
| border-gray-700    | border-color: `#374151;`     |       |
| border-gray-800    | border-color: `#1F2937;`     |       |
| border-gray-900    | border-color: `#111827;`     |       |
| border-red-50      | border-color: `#FEF2F2;`     |       |
| border-red-100     | border-color: `#FEE2E2;`     |       |
| border-red-200     | border-color: `#FECACA;`     |       |
| border-red-300     | border-color: `#FCA5A5;`     |       |
| border-red-400     | border-color: `#F87171;`     |       |
| border-red-500     | border-color: `#EF4444;`     |       |
| border-red-600     | border-color: `#DC2626;`     |       |
| border-red-700     | border-color: `#B91C1C;`     |       |
| border-red-800     | border-color: `#991B1B;`     |       |
| border-red-900     | border-color: `#7F1D1D;`     |       |
| border-yellow-50   | border-color: `#FFFBEB;`     |       |
| border-yellow-100  | border-color: `#FEF3C7;`     |       |
| border-yellow-200  | border-color: `#FDE68A;`     |       |
| border-yellow-300  | border-color: `#FCD34D;`     |       |
| border-yellow-400  | border-color: `#FBBF24;`     |       |
| border-yellow-500  | border-color: `#F59E0B;`     |       |
| border-yellow-600  | border-color: `#D97706;`     |       |
| border-yellow-700  | border-color: `#B45309;`     |       |
| border-yellow-800  | border-color: `#92400E;`     |       |
| border-yellow-900  | border-color: `#78350F;`     |       |
| border-green-50    | border-color: `#ECFDF5;`     |       |
| border-green-100   | border-color: `#D1FAE5;`     |       |
| border-green-200   | border-color: `#A7F3D0;`     |       |
| border-green-300   | border-color: `#6EE7B7;`     |       |
| border-green-400   | border-color: `#34D399;`     |       |
| border-green-500   | border-color: `#10B981;`     |       |
| border-green-600   | border-color: `#059669;`     |       |
| border-green-700   | border-color: `#047857;`     |       |
| border-green-800   | border-color: `#065F46;`     |       |
| border-green-900   | border-color: `#064E3B;`     |       |
| border-blue-50     | border-color: `#EFF6FF;`     |       |
| border-blue-100    | border-color: `#DBEAFE;`     |       |
| border-blue-200    | border-color: `#BFDBFE;`     |       |
| border-blue-300    | border-color: `#93C5FD;`     |       |
| border-blue-400    | border-color: `#60A5FA;`     |       |
| border-blue-500    | border-color: `#3B82F6;`     |       |
| border-blue-600    | border-color: `#2563EB;`     |       |
| border-blue-700    | border-color: `#1D4ED8;`     |       |
| border-blue-800    | border-color: `#1E40AF;`     |       |
| border-blue-900    | border-color: `#1E3A8A;`     |       |
| border-indigo-50   | border-color: `#EEF2FF;`     |       |
| border-indigo-100  | border-color: `#E0E7FF;`     |       |
| border-indigo-200  | border-color: `#C7D2FE;`     |       |
| border-indigo-300  | border-color: `#A5B4FC;`     |       |
| border-indigo-400  | border-color: `#818CF8;`     |       |
| border-indigo-500  | border-color: `#6366F1;`     |       |
| border-indigo-600  | border-color: `#4F46E5;`     |       |
| border-indigo-700  | border-color: `#4338CA;`     |       |
| border-indigo-800  | border-color: `#3730A3;`     |       |
| border-indigo-900  | border-color: `#312E81;`     |       |
| border-purple-50   | border-color: `#F5F3FF;`     |       |
| border-purple-100  | border-color: `#EDE9FE;`     |       |
| border-purple-200  | border-color: `#DDD6FE;`     |       |
| border-purple-300  | border-color: `#C4B5FD;`     |       |
| border-purple-400  | border-color: `#A78BFA;`     |       |
| border-purple-500  | border-color: `#8B5CF6;`     |       |
| border-purple-600  | border-color: `#7C3AED;`     |       |
| border-purple-700  | border-color: `#6D28D9;`     |       |
| border-purple-800  | border-color: `#5B21B6;`     |       |
| border-purple-900  | border-color: `#4C1D95;`     |       |
| border-pink-50     | border-color: `#FDF2F8;`     |       |
| border-pink-100    | border-color: `#FCE7F3;`     |       |
| border-pink-200    | border-color: `#FBCFE8;`     |       |
| border-pink-300    | border-color: `#F9A8D4;`     |       |
| border-pink-400    | border-color: `#F472B6;`     |       |
| border-pink-500    | border-color: `#EC4899;`     |       |
| border-pink-600    | border-color: `#DB2777;`     |       |
| border-pink-700    | border-color: `#BE185D;`     |       |
| border-pink-800    | border-color: `#9D174D;`     |       |
| border-pink-900    | border-color: `#831843;`     |       |











### Border Opacity
Sets opacity for borders.

| Tailwind           | Description           | Other |
| ------------------ | --------------------- | ----- |
| border-opacity-0   | border-opacity: 0;    |       |
| border-opacity-5   | border-opacity: 0.05; |       |
| border-opacity-10  | border-opacity: 0.1;  |       |
| border-opacity-20  | border-opacity: 0.2;  |       |
| border-opacity-25  | border-opacity: 0.25; |       |
| border-opacity-30  | border-opacity: 0.3;  |       |
| border-opacity-40  | border-opacity: 0.4;  |       |
| border-opacity-50  | border-opacity: 0.5;  |       |
| border-opacity-60  | border-opacity: 0.6;  |       |
| border-opacity-70  | border-opacity: 0.7;  |       |
| border-opacity-75  | border-opacity: 0.75; |       |
| border-opacity-80  | border-opacity: 0.8;  |       |
| border-opacity-90  | border-opacity: 0.9;  |       |
| border-opacity-100 | border-opacity: 1;    |       |



### Border Style
Sets style for borders.

| Tailwind      | Description           | Other |
| ------------- | --------------------- | ----- |
| border-solid  | border-style: solid;  |       |
| border-dashed | border-style: dashed; |       |
| border-dotted | border-style: dotted; |       |
| border-double | border-style: double; |       |
| border-hidden | border-style: hidden; |       |
| border-none   | border-style: none;   |       |




### Divide Width
Controls the border width between elements.

| Tailwind         | Description             | Other |
| ---------------- | ----------------------- | ----- |
| divide-x-0       | border-left-width: 0;   |       |
| divide-x-2       | border-left-width: 2px; |       |
| divide-x-4       | border-left-width: 4px; |       |
| divide-x-8       | border-left-width: 8px; |       |
| divide-x         | border-left-width: 1px; |       |
| divide-y-0       | border-top-width: 0;    |       |
| divide-y-2       | border-top-width: 2px;  |       |
| divide-y-4       | border-top-width: 4px;  |       |
| divide-y-8       | border-top-width: 8px;  |       |
| divide-y         | border-top-width: 1px;  |       |
| divide-x-reverse | --divide-x-reverse: 1   |       |
| divide-y-reverse | --divide-y-reverse: 1   |       |



### Divide Color
Controls the border color between elements.

| Tailwind           | Description                  | Other |
| ------------------ | ---------------------------- | ----- |
| divide-transparent | border-color: transparent;   |       |
| divide-current     | border-color: currentColor;  |       |
| divide-black       | border-color: `#000000;`     |       |
| divide-white       | border-color: `#ffffff;`     |       |
| divide-gray-50     | border-color: `#F9FAFB;`     |       |
| divide-gray-100    | border-color: `#F3F4F6;`     |       |
| divide-gray-200    | border-color: `#E5E7EB;`     |       |
| divide-gray-300    | border-color: `#D1D5DB;`     |       |
| divide-gray-400    | border-color: `#9CA3AF;`     |       |
| divide-gray-500    | border-color: `#6B7280;`     |       |
| divide-gray-600    | border-color: `#4B5563;`     |       |
| divide-gray-700    | border-color: `#374151;`     |       |
| divide-gray-800    | border-color: `#1F2937;`     |       |
| divide-gray-900    | border-color: `#111827;`     |       |
| divide-red-50      | border-color: `#FEF2F2;`     |       |
| divide-red-100     | border-color: `#FEE2E2;`     |       |
| divide-red-200     | border-color: `#FECACA;`     |       |
| divide-red-300     | border-color: `#FCA5A5;`     |       |
| divide-red-400     | border-color: `#F87171;`     |       |
| divide-red-500     | border-color: `#EF4444;`     |       |
| divide-red-600     | border-color: `#DC2626;`     |       |
| divide-red-700     | border-color: `#B91C1C;`     |       |
| divide-red-800     | border-color: `#991B1B;`     |       |
| divide-red-900     | border-color: `#7F1D1D;`     |       |
| divide-yellow-50   | border-color: `#FFFBEB;`     |       |
| divide-yellow-100  | border-color: `#FEF3C7;`     |       |
| divide-yellow-200  | border-color: `#FDE68A;`     |       |
| divide-yellow-300  | border-color: `#FCD34D;`     |       |
| divide-yellow-400  | border-color: `#FBBF24;`     |       |
| divide-yellow-500  | border-color: `#F59E0B;`     |       |
| divide-yellow-600  | border-color: `#D97706;`     |       |
| divide-yellow-700  | border-color: `#B45309;`     |       |
| divide-yellow-800  | border-color: `#92400E;`     |       |
| divide-yellow-900  | border-color: `#78350F;`     |       |
| divide-green-50    | border-color: `#ECFDF5;`     |       |
| divide-green-100   | border-color: `#D1FAE5;`     |       |
| divide-green-200   | border-color: `#A7F3D0;`     |       |
| divide-green-300   | border-color: `#6EE7B7;`     |       |
| divide-green-400   | border-color: `#34D399;`     |       |
| divide-green-500   | border-color: `#10B981;`     |       |
| divide-green-600   | border-color: `#059669;`     |       |
| divide-green-700   | border-color: `#047857;`     |       |
| divide-green-800   | border-color: `#065F46;`     |       |
| divide-green-900   | border-color: `#064E3B;`     |       |
| divide-blue-50     | border-color: `#EFF6FF;`     |       |
| divide-blue-100    | border-color: `#DBEAFE;`     |       |
| divide-blue-200    | border-color: `#BFDBFE;`     |       |
| divide-blue-300    | border-color: `#93C5FD;`     |       |
| divide-blue-400    | border-color: `#60A5FA;`     |       |
| divide-blue-500    | border-color: `#3B82F6;`     |       |
| divide-blue-600    | border-color: `#2563EB;`     |       |
| divide-blue-700    | border-color: `#1D4ED8;`     |       |
| divide-blue-800    | border-color: `#1E40AF;`     |       |
| divide-blue-900    | border-color: `#1E3A8A;`     |       |
| divide-indigo-50   | border-color: `#EEF2FF;`     |       |
| divide-indigo-100  | border-color: `#E0E7FF;`     |       |
| divide-indigo-200  | border-color: `#C7D2FE;`     |       |
| divide-indigo-300  | border-color: `#A5B4FC;`     |       |
| divide-indigo-400  | border-color: `#818CF8;`     |       |
| divide-indigo-500  | border-color: `#6366F1;`     |       |
| divide-indigo-600  | border-color: `#4F46E5;`     |       |
| divide-indigo-700  | border-color: `#4338CA;`     |       |
| divide-indigo-800  | border-color: `#3730A3;`     |       |
| divide-indigo-900  | border-color: `#312E81;`     |       |
| divide-purple-50   | border-color: `#F5F3FF;`     |       |
| divide-purple-100  | border-color: `#EDE9FE;`     |       |
| divide-purple-200  | border-color: `#DDD6FE;`     |       |
| divide-purple-300  | border-color: `#C4B5FD;`     |       |
| divide-purple-400  | border-color: `#A78BFA;`     |       |
| divide-purple-500  | border-color: `#8B5CF6;`     |       |
| divide-purple-600  | border-color: `#7C3AED;`     |       |
| divide-purple-700  | border-color: `#6D28D9;`     |       |
| divide-purple-800  | border-color: `#5B21B6;`     |       |
| divide-purple-900  | border-color: `#4C1D95;`     |       |
| divide-pink-50     | border-color: `#FDF2F8;`     |       |
| divide-pink-100    | border-color: `#FCE7F3;`     |       |
| divide-pink-200    | border-color: `#FBCFE8;`     |       |
| divide-pink-300    | border-color: `#F9A8D4;`     |       |
| divide-pink-400    | border-color: `#F472B6;`     |       |
| divide-pink-500    | border-color: `#EC4899;`     |       |
| divide-pink-600    | border-color: `#DB2777;`     |       |
| divide-pink-700    | border-color: `#BE185D;`     |       |
| divide-pink-800    | border-color: `#9D174D;`     |       |
| divide-pink-900    | border-color: `#831843;`     |       |
















### Divide Opacity
Controls the border opacity between elements.

| Tailwind           | Description             | Other |
| ------------------ | ----------------------- | ----- |
| divide-opacity-0   | --divide-opacity: 0;    |       |
| divide-opacity-5   | --divide-opacity: 0.05; |       |
| divide-opacity-10  | --divide-opacity: 0.1;  |       |
| divide-opacity-20  | --divide-opacity: 0.2;  |       |
| divide-opacity-25  | --divide-opacity: 0.25; |       |
| divide-opacity-30  | --divide-opacity: 0.3;  |       |
| divide-opacity-40  | --divide-opacity: 0.4;  |       |
| divide-opacity-50  | --divide-opacity: 0.5;  |       |
| divide-opacity-60  | --divide-opacity: 0.6;  |       |
| divide-opacity-70  | --divide-opacity: 0.7;  |       |
| divide-opacity-75  | --divide-opacity: 0.75; |       |
| divide-opacity-80  | --divide-opacity: 0.8;  |       |
| divide-opacity-90  | --divide-opacity: 0.9;  |       |
| divide-opacity-100 | --divide-opacity: 1;    |       |



### Divide Style
Sets style for divides.

| Tailwind      | Description           | Other |
| ------------- | --------------------- | ----- |
| divide-solid  | border-style: solid;  |       |
| divide-dashed | border-style: dashed; |       |
| divide-dotted | border-style: dotted; |       |
| divide-double | border-style: double; |       |
| divide-none   | border-style: none;   |       |



### Outline Width
Utilities for controlling the width of an element's outline.

| Tailwind  | Description         | Other |
| --------- | ------------------- | ----- |
| outline-0 | outline-width: 0px; |       |
| outline-1 | outline-width: 1px; |       |
| outline-2 | outline-width: 2px; |       |
| outline-4 | outline-width: 4px; |       |
| outline-8 | outline-width: 8px; |       |



### Outline Style
Utilities for controlling the style of an element's outline.

| Tailwind       | Description            | Other |
| -------------- | ---------------------- | ----- |
| outline-solid  | outline-style: solid;  |       |
| outline-dashed | outline-style: dashed; |       |
| outline-dotted | outline-style: dotted; |       |
| outline-double | outline-style: double; |       |
| outline-hidden | outline-style: hidden; |       |
| outline-none   | outline-style: none;   |       |




### Outline Offset
Utilities for controlling the Offset of an element's outline.

| Tailwind         | Description          | Other |
| ---------------- | -------------------- | ----- |
| outline-offset-0 | outline-offset: 0px; |       |
| outline-offset-1 | outline-offset: 1px; |       |
| outline-offset-2 | outline-offset: 2px; |       |
| outline-offset-4 | outline-offset: 4px; |       |
| outline-offset-8 | outline-offset: 8px; |       |



### Ring Width
Utilities for creating outline rings with box-shadows.

| Tailwind   | Description                                                                                          | Other |
| ---------- | ---------------------------------------------------------------------------------------------------- | ----- |
| ring-0     | box-shadow: var(--tw-ring-inset) 0 0 0 calc(0px + var(--tw-ring-offset-width)) var(--tw-ring-color); |       |
| ring-1     | box-shadow: var(--tw-ring-inset) 0 0 0 calc(1px + var(--tw-ring-offset-width)) var(--tw-ring-color); |       |
| ring-2     | box-shadow: var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color); |       |
| ring-4     | box-shadow: var(--tw-ring-inset) 0 0 0 calc(4px + var(--tw-ring-offset-width)) var(--tw-ring-color); |       |
| ring-8     | box-shadow: var(--tw-ring-inset) 0 0 0 calc(8px + var(--tw-ring-offset-width)) var(--tw-ring-color); |       |
| ring       | box-shadow: var(--tw-ring-inset) 0 0 0 calc(3px + var(--tw-ring-offset-width)) var(--tw-ring-color); |       |
| ring-inset | --tw-ring-inset: inset;                                                                              |       |



### Ring Color
Utilities for setting the color of outline rings.

| Tailwind         | Description                  | Other |
| ---------------- | ---------------------------- | ----- |
| ring-transparent | --ring-color: transparent;   |       |
| ring-current     | --ring-color: currentColor;  |       |
| ring-black       | --ring-color: `#000000;`     |       |
| ring-white       | --ring-color: `#ffffff;`     |       |
| ring-gray-50     | --ring-color: `#F9FAFB;`     |       |
| ring-gray-100    | --ring-color: `#F3F4F6;`     |       |
| ring-gray-200    | --ring-color: `#E5E7EB;`     |       |
| ring-gray-300    | --ring-color: `#D1D5DB;`     |       |
| ring-gray-400    | --ring-color: `#9CA3AF;`     |       |
| ring-gray-500    | --ring-color: `#6B7280;`     |       |
| ring-gray-600    | --ring-color: `#4B5563;`     |       |
| ring-gray-700    | --ring-color: `#374151;`     |       |
| ring-gray-800    | --ring-color: `#1F2937;`     |       |
| ring-gray-900    | --ring-color: `#111827;`     |       |
| ring-red-50      | --ring-color: `#FEF2F2;`     |       |
| ring-red-100     | --ring-color: `#FEE2E2;`     |       |
| ring-red-200     | --ring-color: `#FECACA;`     |       |
| ring-red-300     | --ring-color: `#FCA5A5;`     |       |
| ring-red-400     | --ring-color: `#F87171;`     |       |
| ring-red-500     | --ring-color: `#EF4444;`     |       |
| ring-red-600     | --ring-color: `#DC2626;`     |       |
| ring-red-700     | --ring-color: `#B91C1C;`     |       |
| ring-red-800     | --ring-color: `#991B1B;`     |       |
| ring-red-900     | --ring-color: `#7F1D1D;`     |       |
| ring-yellow-50   | --ring-color: `#FFFBEB;`     |       |
| ring-yellow-100  | --ring-color: `#FEF3C7;`     |       |
| ring-yellow-200  | --ring-color: `#FDE68A;`     |       |
| ring-yellow-300  | --ring-color: `#FCD34D;`     |       |
| ring-yellow-400  | --ring-color: `#FBBF24;`     |       |
| ring-yellow-500  | --ring-color: `#F59E0B;`     |       |
| ring-yellow-600  | --ring-color: `#D97706;`     |       |
| ring-yellow-700  | --ring-color: `#B45309;`     |       |
| ring-yellow-800  | --ring-color: `#92400E;`     |       |
| ring-yellow-900  | --ring-color: `#78350F;`     |       |
| ring-green-50    | --ring-color: `#ECFDF5;`     |       |
| ring-green-100   | --ring-color: `#D1FAE5;`     |       |
| ring-green-200   | --ring-color: `#A7F3D0;`     |       |
| ring-green-300   | --ring-color: `#6EE7B7;`     |       |
| ring-green-400   | --ring-color: `#34D399;`     |       |
| ring-green-500   | --ring-color: `#10B981;`     |       |
| ring-green-600   | --ring-color: `#059669;`     |       |
| ring-green-700   | --ring-color: `#047857;`     |       |
| ring-green-800   | --ring-color: `#065F46;`     |       |
| ring-green-900   | --ring-color: `#064E3B;`     |       |
| ring-blue-50     | --ring-color: `#EFF6FF;`     |       |
| ring-blue-100    | --ring-color: `#DBEAFE;`     |       |
| ring-blue-200    | --ring-color: `#BFDBFE;`     |       |
| ring-blue-300    | --ring-color: `#93C5FD;`     |       |
| ring-blue-400    | --ring-color: `#60A5FA;`     |       |
| ring-blue-500    | --ring-color: `#3B82F6;`     |       |
| ring-blue-600    | --ring-color: `#2563EB;`     |       |
| ring-blue-700    | --ring-color: `#1D4ED8;`     |       |
| ring-blue-800    | --ring-color: `#1E40AF;`     |       |
| ring-blue-900    | --ring-color: `#1E3A8A;`     |       |
| ring-indigo-50   | --ring-color: `#EEF2FF;`     |       |
| ring-indigo-100  | --ring-color: `#E0E7FF;`     |       |
| ring-indigo-200  | --ring-color: `#C7D2FE;`     |       |
| ring-indigo-300  | --ring-color: `#A5B4FC;`     |       |
| ring-indigo-400  | --ring-color: `#818CF8;`     |       |
| ring-indigo-500  | --ring-color: `#6366F1;`     |       |
| ring-indigo-600  | --ring-color: `#4F46E5;`     |       |
| ring-indigo-700  | --ring-color: `#4338CA;`     |       |
| ring-indigo-800  | --ring-color: `#3730A3;`     |       |
| ring-indigo-900  | --ring-color: `#312E81;`     |       |
| ring-purple-50   | --ring-color: `#F5F3FF;`     |       |
| ring-purple-100  | --ring-color: `#EDE9FE;`     |       |
| ring-purple-200  | --ring-color: `#DDD6FE;`     |       |
| ring-purple-300  | --ring-color: `#C4B5FD;`     |       |
| ring-purple-400  | --ring-color: `#A78BFA;`     |       |
| ring-purple-500  | --ring-color: `#8B5CF6;`     |       |
| ring-purple-600  | --ring-color: `#7C3AED;`     |       |
| ring-purple-700  | --ring-color: `#6D28D9;`     |       |
| ring-purple-800  | --ring-color: `#5B21B6;`     |       |
| ring-purple-900  | --ring-color: `#4C1D95;`     |       |
| ring-pink-50     | --ring-color: `#FDF2F8;`     |       |
| ring-pink-100    | --ring-color: `#FCE7F3;`     |       |
| ring-pink-200    | --ring-color: `#FBCFE8;`     |       |
| ring-pink-300    | --ring-color: `#F9A8D4;`     |       |
| ring-pink-400    | --ring-color: `#F472B6;`     |       |
| ring-pink-500    | --ring-color: `#EC4899;`     |       |
| ring-pink-600    | --ring-color: `#DB2777;`     |       |
| ring-pink-700    | --ring-color: `#BE185D;`     |       |
| ring-pink-800    | --ring-color: `#9D174D;`     |       |
| ring-pink-900    | --ring-color: `#831843;`     |       |















### Ring Opacity
Utilities for setting the opacity of outline rings.

| Tailwind         | Description           | Other |
| ---------------- | --------------------- | ----- |
| ring-opacity-0   | --ring-opacity: 0;    |       |
| ring-opacity-5   | --ring-opacity: 0.05; |       |
| ring-opacity-10  | --ring-opacity: 0.1;  |       |
| ring-opacity-20  | --ring-opacity: 0.2;  |       |
| ring-opacity-25  | --ring-opacity: 0.25; |       |
| ring-opacity-30  | --ring-opacity: 0.3;  |       |
| ring-opacity-40  | --ring-opacity: 0.4;  |       |
| ring-opacity-50  | --ring-opacity: 0.5;  |       |
| ring-opacity-60  | --ring-opacity: 0.6;  |       |
| ring-opacity-70  | --ring-opacity: 0.7;  |       |
| ring-opacity-75  | --ring-opacity: 0.75; |       |
| ring-opacity-80  | --ring-opacity: 0.8;  |       |
| ring-opacity-90  | --ring-opacity: 0.9;  |       |
| ring-opacity-100 | --ring-opacity: 1;    |       |



### Ring Offset Width
Utilities for simulating an offset when adding outline rings.

| Tailwind      | Description                                                                                                        | Other |
| ------------- | ------------------------------------------------------------------------------------------------------------------ | ----- |
| ring-offset-0 | --ring-offset-width: 0px; box-shadow: 0 0 0 var(--ring-offset-width) var(--ring-offset-color), var(--ring-shadow); |       |
| ring-offset-1 | --ring-offset-width: 1px; box-shadow: 0 0 0 var(--ring-offset-width) var(--ring-offset-color), var(--ring-shadow); |       |
| ring-offset-2 | --ring-offset-width: 2px; box-shadow: 0 0 0 var(--ring-offset-width) var(--ring-offset-color), var(--ring-shadow); |       |
| ring-offset-4 | --ring-offset-width: 4px; box-shadow: 0 0 0 var(--ring-offset-width) var(--ring-offset-color), var(--ring-shadow); |       |
| ring-offset-8 | --ring-offset-width: 8px; box-shadow: 0 0 0 var(--ring-offset-width) var(--ring-offset-color), var(--ring-shadow); |       |



### Ring Offset Color
Utilities for setting the color of outline rings offset.

| Tailwind                | Description                         | Other |
| ----------------------- | ----------------------------------- | ----- |
| ring-offset-transparent | --ring-offset-color: transparent;   |       |
| ring-offset-current     | --ring-offset-color: currentColor;  |       |
| ring-offset-black       | --ring-offset-color: `#000000;`     |       |
| ring-offset-white       | --ring-offset-color: `#ffffff;`     |       |
| ring-offset-gray-50     | --ring-offset-color: `#F9FAFB;`     |       |
| ring-offset-gray-100    | --ring-offset-color: `#F3F4F6;`     |       |
| ring-offset-gray-200    | --ring-offset-color: `#E5E7EB;`     |       |
| ring-offset-gray-300    | --ring-offset-color: `#D1D5DB;`     |       |
| ring-offset-gray-400    | --ring-offset-color: `#9CA3AF;`     |       |
| ring-offset-gray-500    | --ring-offset-color: `#6B7280;`     |       |
| ring-offset-gray-600    | --ring-offset-color: `#4B5563;`     |       |
| ring-offset-gray-700    | --ring-offset-color: `#374151;`     |       |
| ring-offset-gray-800    | --ring-offset-color: `#1F2937;`     |       |
| ring-offset-gray-900    | --ring-offset-color: `#111827;`     |       |
| ring-offset-red-50      | --ring-offset-color: `#FEF2F2;`     |       |
| ring-offset-red-100     | --ring-offset-color: `#FEE2E2;`     |       |
| ring-offset-red-200     | --ring-offset-color: `#FECACA;`     |       |
| ring-offset-red-300     | --ring-offset-color: `#FCA5A5;`     |       |
| ring-offset-red-400     | --ring-offset-color: `#F87171;`     |       |
| ring-offset-red-500     | --ring-offset-color: `#EF4444;`     |       |
| ring-offset-red-600     | --ring-offset-color: `#DC2626;`     |       |
| ring-offset-red-700     | --ring-offset-color: `#B91C1C;`     |       |
| ring-offset-red-800     | --ring-offset-color: `#991B1B;`     |       |
| ring-offset-red-900     | --ring-offset-color: `#7F1D1D;`     |       |
| ring-offset-yellow-50   | --ring-offset-color: `#FFFBEB;`     |       |
| ring-offset-yellow-100  | --ring-offset-color: `#FEF3C7;`     |       |
| ring-offset-yellow-200  | --ring-offset-color: `#FDE68A;`     |       |
| ring-offset-yellow-300  | --ring-offset-color: `#FCD34D;`     |       |
| ring-offset-yellow-400  | --ring-offset-color: `#FBBF24;`     |       |
| ring-offset-yellow-500  | --ring-offset-color: `#F59E0B;`     |       |
| ring-offset-yellow-600  | --ring-offset-color: `#D97706;`     |       |
| ring-offset-yellow-700  | --ring-offset-color: `#B45309;`     |       |
| ring-offset-yellow-800  | --ring-offset-color: `#92400E;`     |       |
| ring-offset-yellow-900  | --ring-offset-color: `#78350F;`     |       |
| ring-offset-green-50    | --ring-offset-color: `#ECFDF5;`     |       |
| ring-offset-green-100   | --ring-offset-color: `#D1FAE5;`     |       |
| ring-offset-green-200   | --ring-offset-color: `#A7F3D0;`     |       |
| ring-offset-green-300   | --ring-offset-color: `#6EE7B7;`     |       |
| ring-offset-green-400   | --ring-offset-color: `#34D399;`     |       |
| ring-offset-green-500   | --ring-offset-color: `#10B981;`     |       |
| ring-offset-green-600   | --ring-offset-color: `#059669;`     |       |
| ring-offset-green-700   | --ring-offset-color: `#047857;`     |       |
| ring-offset-green-800   | --ring-offset-color: `#065F46;`     |       |
| ring-offset-green-900   | --ring-offset-color: `#064E3B;`     |       |
| ring-offset-blue-50     | --ring-offset-color: `#EFF6FF;`     |       |
| ring-offset-blue-100    | --ring-offset-color: `#DBEAFE;`     |       |
| ring-offset-blue-200    | --ring-offset-color: `#BFDBFE;`     |       |
| ring-offset-blue-300    | --ring-offset-color: `#93C5FD;`     |       |
| ring-offset-blue-400    | --ring-offset-color: `#60A5FA;`     |       |
| ring-offset-blue-500    | --ring-offset-color: `#3B82F6;`     |       |
| ring-offset-blue-600    | --ring-offset-color: `#2563EB;`     |       |
| ring-offset-blue-700    | --ring-offset-color: `#1D4ED8;`     |       |
| ring-offset-blue-800    | --ring-offset-color: `#1E40AF;`     |       |
| ring-offset-blue-900    | --ring-offset-color: `#1E3A8A;`     |       |
| ring-offset-indigo-50   | --ring-offset-color: `#EEF2FF;`     |       |
| ring-offset-indigo-100  | --ring-offset-color: `#E0E7FF;`     |       |
| ring-offset-indigo-200  | --ring-offset-color: `#C7D2FE;`     |       |
| ring-offset-indigo-300  | --ring-offset-color: `#A5B4FC;`     |       |
| ring-offset-indigo-400  | --ring-offset-color: `#818CF8;`     |       |
| ring-offset-indigo-500  | --ring-offset-color: `#6366F1;`     |       |
| ring-offset-indigo-600  | --ring-offset-color: `#4F46E5;`     |       |
| ring-offset-indigo-700  | --ring-offset-color: `#4338CA;`     |       |
| ring-offset-indigo-800  | --ring-offset-color: `#3730A3;`     |       |
| ring-offset-indigo-900  | --ring-offset-color: `#312E81;`     |       |
| ring-offset-purple-50   | --ring-offset-color: `#F5F3FF;`     |       |
| ring-offset-purple-100  | --ring-offset-color: `#EDE9FE;`     |       |
| ring-offset-purple-200  | --ring-offset-color: `#DDD6FE;`     |       |
| ring-offset-purple-300  | --ring-offset-color: `#C4B5FD;`     |       |
| ring-offset-purple-400  | --ring-offset-color: `#A78BFA;`     |       |
| ring-offset-purple-500  | --ring-offset-color: `#8B5CF6;`     |       |
| ring-offset-purple-600  | --ring-offset-color: `#7C3AED;`     |       |
| ring-offset-purple-700  | --ring-offset-color: `#6D28D9;`     |       |
| ring-offset-purple-800  | --ring-offset-color: `#5B21B6;`     |       |
| ring-offset-purple-900  | --ring-offset-color: `#4C1D95;`     |       |
| ring-offset-pink-50     | --ring-offset-color: `#FDF2F8;`     |       |
| ring-offset-pink-100    | --ring-offset-color: `#FCE7F3;`     |       |
| ring-offset-pink-200    | --ring-offset-color: `#FBCFE8;`     |       |
| ring-offset-pink-300    | --ring-offset-color: `#F9A8D4;`     |       |
| ring-offset-pink-400    | --ring-offset-color: `#F472B6;`     |       |
| ring-offset-pink-500    | --ring-offset-color: `#EC4899;`     |       |
| ring-offset-pink-600    | --ring-offset-color: `#DB2777;`     |       |
| ring-offset-pink-700    | --ring-offset-color: `#BE185D;`     |       |
| ring-offset-pink-800    | --ring-offset-color: `#9D174D;`     |       |
| ring-offset-pink-900    | --ring-offset-color: `#831843;`     |       |















---

## Transitions & Animations



### Transition Property
Sets the CSS properties affected by transition animations.

| Tailwind             | Description                                                                                               | Other |
| -------------------- | --------------------------------------------------------------------------------------------------------- | ----- |
| transition           | transition-property: background-color, border-color, color, fill, stroke, opacity, box-shadow, transform; |       |
| transition-none      | transition-property: none;                                                                                |       |
| transition-all       | transition-property: all;                                                                                 |       |
| transition-colors    | transition-property: background-color, border-color, color, fill, stroke;                                 |       |
| transition-opacity   | transition-property: opacity;                                                                             |       |
| transition-shadow    | transition-property: box-shadow;                                                                          |       |
| transition-transform | transition-property: transform;                                                                           |       |




### Transition Duration
Sets the length of time for a transition animations to complete.

| Tailwind      | Description                  | Other |
| ------------- | ---------------------------- | ----- |
| duration-75   | transition-duration: 75ms;   |       |
| duration-100  | transition-duration: 100ms;  |       |
| duration-150  | transition-duration: 150ms;  |       |
| duration-200  | transition-duration: 200ms;  |       |
| duration-300  | transition-duration: 300ms;  |       |
| duration-500  | transition-duration: 500ms;  |       |
| duration-700  | transition-duration: 700ms;  |       |
| duration-1000 | transition-duration: 1000ms; |       |



### Transition Timing Function
Sets the easing function of transition animations.

| Tailwind    | Description                                               | Other |
| ----------- | --------------------------------------------------------- | ----- |
| ease-linear | transition-timing-function: linear;                       |       |
| ease-in     | transition-timing-function: cubic-bezier(0.4, 0, 1, 1);   |       |
| ease-out    | transition-timing-function: cubic-bezier(0, 0, 0.2, 1);   |       |
| ease-in-out | transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1); |       |




### Transition Delay
Sets the CSS properties affected by transition delay.

| Tailwind   | Description               | Other |
| ---------- | ------------------------- | ----- |
| delay-75   | transition-delay: 75ms;   |       |
| delay-100  | transition-delay: 100ms;  |       |
| delay-150  | transition-delay: 150ms;  |       |
| delay-200  | transition-delay: 200ms;  |       |
| delay-300  | transition-delay: 300ms;  |       |
| delay-500  | transition-delay: 500ms;  |       |
| delay-700  | transition-delay: 700ms;  |       |
| delay-1000 | transition-delay: 1000ms; |       |





### Animation
Utilities for animating elements with CSS animations.

| Tailwind       | Description                                                                                                                                                                                                                                           | Other |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| animate-none   | animation: none;                                                                                                                                                                                                                                      |       |
| animate-spin   | animation: spin 1s linear infinite; @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }                                                                                                                           |       |
| animate-ping   | animation: ping 1s cubic-bezier(0, 0, 0.2, 1) infinite; @keyframes ping { 75%, 100% { transform: scale(2); opacity: 0; } }                                                                                                                            |       |
| animate-pulse  | animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: .5; } }                                                                                                                         |       |
| animate-bounce | animation: animation: bounce 1s infinite; @keyframes bounce { 0%, 100% { transform: translateY(-25%); animationTimingFunction: cubic-bezier(0.8, 0, 1, 1); } 50% { transform: translateY(0); animationTimingFunction: cubic-bezier(0, 0, 0.2, 1); } } |       |


---

## Tables


### Border Collapse
Collapse or separate table borders.

| Tailwind        | Description                | Other |
| --------------- | -------------------------- | ----- |
| border-collapse | border-collapse: collapse; |       |
| border-separate | border-collapse: separate; |       |



### Table Layout
Defines the algorithm used to lay out table cells, rows, and columns.

| Tailwind    | Description          | Other |
| ----------- | -------------------- | ----- |
| table-auto  | table-layout: auto;  |       |
| table-fixed | table-layout: fixed; |       |



---

