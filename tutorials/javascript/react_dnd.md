---
slug: react-dnd
title: "React: Drag and Drop from Scratch"
authors: Aaron Wolf
sidebar_position: 4
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## Introduction

In this tutorial I will show how to make a Drag and Drop component from scratch with no 3rd party libraries using React.


## Important info

1. There exists the event handler `e.dataTransfer` which helps with drag and drop functionality, but as we're using React I find using state to be simpler.

2. Make sure to check out the [Code Sandbox](https://codesandbox.io/s/change-cursor-on-dragover-rfl5u?file=/src/Dnd.js). I may add a few things that aren't reflected below, but the code below is complete.

3. You might know a better way to do this! If you think you can improve the code please comment.

<!-- truncate -->

## Drag and drop in html5

There are a few new elements that we will be using thought we're not using _all_ of the HTML5 Drag and Drop elements.

1. `draggable` makes a div **draggable** (instead of highlighting when you click and drag)
2. `onDragStart` fires ONCE when you **begin** to drag
3. `onDragEnter` fires ONCE when the dragged div **enters** another.
4. `onDragOver` fires **CONTINUOUSLY** when **dragging over** a div
5. `onDrop` fires when the **mouse click is released**

The final 4 of these we will pass to JavaScript to give it the DND logic.


## Getting started

Let's make a some `groups` to drag between and some `item`s to be dragged around.

Dnd.js
```javascript
import React, { useState } from "react";
import "./Dnd.scss";

export default function Dnd() {

  // my groups to be dragged between

  const groups = ["group1", "group2", "group3", "noDrop"];

  // My items to be dragged around

  const initialItems = [
    { id: 1, group: "group1", value: "drag 1" },
    { id: 2, group: "group1", value: "drag 2" },
    { id: 3, group: "group1", value: "drag 3" }
  ];

  return (
    <>

      // Creating the group divs 

      <div className="groups">
        {groups.map((group) => (
          <div className="group">
            <h1 className="title">{group}</h1>
            <div>

              // Creating our items to drag and drop

              {items
                .filter((item) => item.group === group)
                .map((item) => (
                  <div
                    key={item.id}
                    id={item.id}
                    className="item"

                    // THIS MAKES THE ITEM DRAGGABLE!!!

                    draggable
                  >
                     // item title
                    {item.value}
                  </div>
                ))}
            </div>
          </div>
        ))}
      </div>
    </>
  );
}

```

Dnd.scss

```scss
.groups {
  display: flex;
  margin: 5px;
  padding: 5px;
  flex-wrap: wrap;
  

  .group {
    margin: 2px;
    padding: 20px;
    min-height: 16rem;
    background-color: green;

    .title{
      color: white;
      padding: 0;
      margin-top: 0;
    }
  }
}


.item {
  background-color: yellow;
  color: blue;
  margin: 5px;
  padding: 5px;
  border: 2px green;
  cursor: grab;
}
```

The code above creates something that looks like this: 
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qdoz1o8do2cr1zvt8s3y.png)


Now we'll add the events and the event handlers. Make sure to read the comments in the code as that's where the explanations are. I think this is simpler than describing everything outside of the code.

