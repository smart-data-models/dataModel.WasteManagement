Entité : WasteContainerIsle  
===========================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainerIsle/LICENSE.md)  
Description globale : **Un îlot de conteneurs à déchets**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `features`: Une liste des fonctionnalités fournies par l'île.  - `id`: Identifiant unique de l'entité  - `insertHolesNumber`: Nombre de trous d'insertion de l'île  - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `refWasteContainer`: Liste des conteneurs présents dans l'île  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type d'entité NGSI : Il doit s'agir de WasteContainerIsle    
Propriétés requises  
- `id`  - `location`  - `type`    
Une zone géographique qui conserve un ou plusieurs conteneurs de déchets.  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WasteContainerIsle:    
  description: 'A waste container isle'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
    description:    
      description: 'A description of this item'    
      type: Property    
    features:    
      description: 'A list of features provided by the isle.'    
      items:    
        enum:    
          - containerFix    
          - underground    
          - fenced    
          - other    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
    id:    
      anyOf: &wastecontainerisle_-_properties_-_owner_-_items_-_anyof    
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
    insertHolesNumber:    
      description: 'Number of insert holes the isle has'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wastecontainerisle_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refWasteContainer:    
      description: 'List of containers present in the isle'    
      items:    
        anyOf: *wastecontainerisle_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/URL.    
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
      description: 'NGSI Entity Type: It has to be WasteContainerIsle'    
      enum:    
        - WasteContainerIsle    
      type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### WasteContainerIsle NGSI V2 key-values Exemple  
Voici un exemple d'une WasteContainerIsle en format JSON comme valeurs clés. Il est compatible avec la version 2 de l'INSG lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "wastecontainerisle:Fleming:12",  
  "type": "WasteContainerIsle",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [-3.164485591715449, 40.62785133667262],  
        [-3.164445130316209, 40.627871567372239],  
        [-3.164394553567159, 40.627772099765778],  
        [-3.164424899616589, 40.62775018317452],  
        [-3.164485591715449, 40.62785133667262]  
      ]  
    ]  
  },  
  "address": {  
    "streetAddress": "Calle Dr. Fleming, 12",  
    "addressLocality": "Guadalajara",  
    "addressCountry": "ES"  
  },  
  "features": ["underground"],  
  "name": "Dr. Fleming 12, Esquina Manuel Paez Xaramillo",  
  "description": "Container isle located downtown",  
  "refWasteContainer": [  
    "wastecontainer:Fleming:12a",  
    "wastecontainer:Fleming:12b"  
  ]  
}  
```  
#### WasteContainerIsle NGSI V2 normalisé Exemple  
Voici un exemple d'une WasteContainerIsle au format JSON normalisé. Ce format est compatible avec la version 2 de l'INSG lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "wastecontainerisle:Fleming:12",  
  "type": "WasteContainerIsle",  
  "refWasteContainer": {  
    "type": "Relationship",  
    "value": ["wastecontainer:Fleming:12a", "wastecontainer:Fleming:12b"]  
  },  
  "features": {  
    "value": ["underground"]  
  },  
  "description": {  
    "value": "Container isle located downtown"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [-3.164485591715449, 40.62785133667262],  
          [-3.164445130316209, 40.62787156737224],  
          [-3.164394553567159, 40.62777209976578],  
          [-3.164424899616589, 40.62775018317452],  
          [-3.164485591715449, 40.62785133667262]  
        ]  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "Guadalajara",  
      "addressCountry": "ES",  
      "streetAddress": "Calle Dr. Fleming, 12"  
    }  
  },  
  "name": {  
    "value": "Dr. Fleming 12, Esquina Manuel Paez Xaramillo"  
  }  
}  
```  
#### WasteContainerIsle NGSI-LD key-values Example  
Voici un exemple d'une WasteContainerIsle en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "address": {"addressCountry": "ES",  
             "addressLocality": "Guadalajara",  
             "streetAddress": "Calle Dr. Fleming, 12",  
             "type": "PostalAddress"},  
 "description": "Container isle located downtown",  
 "features": ["underground"],  
 "id": "urn:ngsi-ld:WasteContainerIsle:wastecontainerisle:Fleming:12",  
 "location": {"coordinates": [[[-3.164485591715449, 40.62785133667262],  
                               [-3.164445130316209, 40.62787156737224],  
                               [-3.164394553567159, 40.62777209976578],  
                               [-3.164424899616589, 40.62775018317452],  
                               [-3.164485591715449, 40.62785133667262]]],  
              "type": "Polygon"},  
 "name": "Dr. Fleming 12, Esquina Manuel Paez Xaramillo",  
 "refWasteContainer": ["urn:ngsi-ld:WasteContainer:wastecontainer:Fleming:12a",  
                       "urn:ngsi-ld:WasteContainer:wastecontainer:Fleming:12b"],  
 "type": "WasteContainerIsle"}  
```  
#### WasteContainerIsle NGSI-LD normalisé Exemple  
Voici un exemple de WasteContainerIsle au format JSON-LD tel que normalisé. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:WasteContainerIsle:wastecontainerisle:Fleming:12",  
    "type": "WasteContainerIsle",  
    "refWasteContainer": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:WasteContainer:wastecontainer:Fleming:12a",  
            "urn:ngsi-ld:WasteContainer:wastecontainer:Fleming:12b"  
        ]  
    },  
    "features": {  
        "type": "Property",  
        "value": [  
            "underground"  
        ]  
    },  
    "description": {  
        "type": "Property",  
        "value": "Container isle located downtown"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Polygon",  
            "coordinates": [  
                [  
                    [  
                        -3.164485591715449,  
                        40.62785133667262  
                    ],  
                    [  
                        -3.164445130316209,  
                        40.62787156737224  
                    ],  
                    [  
                        -3.164394553567159,  
                        40.62777209976578  
                    ],  
                    [  
                        -3.164424899616589,  
                        40.62775018317452  
                    ],  
                    [  
                        -3.164485591715449,  
                        40.62785133667262  
                    ]  
                ]  
            ]  
        }  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressLocality": "Guadalajara",  
            "addressCountry": "ES",  
            "streetAddress": "Calle Dr. Fleming, 12",  
            "type": "PostalAddress"  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "Dr. Fleming 12, Esquina Manuel Paez Xaramillo"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
