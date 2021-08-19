Entity: WasteContainerModel  
===========================  
[Open License](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainerModel/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **A model of waste container which captures the static properties of a class of containers.**  

## List of properties  

- `alternateName`: An alternative name for this item  - `annotations`: Annotations about the item  - `brandName`: Name of the brand  - `cargoVolume`: Total volume the container can hold  - `category`: Container’s category. Enum:'dumpster, trashCan, wheelieBin, other'.  dumpster . See [https://en.wikipedia.org/wiki/Dumpster](https://en.wikipedia.org/wiki/Dumpster)  - `color`: The color of the product  - `compliantWith`: A list of standards to which the container is compliant  with (ex. UNE-EN 840-2:2013).   - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `depth`: Depth of the container  - `description`: A description of this item  - `features`: A list of container features. Enum:'wheels, lid, roundedLid, insertHoles, lockable'. Any other value meaningful for the application.  - `height`: Height of the container  - `id`: Unique identifier of the entity  - `image`: An image of the item  - `insertHolesNumber`: Number of insert holes the container has  - `madeOf`: Material the container is made of. Enum:' plastic , wood, metal, other '  - `madeOfCode`: Material Code as per standard tables.   - `manufacturerName`: Name of the manufacturer.   - `maximumLoad`: Maximum load the container can hold safely. Unit:'Kilogram'  - `modelName`: Name of the model as given by the manufacturer. This attribute is different than name which is just a codename usually given by municipalities.  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `recommendedLoad`: Manufacturer recommended load for the container. Unit:'Kilogram'  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity Type: It has to be WasteContainerModel  - `weight`: Weight of the container  - `width`: Width of the container    
Required properties  
- `id`  - `name`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WasteContainerModel:    
  description: 'A model of waste container which captures the static properties of a class of containers.'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    brandName:    
      description: 'Name of the brand'    
      type: string    
      x-ngsi:    
        model: https://schema.org/brand    
        type: Property    
    cargoVolume:    
      description: 'Total volume the container can hold'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/cargoVolume    
        type: Property    
    category:    
      description: 'Container’s category. Enum:''dumpster, trashCan, wheelieBin, other''.  dumpster . See [https://en.wikipedia.org/wiki/Dumpster](https://en.wikipedia.org/wiki/Dumpster)'    
      items:    
        enum:    
          - dumpster    
          - trashCan    
          - wheelieBin    
          - other    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    color:    
      description: 'The color of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    compliantWith:    
      description: 'A list of standards to which the container is compliant  with (ex. UNE-EN 840-2:2013). '    
      items:    
        type: string    
      minItems: 0    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    depth:    
      description: 'Depth of the container'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/depth    
        type: Property    
        units: Meters    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    features:    
      description: 'A list of container features. Enum:''wheels, lid, roundedLid, insertHoles, lockable''. Any other value meaningful for the application.'    
      items:    
        enum:    
          - wheels    
          - lid    
          - roundedLid    
          - insertHoles    
          - lockable    
          - other    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    height:    
      description: 'Height of the container'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/heigth    
        type: Property    
        units: Meters    
    id:    
      anyOf: &wastecontainermodel_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    insertHolesNumber:    
      description: 'Number of insert holes the container has'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    madeOf:    
      description: 'Material the container is made of. Enum:'' plastic , wood, metal, other '''    
      enum:    
        - plastic    
        - wood    
        - metal    
        - other    
      type: string    
      x-ngsi:    
        type: Property    
    madeOfCode:    
      description: 'Material Code as per standard tables. '    
      type: string    
      x-ngsi:    
        type: Property    
    manufacturerName:    
      description: 'Name of the manufacturer. '    
      type: string    
      x-ngsi:    
        type: Property    
    maximumLoad:    
      description: 'Maximum load the container can hold safely. Unit:''Kilogram'''    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    modelName:    
      description: 'Name of the model as given by the manufacturer. This attribute is different than name which is just a codename usually given by municipalities.'    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wastecontainermodel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    recommendedLoad:    
      description: 'Manufacturer recommended load for the container. Unit:''Kilogram'''    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity Type: It has to be WasteContainerModel'    
      enum:    
        - WasteContainerModel    
      type: string    
      x-ngsi:    
        type: Property    
    weight:    
      description: 'Weight of the container'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/weigth    
        type: Property    
        units: Kilograms    
    width:    
      description: 'Width of the container'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/width    
        type: Property    
        units: Meters    
  required:    
    - id    
    - type    
    - name    
  type: object    
```  
</details>    
## Example payloads    
#### WasteContainerModel NGSI-v2 key-values Example    
Here is an example of a WasteContainerModel in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "wastecontainermodel:c1",  
  "type": "WasteContainerModel",  
  "width": 0.5,  
  "height": 0.8,  
  "depth": 0.4,  
  "cargoVolume": 150,  
  "brandName": "Brute",  
  "name": "Dumpster_Brute_2009_Plastic_Green",  
  "modelName": "C1",  
  "compliantWith": ["UNE-EN 840-2:2013"],  
  "madeOf": "plastic",  
  "features": ["wheels", "lid"],  
  "category": ["dumpster"]  
}  
```  
#### WasteContainerModel NGSI-v2 normalized Example    
Here is an example of a WasteContainerModel in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "wastecontainermodel:c1",  
  "type": "WasteContainerModel",  
  "category": {  
    "type": "array",  
    "value": [  
      "dumpster"  
    ]  
  },  
  "cargoVolume": {  
    "type": "Number",  
    "value": 150  
  },  
  "modelName": {  
    "type": "Text",  
    "value": "C1"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Dumpster_Brute_2009_Plastic_Green"  
  },  
  "compliantWith": {  
    "type": "array>",  
    "value": [  
      "UNE-EN 840-2:2013"  
    ]  
  },  
  "madeOf": {  
    "type": "Text",  
    "value": "plastic"  
  },  
  "height": {  
    "type": "Number",  
    "value": 0.8  
  },  
  "width": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "depth": {  
    "type": "Number",  
    "value": 0.4  
  },  
  "brandName": {  
    "type": "Text",  
    "value": "Brute"  
  },  
  "features": {  
    "type": "array",  
    "value": [  
      "wheels",  
      "lid"  
    ]  
  }  
}  
```  
#### WasteContainerModel NGSI-LD key-values Example    
Here is an example of a WasteContainerModel in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "brandName": "Brute",  
  "cargoVolume": 150,  
  "category": [  
    "dumpster"  
  ],  
  "compliantWith": [  
    "UNE-EN 840-2:2013"  
  ],  
  "depth": 0.4,  
  "features": [  
    "wheels",  
    "lid"  
  ],  
  "height": 0.8,  
  "id": "urn:ngsi-ld:WasteContainerModel:wastecontainermodel:c1",  
  "madeOf": "plastic",  
  "modelName": "C1",  
  "name": "Dumpster_Brute_2009_Plastic_Green",  
  "type": "WasteContainerModel",  
  "width": 0.5  
}  
```  
#### WasteContainerModel NGSI-LD normalized Example    
Here is an example of a WasteContainerModel in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:WasteContainerModel:wastecontainermodel:c1",  
  "type": "WasteContainerModel",  
  "category": {  
    "type": "Property",  
    "value": [  
      "dumpster"  
    ]  
  },  
  "cargoVolume": {  
    "type": "Property",  
    "value": 150  
  },  
  "modelName": {  
    "type": "Property",  
    "value": "C1"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Dumpster_Brute_2009_Plastic_Green"  
  },  
  "compliantWith": {  
    "type": "Property",  
    "value": [  
      "UNE-EN 840-2:2013"  
    ]  
  },  
  "madeOf": {  
    "type": "Property",  
    "value": "plastic"  
  },  
  "height": {  
    "type": "Property",  
    "value": 0.8  
  },  
  "width": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "depth": {  
    "type": "Property",  
    "value": 0.4  
  },  
  "brandName": {  
    "type": "Property",  
    "value": "Brute"  
  },  
  "features": {  
    "type": "Property",  
    "value": [  
      "wheels",  
      "lid"  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
