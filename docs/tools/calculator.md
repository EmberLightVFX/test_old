# Calculator

```calculator
{
    "element": "group",
    "columns": 3,
    "content": [
        {
            "element": "list",
            "varName": "vendor",
            "label": "Vendor",
            "generate": "Object.keys(db);",
            "onChange": "updateList('camera', Object.keys(db[vendor.value]));",
            "help": "Text under again"
        },
        {
            "element": "list",
            "varName": "camera",
            "label": "Camera",
            "generate": "updateList('camera', Object.keys(db[vendor.value]));",
            "onChange": "updateList('sensor', Object.keys(db[vendor.value][camera.value]['sensor dimensions']));",
            "help": "Text under again"
        },
        {
            "element": "list",
            "varName": "sensor",
            "label": "Sensor",
            "generate": "updateList('sensor', Object.keys(db[vendor.value][camera.value]['sensor dimensions']));",
            "help": "Text under again"
        }
    ]
},
{
    "varName": "A",
    "type": "number",
    "element": "input",
    "label": "Number 1",
    "prefix": "@",
    "value": "123",
    "suffix": "$",
    "help": "Text under",
    "readOnly": false,
    "disabled": false
},
{
    "varName": "B",
    "label": "Number 2",
    "element": "input",
    "type": "number",
    "placeholder": "something",
    "prefix": "@",
    "suffix": "$",
    "help": "Text under again",
    "readOnly": false,
    "disabled": false
},
{
    "varName": "C",
    "label": "List 1",
    "element": "list",
    "placeholder": "Pick a fruit",
    "list": [
        {
            "name": "apple",
            "value": 1
        },
        {
            "name": "banana",
            "value": 2
        },
        {
            "name": "orange",
            "value": 3
        }
    ],
    "prefix": "@",
    "suffix": "$",
    "help": "Text under again",
    "readOnly": false,
    "disabled": false
},
{
    "label": "Resolution",
    "element": "multi",
    "content": [
        {
            "varName": "X",
            "ariaLabel": "Width",
            "element": "input",
            "type": "number",
            "prefix": "@",
            "suffix": "$",
            "readOnly": false,
            "disabled": false
        },
        {
            "varName": "Y",
            "ariaLabel": "Height",
            "element": "input",
            "type": "number",
            "prefix": "@",
            "suffix": "$",
            "readOnly": false,
            "disabled": false
        }
    ],
    "help": "Text under this multi",
    "readOnly": false,
    "disabled": false
},
{
    "element": "sum",
    "label": "Total",
    "formula": "A * B",
    "prefix": "@",
    "suffix": "$",
    "help": "Text under again",
    "disabled": false
}
```
