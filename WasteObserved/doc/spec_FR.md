<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : WasteObserved  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteObserved/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Cette entité modélise une seule collection de déchets.**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `annotations[array]`: Annotations sur l'élément  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: La couleur du produit  . Model: [https://schema.org/color](https://schema.org/color)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateObserved[string]`: Heure de la collecte des déchets au format ISO8601 UTC.  - `description[string]`: Une description de cet article  - `grossWeight[number]`: Le poids brut des déchets collectés. Le code de l'unité (texte) est donné à l'aide des [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes ). Par exemple, "KGM" représente le kilogramme.  - `id[*]`: Identifiant unique de l'entité  - `image[string]`: Une image de l'article  . Model: [https://schema.org/URL](https://schema.org/URL)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `refGarbageTruck[*]`: Une référence à un modèle Vehicle Smart référençant le véhicule utilisé lors de la collecte des ordures. ***Puis-je le définir comme 1) un identifiant (chaîne de caractères) d'un système externe, ou 2) une référence propre à une autre entité NGSI (par exemple refVehicle:Truck123 ? ??) ?  - `refServiceOrderId[*]`: Une référence à un système externe contenant des bons de travail. Cela peut contenir des données sur un client demandant la collecte des ordures, ou un bon de travail pour la collecte des déchets, ou toute autre référence pertinente.  - `refWeighingDevice[*]`: Une référence à l'appareil utilisé pour mesurer le poids des déchets.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `tareWeight[number]`: Le poids à vide des déchets collectés. Le code de l'unité (texte) est indiqué à l'aide des [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes ). Par exemple, "KGM" représente le kilogramme.  - `type[string]`: Type d'entité NGSI. Il doit s'agir de WasteObserved  - `weight[number]`: Le poids net des déchets collectés. Le code de l'unité (texte) est donné à l'aide des [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes ). Par exemple, "KGM" représente le kilogramme.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WasteObserved:    
  description: 'This entity models a single collection of Waste.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
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
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    color:    
      description: 'The color of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
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
    dateObserved:    
      description: 'Time of the wastecollection in ISO8601 UTCformat.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    grossWeight:    
      description: 'The gross weight of the collected waste. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes ). For instance, ''KGM'' represents kilogram'    
      type: number    
      x-ngsi:    
        type: Property    
        units: ' KGM.'    
    id:    
      anyOf: &wasteobserved_-_properties_-_owner_-_items_-_anyof    
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
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wasteobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refGarbageTruck:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A reference to an Vehicle Smart model referencing the vehicle used during garbage collection. ***Can I define this as either 1) an id (string) of an external system, or 2) a proper reference to another NGSI entity (e.g. refVehicle:Truck123 ???'    
      x-ngsi:    
        type: Relationship    
    refServiceOrderId:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A reference to an external system containing workorders. This might contain data about a client requesting the garbage collection, or a workorder for waste collection, or any other relevant reference.'    
      x-ngsi:    
        type: Relationship    
    refWeighingDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A reference to the device used to measure the waste weight.'    
      x-ngsi:    
        type: Relationship    
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
    tareWeight:    
      description: 'The tare weight of the collected waste. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes ). For instance, ''KGM'' represents kilogram'    
      type: number    
      x-ngsi:    
        type: Property    
        units: ' KGM.'    
    type:    
      description: 'NGSI Entity type. It has to be WasteObserved'    
      enum:    
        - WasteObserved    
      type: string    
      x-ngsi:    
        type: Property    
    weight:    
      description: 'The net weight of the collected waste. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes ). For instance, ''KGM'' represents kilogram'    
      type: number    
      x-ngsi:    
        type: Property    
        units: ' KGM.'    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.WasteManagement/blob/master/WasteObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.WasteManagement/WasteObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Valeurs-clés de la NGSI-v2 WasteObserved Exemple  
Voici un exemple de WasteObserved au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "ngsi-ld:WasteObserved:001",  
  "type": "WasteObserved",  
  "tareWeight": 2.0,  
  "address": {  
    "addressCountry": "BE",  
    "postalCode": "2018",  
    "streetAddress": "Lange Kievitstraat n\u00b070"  
  },  
  "dateObserved": "2022-10-19T14:57:39.000Z",  
  "grossWeight": 8.85,  
  "location": {  
      "coordinates": [  
          4.421732917,  
          51.21301073  
        ],  
      "type": "Point"  
    },  
  "refServiceOrderId": "ngsi-ld:WorkOrder1234",  
    "weight": 6.85  
}  
```  
</details>  
#### DéchetsObservés NGSI-v2 normalisé Exemple  
Voici un exemple de WasteObserved au format JSON-LD tel que normalisé. Ceci est compatible avec la NGSI-v2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "WasteObserved:<uuid of Observer>",  
	"type": "WasteObserved",  
	"location": {  
		"type": "geo:json",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.421732917,  
				51.21301073  
			]  
		},  
		"metadata": {  
			"timestamp": {  
				"type": "DateTime",  
				"value": "2022-10-19T14:57:39.000Z"  
			}  
		}  
	},  
	"address": {  
		"type": "PostalAddress",  
		"value": {  
			"postalCode": "2018",  
			"streetAddress": "Lange Kievitstraat n°70",  
			"addressCountry": "BE"  
		},  
		"metadata": {  
			"timestamp": {  
				"type": "DateTime",  
				"value": "2022-10-19T14:57:39.000Z"  
			}  
		}  
	},  
	"dateObserved": {  
		"type": "DateTime",  
		"value": "2022-10-19T14:57:39.000Z",  
		"metadata": {}  
	},  
	"weight": {  
		"type": "Number",  
		"value": 6.85,  
		"metadata": {  
			"UnitCode": {  
				"type": "string",  
				"value": "KGM"  
			}  
		}  
	},  
	"grossWeight": {  
		"type": "Number",  
		"value": 8.85,  
		"metadata": {  
			"UnitCode": {  
				"type": "string",  
				"value": "KGM"  
			}  
		}  
	},  
	"tareWeight": {  
		"type": "Number",  
		"value": 2.0,  
		"metadata": {  
			"UnitCode": {  
				"type": "string",  
				"value": "KGM"  
			}  
		}  
	},  
	"refServiceOrderId": {  
		"type": "Relationship",  
		"value": "ngsi-ld:WorkOrder1234"  
	}  
}  
```  
</details>  
#### Valeurs-clés NGSI-LD de WasteObserved Exemple  
Voici un exemple de WasteObserved au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et retourne les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "ngsi-ld:WasteObserved:001",  
  "type": "WasteObserved",  
  "tareWeight": 2.0,  
  "address": {  
    "addressCountry": "BE",  
    "postalCode": "2018",  
    "streetAddress": "Lange Kievitstraat n\u00b070"  
  },  
  "dateObserved": "2022-10-19T14:57:39.000Z",  
  "grossWeight": 8.85,  
  "location": {  
      "coordinates": [  
          4.421732917,  
          51.21301073  
        ],  
      "type": "Point"  
    },  
  "refServiceOrderId": "ngsi-ld:WorkOrder1234",  
    "weight": 6.85,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteManagement/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### DéchetsObservés NGSI-LD normalisé Exemple  
Voici un exemple de WasteObserved au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "ngsi-ld:WasteObserved:0001",  
  "type": "WasteObserved",  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        4.421732917,  
        51.21301073  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "postalCode": "2018",  
      "streetAddress": "Lange Kievitstraat nÂ°70",  
      "addressCountry": "BE"  
    }  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-10-19T14:57:39.000Z"  
    }  
  },  
  "weight": {  
    "type": "Property",  
    "value": 6.85  
  },  
  "grossWeight": {  
    "type": "Property",  
    "value": 8.85  
  },  
  "tareWeight": {  
    "type": "Property",  
    "value": 2.0  
  },  
  "refServiceOrderId": {  
    "type": "Relationship",  
    "value": "ngsi-ld:WorkOrder1234"  
  }  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
