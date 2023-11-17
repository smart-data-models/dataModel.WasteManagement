<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 폐기물 컨테이너 모델    
================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainerModel/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
전역 설명: **컨테이너 클래스의 정적 속성을 캡처하는 폐기물 컨테이너 모델**입니다.    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `alternateName[string]`: 이 항목의 대체 이름  - `annotations[array]`: 항목에 대한 주석  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: 브랜드 이름  . Model: [https://schema.org/brand](https://schema.org/brand)- `cargoVolume[number]`: 컨테이너에 담을 수 있는 총 용량  . Model: [https://schema.org/cargoVolume](https://schema.org/cargoVolume)- `category[array]`: 컨테이너의 카테고리. 열거형:'쓰레기통, 쓰레기통, 휠리빈, 기타'. 쓰레기통 . 참조 [https://en.wikipedia.org/wiki/Dumpster](https://en.wikipedia.org/wiki/Dumpster)  - `color[string]`: 제품의 색상  . Model: [https://schema.org/color](https://schema.org/color)- `compliantWith[array]`: 컨테이너가 준수하는 표준 목록(예: UNE-EN 840-2:2013).  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `depth[number]`: 컨테이너의 깊이  . Model: [https://schema.org/depth](https://schema.org/depth)- `description[string]`: 이 항목에 대한 설명  - `features[array]`: 컨테이너 기능 목록입니다. Enum:'바퀴, 뚜껑, 둥근 뚜껑, 삽입 구멍, 잠금 가능'. 애플리케이션에 의미 있는 기타 값  - `height[number]`: 컨테이너 높이  . Model: [https://schema.org/heigth](https://schema.org/heigth)- `id[*]`: 엔티티의 고유 식별자  - `image[uri]`: 항목 이미지  . Model: [https://schema.org/URL](https://schema.org/URL)- `insertHolesNumber[number]`: 컨테이너에 있는 삽입 구멍의 수  . Model: [https://schema.org/Number](https://schema.org/Number)- `madeOf[string]`: 컨테이너의 재질. Enum:'플라스틱 , 나무, 금속, 기타 '  - `madeOfCode[string]`: 표준 표에 따른 머티리얼 코드.  - `manufacturerName[string]`: 제조업체 이름.  - `maximumLoad[number]`: 컨테이너가 안전하게 보관할 수 있는 최대 적재량입니다. 단위:'킬로그램'  . Model: [https://schema.org/Number](https://schema.org/Number)- `modelName[string]`: 제조업체에서 제공한 모델 이름입니다. 이 속성은 일반적으로 지자체에서 부여하는 코드명인 이름과는 다릅니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `recommendedLoad[number]`: 컨테이너에 대한 제조업체 권장 적재량입니다. 단위:'킬로그램'  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 엔티티 유형: 폐기물 컨테이너 모델이어야 합니다.  - `weight[number]`: 컨테이너 무게  . Model: [https://schema.org/weigth](https://schema.org/weigth)- `width[number]`: 컨테이너 너비  . Model: [https://schema.org/width](https://schema.org/width)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
WasteContainerModel:      
  description: A model of waste container which captures the static properties of a class of containers.      
  properties:      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    annotations:      
      description: Annotations about the item      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    brandName:      
      description: Name of the brand      
      type: string      
      x-ngsi:      
        model: https://schema.org/brand      
        type: Property      
    cargoVolume:      
      description: Total volume the container can hold      
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
      description: The color of the product      
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
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    depth:      
      description: Depth of the container      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/depth      
        type: Property      
        units: Meters      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    features:      
      description: 'A list of container features. Enum:''wheels, lid, roundedLid, insertHoles, lockable''. Any other value meaningful for the application'      
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
      description: Height of the container      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/heigth      
        type: Property      
        units: Meters      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    image:      
      description: An image of the item      
      format: uri      
      type: string      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Property      
    insertHolesNumber:      
      description: Number of insert holes the container has      
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
      description: Name of the model as given by the manufacturer. This attribute is different than name which is just a codename usually given by municipalities      
      type: string      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
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
      description: list of uri pointing to additional resources about the item      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
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
      description: Weight of the container      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/weigth      
        type: Property      
        units: Kilograms      
    width:      
      description: Width of the container      
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
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.WasteManagement/blob/master/WasteContainerModel/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.WasteManagement/WasteContainerModel/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### 폐기물 컨테이너 모델 NGSI-v2 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 WasteContainerModel의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
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
  "compliantWith": [  
    "UNE-EN 840-2:2013"  
  ],  
  "madeOf": "plastic",  
  "features": [  
    "wheels",  
    "lid"  
  ],  
  "category": [  
    "dumpster"  
  ]  
}  
```  
</details>    
#### WasteContainerModel NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 WasteContainerModel의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "wastecontainermodel:c1",  
  "type": "WasteContainerModel",  
  "category": {  
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
    "value": [  
      "wheels",  
      "lid"  
    ]  
  }  
}  
```  
</details>    
#### 폐기물 컨테이너 모델 NGSI-LD 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 WasteContainerModel의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:WasteContainerModel:wastecontainermodel:c1",  
  "type": "WasteContainerModel",  
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
  "madeOf": "plastic",  
  "modelName": "C1",  
  "name": "Dumpster_Brute_2009_Plastic_Green",  
  "width": 0.5,  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteManagement/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### WasteContainerModel NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 WasteContainerModel의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:WasteContainerModel:wastecontainermodel:c1",  
  "type": "WasteContainerModel",  
  "brandName": {  
    "type": "Property",  
    "value": "Brute"  
  },  
  "cargoVolume": {  
    "type": "Property",  
    "value": 150  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "dumpster"  
    ]  
  },  
  "compliantWith": {  
    "type": "Property",  
    "value": [  
      "UNE-EN 840-2:2013"  
    ]  
  },  
  "depth": {  
    "type": "Property",  
    "value": 0.4  
  },  
  "features": {  
    "type": "Property",  
    "value": [  
      "wheels",  
      "lid"  
    ]  
  },  
  "height": {  
    "type": "Property",  
    "value": 0.8  
  },  
  "madeOf": {  
    "type": "Property",  
    "value": "plastic"  
  },  
  "modelName": {  
    "type": "Property",  
    "value": "C1"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Dumpster_Brute_2009_Plastic_Green"  
  },  
  "width": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteManagement/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
