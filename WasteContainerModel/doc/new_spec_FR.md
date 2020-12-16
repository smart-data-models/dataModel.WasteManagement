Entité : WasteContainerModel  
============================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainerModel/LICENSE.md)  
Description globale : **Un modèle de conteneur de déchets qui saisit les propriétés statiques d'une classe de conteneurs.**  

## Liste des biens  

- `alternateName`: Un autre nom pour cet article  - `annotations`: Annotations sur le sujet  - `brandName`: Nom de la marque  - `cargoVolume`: Volume total que le conteneur peut contenir  - `category`: Catégorie du conteneur. Enum : "benne, poubelle, poubelle à roulettes, autre". benne . Voir [https://en.wikipedia.org/wiki/Dumpster](https://en.wikipedia.org/wiki/Dumpster)  - `color`: La couleur du produit  - `compliantWith`: Une liste des normes auxquelles le conteneur est conforme (ex. UNE-EN 840-2:2013).  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `depth`: Profondeur du conteneur  - `description`: Une description de cet article  - `features`: Une liste des caractéristiques des conteneurs. Enum : "roues, couvercle, arrondiCouvercle, trous d'insertion, verrouillable". Toute autre valeur significative pour l'application.  - `height`: Hauteur du conteneur  - `id`: Identifiant unique de l'entité  - `image`: Une image de l'objet  - `insertHolesNumber`: Nombre de trous d'insertion du récipient  - `madeOf`: Matériau dont le conteneur est fait. Enum:' plastique, bois, métal, autres '  - `madeOfCode`: Code des matériaux selon les tableaux standards.  - `manufacturerName`: Nom du fabricant.  - `maximumLoad`: Charge maximale que le conteneur peut contenir en toute sécurité. Unité : "Kilogramme  - `modelName`: Nom du modèle tel qu'il est indiqué par le fabricant. Cet attribut est différent du nom qui n'est qu'un nom de code habituellement donné par les municipalités.  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `recommendedLoad`: Charge recommandée par le fabricant pour le conteneur. Unité : "Kilogramme  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type d'entité NGSI : Il doit s'agir de WasteContainerModel  - `weight`: Poids du conteneur  - `width`: Largeur du conteneur    
Propriétés requises  
- `id`  - `name`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WasteContainerModel:    
  description: 'A model of waste container which captures the static properties of a class of containers.'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    brandName:    
      description: 'Name of the brand'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/brand    
    cargoVolume:    
      description: 'Total volume the container can hold'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/cargoVolume    
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
      type: Property    
      uniqueItems: true    
    color:    
      description: 'The color of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/color    
    compliantWith:    
      description: 'A list of standards to which the container is compliant  with (ex. UNE-EN 840-2:2013). '    
      items:    
        type: string    
      minItems: 0    
      type: Property    
      uniqueItems: true    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    depth:    
      description: 'Depth of the container'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/depth    
        units: Meters    
    description:    
      description: 'A description of this item'    
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
      type: Property    
      uniqueItems: true    
    height:    
      description: 'Height of the container'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/heigth    
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
      type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    insertHolesNumber:    
      description: 'Number of insert holes the container has'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    madeOf:    
      description: 'Material the container is made of. Enum:'' plastic , wood, metal, other '''    
      enum:    
        - plastic    
        - wood    
        - metal    
        - other    
      type: Property    
    madeOfCode:    
      description: 'Material Code as per standard tables. '    
      type: Property    
    manufacturerName:    
      description: 'Name of the manufacturer. '    
      type: Property    
    maximumLoad:    
      description: 'Maximum load the container can hold safely. Unit:''Kilogram'''    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    modelName:    
      description: 'Name of the model as given by the manufacturer. This attribute is different than name which is just a codename usually given by municipalities.'    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wastecontainermodel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    recommendedLoad:    
      description: 'Manufacturer recommended load for the container. Unit:''Kilogram'''    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity Type: It has to be WasteContainerModel'    
      enum:    
        - WasteContainerModel    
      type: Property    
    weight:    
      description: 'Weight of the container'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/weigth    
        units: Kilograms    
    width:    
      description: 'Width of the container'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/width    
        units: Meters    
  required:    
    - id    
    - type    
    - name    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### WasteContainerModel NGSI V2 key-values Example  
Voici un exemple de modèle de conteneur de déchets au format JSON comme valeurs clés. Ce modèle est compatible avec la version 2 de l'INSG lorsqu'il utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
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
#### WasteContainerModel NGSI V2 normalisé Exemple  
Voici un exemple de WasteContainerModel au format JSON tel que normalisé. Ce modèle est compatible avec la version 2 de l'INSG lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "wastecontainermodel:c1",  
  "type": "WasteContainerModel",  
  "category": {  
    "value": ["dumpster"]  
  },  
  "cargoVolume": {  
    "value": 150  
  },  
  "modelName": {  
    "value": "C1"  
  },  
  "name": {  
    "value": "Dumpster_Brute_2009_Plastic_Green"  
  },  
  "compliantWith": {  
    "value": ["UNE-EN 840-2:2013"]  
  },  
  "madeOf": {  
    "value": "plastic"  
  },  
  "height": {  
    "value": 0.8  
  },  
  "width": {  
    "value": 0.5  
  },  
  "depth": {  
    "value": 0.4  
  },  
  "brandName": {  
    "value": "Brute"  
  },  
  "features": {  
    "value": ["wheels", "lid"]  
  }  
}  
```  
#### WasteContainerModel NGSI-LD key-values Example  
Voici un exemple de modèle de conteneur de déchets au format JSON-LD comme valeurs clés. Ce modèle est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "brandName": "Brute",  
 "cargoVolume": 150,  
 "category": ["dumpster"],  
 "compliantWith": ["UNE-EN 840-2:2013"],  
 "depth": 0.4,  
 "features": ["wheels", "lid"],  
 "height": 0.8,  
 "id": "urn:ngsi-ld:WasteContainerModel:wastecontainermodel:c1",  
 "madeOf": "plastic",  
 "modelName": "C1",  
 "name": "Dumpster_Brute_2009_Plastic_Green",  
 "type": "WasteContainerModel",  
 "width": 0.5}  
```  
#### WasteContainerModel NGSI-LD normalisé Exemple  
Voici un exemple de WasteContainerModel au format JSON-LD tel que normalisé. Ce modèle est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
