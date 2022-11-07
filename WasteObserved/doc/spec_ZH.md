<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。观察到的废物  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteObserved/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**该实体为一个单一的废物集合建模。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `annotations[array]`: 关于该项目的注释  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: 产品的颜色  . Model: [https://schema.org/color](https://schema.org/color)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `dateObserved[string]`: 采集垃圾的时间，以ISO8601 UTC格式表示。  - `description[string]`: 对这个项目的描述  - `grossWeight[number]`: 收集的废物的毛重。单位代码（文本）使用[UN/CEFACT通用代码](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes )给出。例如，"KGM "代表公斤  - `id[*]`: 实体的唯一标识符  - `image[string]`: 该物品的图像  . Model: [https://schema.org/URL](https://schema.org/URL)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `refGarbageTruck[*]`: 一个对车辆智能模型的引用，指的是垃圾收集期间使用的车辆。***我可以把它定义为：1）一个外部系统的ID（字符串），或者2）一个对另一个NGSI实体的适当引用（例如，refVehicle:Truck123 ?  - `refServiceOrderId[*]`: 一个对包含工作单的外部系统的引用。这可能包含一个要求收集垃圾的客户的数据，或一个收集垃圾的工作单，或任何其他相关的参考。  - `refWeighingDevice[*]`: 用于测量废物重量的设备的参考。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `tareWeight[number]`: 收集的废物的皮重。单位代码（文本）使用[UN/CEFACT通用代码](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes )给出。例如，'KGM'代表公斤  - `type[string]`: NGSI实体类型。它必须是WasteObserved  - `weight[number]`: 收集的废物的净重。单位代码（文本）使用[UN/CEFACT通用代码](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes )给出。例如，"KGM "代表公斤  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
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
## ＃＃＃＃有效载荷的例子  
#### WasteObserved NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为关键值的WasteObserved的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的背景数据。  
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
#### WasteObserved NGSI-v2 normalized 示例  
下面是一个以JSON-LD格式规范化的WasteObserved的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### WasteObserved NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为关键值的WasteObserved的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### 观察到的废物NGSI-LD归一化的例子  
下面是一个以JSON-LD格式规范化的WasteObserved的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