Hint: The comments are easier to read in the [Code Sandbox](https://codesandbox.io/s/change-cursor-on-dragover-rfl5u?file=/src/Dnd.js).

Dnd.js
```javascript
import React, { useState } from "react";
import "./Dnd.scss";

export default function Dnd() {
  // Initial groups to drag between
  const groups = ["group1", "group2", "group3", "noDrop"];
  // Initial items to be dragged 
  const initialItems = [
    { id: 1, group: "group1", value: "drag 1" },
    { id: 2, group: "group1", value: "drag 2" },
    { id: 3, group: "group1", value: "drag 3" }
  ];
  // Sets the state of the items. I may add an "add" function later
  // Can be used to add items
  const [items, setItems] = useState(initialItems);
  // Data about a thing's id, origin, and destination
  const [dragData, setDragData] = useState({});
  // Are we hovering over the noDrop div?
  const [noDrop, setNoDrop] = useState("");

  // onDragStart we setDragData.
  // useState instead of e.dataTransfer so we can transfer more data
  const handleDragStart = (e, id, group) => {
    setDragData({ id: id, initialGroup: group });
  };

  // If we enter the noDrop zone the state will be updated
  // Used for styling.
  const handleDragEnter = (e, group) => {
    if (group === "noDrop") {
      setNoDrop("noDrop");
    }
  };

  // DND will not work without this.
  const handleDragOver = (e) => {
    e.preventDefault();
  };

  // setNoDrop to nothing to return styling to normal
  const handleDragLeave = (e) => {
    setNoDrop("");
  };

  // 1. makes copy of items (newItems)
  // 2. changes category of the item to its new group
  // 3. setItem to our NewItems
  const changeCategory = (itemId, group) => {
    const newItems = [...items];
    newItems[itemId - 1].group = group;
    setItems([...newItems]);
  };

  // 1. setNoDrop in case item was dropped in noDrop
  // 2. gets the item id
  // 3. doesn't allow drop in noDrop
  // 4. changeCategory (see above)
  const handleDrop = (e, group) => {
    setNoDrop("");
    const selected = dragData.id;
    if (group === "noDrop") {
      console.log("nuh uh");
    } else {
      changeCategory(selected, group);
    }
  };

  return (
    <>
      <div className="groups">
        {/* iterate over groups */}
        {groups.map((group) => (
          <div
            // change styling if dragging into noDrop zone
            className={`${
              group === "noDrop" && noDrop === "noDrop" ? noDrop : "group"
            }`}
            // event handlers
            onDragEnter={(e) => handleDragEnter(e, group)}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={(e) => handleDrop(e, group)}
            key={group}
          >
            <h1 className="title">{group}</h1>
            <div>
              {/* iterate over items */}
              {items
                .filter((item) => item.group === group)
                .map((item) => (
                  <div
                    key={item.id}
                    id={item.id}
                    // change style if dragged over noDrop
                    className={`${
                      group === "noDrop" && noDrop === "noDrop"
                        ? "notAllowed"
                        : "item"
                    }`}
                    // MAKES THE ITEM DRAGGABLE!!!!
                    draggable
                    // event handler
                    onDragStart={(e) => handleDragStart(e, item.id, group)}
                  >
                    {/* The name of each item */}
                    {item.value}
                  </div>
                ))}
            </div>
          </div>
        ))}
      </div>
    </>
  );
}
```

Dnd.scss

```scss
.groups {
  display: flex;
  margin: 5px;
  padding: 5px;
  flex-wrap: wrap;
  

  .group {
    margin: 2px;
    padding: 20px;
    min-height: 16rem;
    background-color: green;

    .title{
      color: white;
      padding: 0;
      margin-top: 0;
    }
  }
  .noDrop {
    margin: 2px;
    padding: 20px;
    min-height: 16rem;
    background-color: red;
    cursor: not-allowed !important;

    .title{
      color: white;
      padding: 0;
      margin-top: 0;
    }
  }
}


.item {
  background-color: yellow;
  color: blue;
  margin: 5px;
  padding: 5px;
  border: 2px green;
  cursor: grab;
}

.notAllowed {
  background-color: yellow;
  color: blue;
  margin: 5px;
  padding: 5px;
  border: 2px green;
  cursor: not-allowed;
}
```

## This is what it looks like

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7vcxwt7g8lvah8amwn2r.gif)

## Conclusion

This is the basic gist of it. If you need something simple that works this is it, otherwise feel free to install a library. 

Watch it in action! [See the Code Sandbox](https://codesandbox.io/s/change-cursor-on-dragover-rfl5u?file=/src/Dnd.js)
