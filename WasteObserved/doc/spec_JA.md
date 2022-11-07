<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティWasteObserved  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteObserved/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**このエンティティは、廃棄物の単一のコレクションをモデル化する**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `annotations[array]`: アイテムに関するアノテーション  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: 製品の色  . Model: [https://schema.org/color](https://schema.org/color)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateObserved[string]`: ISO8601 UTCフォーマットでの廃棄物回収時刻。  - `description[string]`: このアイテムの説明  - `grossWeight[number]`: 回収された廃棄物の総重量。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes )を用いて付与する。例えば、'KGM'はキログラムを表す。  - `id[*]`: エンティティの一意な識別子  - `image[string]`: アイテムの画像  . Model: [https://schema.org/URL](https://schema.org/URL)- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `refGarbageTruck[*]`: ガベージコレクション中に使用される車両を参照する、車両スマートモデルへの参照。***これを1）外部システムのID（文字列）、または2）他のNGSIエンティティへの適切な参照（例：refVehicle:Truck123 ?  - `refServiceOrderId[*]`: 作業指示を含む外部システムへの参照。これは、ゴミ収集を要求するクライアントに関するデータ、またはゴミ収集のための作業指示、または他の関連する参照を含むかもしれない。  - `refWeighingDevice[*]`: 廃棄物の重量を測定するために使用される装置への言及。  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `tareWeight[number]`: 回収した廃棄物の風袋重量。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes )を用いて付与する。例えば、'KGM'はキログラムを表す。  - `type[string]`: NGSI エンティティタイプ。これはWasteObservedでなければならない。  - `weight[number]`: 回収された廃棄物の正味重量。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes )を用いて付与する。例えば、'KGM'はキログラムを表す。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
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
## ペイロードの例  
#### WasteObserved NGSI-v2 key-value 例  
以下は、WasteObservedをJSON-LD形式でkey-valuesにした例である。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### 廃棄物量 NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のWasteObservedの例である。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### 廃棄物観測 NGSI-LD キー値例  
以下は、WasteObservedをJSON-LD形式でkey-valuesにした例である。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返される。  
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
#### 廃棄物観測 NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のWasteObservedの例である。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
