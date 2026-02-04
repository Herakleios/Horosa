---
title: 星阙app
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.30"

---

# 星阙app

Base URLs:

# Authentication

# 用户

## POST 用户微信登录

POST /user/login/wechat

> Body 请求参数

```json
{
  "code": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» code|body|string| 是 | 微信获取code|none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|

## POST 用户详情

POST /user/info

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "id": "string",
    "avatar": "string",
    "name": "string",
    "sex": 0,
    "birthday": "string",
    "residence_province_id": 0,
    "residence_city_id": "string",
    "residence_district_id": "string",
    "birth_province_id": "string",
    "birth_city_id": "string",
    "birth_district_id": "string"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|
|»» id|string|true|none|id|ID 编号|
|»» avatar|string|true|none|头像|none|
|»» name|string|true|none|昵称|none|
|»» sex|integer|true|none|性别|1 男 2 女  0 未定义|
|»» birthday|string|true|none|生日|none|
|»» residence_province_id|integer|true|none|现居住省id|none|
|»» residence_city_id|string|true|none|现居住市id|none|
|»» residence_district_id|string|true|none|现居住区id|none|
|»» birth_province_id|string|true|none|出生省id|none|
|»» birth_city_id|string|true|none|出生城市id|none|
|»» birth_district_id|string|true|none|出生区id|none|

## POST 用户详情 Copy

POST /user/cancel_user

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|

## POST 修改用户信息

POST /user/modify

> Body 请求参数

```json
{
  "id": "string",
  "avatar": "string",
  "name": "string",
  "sex": 0,
  "birthday": "string",
  "residence_province_id": 0,
  "residence_city_id": "string",
  "residence_district_id": "string",
  "birth_province_id": "string",
  "birth_city_id": "string",
  "birth_district_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» id|body|string| 是 ||none|
|» avatar|body|string| 是 ||none|
|» name|body|string| 是 ||none|
|» sex|body|integer| 是 ||none|
|» birthday|body|string| 是 ||none|
|» residence_province_id|body|integer| 是 ||none|
|» residence_city_id|body|string| 是 ||none|
|» residence_district_id|body|string| 是 ||none|
|» birth_province_id|body|string| 是 ||none|
|» birth_city_id|body|string| 是 ||none|
|» birth_district_id|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|

## POST 提交用户建议

POST /user/suggest

> Body 请求参数

```json
{
  "content": "string",
  "images": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» content|body|string| 是 ||none|
|» images|body|string| 否 ||暂时不传|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|

## POST 上报用户行为

POST /user/behavior

> Body 请求参数

```json
{
  "module": "trigram",
  "operate": "open"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» module|body|string| 是 | 模块|none|
|» operate|body|string| 是 | 操作|none|

#### 枚举值

|属性|值|
|---|---|
|» module|trigram|
|» module|app|
|» operate|open|
|» operate|sixline|
|» operate|bazi|
|» operate|qimen|
|» operate|liuren|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|

## POST 用户登录

POST /user/login

> Body 请求参数

```json
{
  "username": "11111",
  "password": "1s414fg"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» username|body|string| 是 ||none|
|» password|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "token": "string"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» token|string|true|none||none|

## POST 用户注册

POST /user/register

> Body 请求参数

```json
{
  "username": "11111",
  "password": "1s414fg",
  "confirm_password": "1s414fg"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» username|body|string| 是 ||none|
|» password|body|string| 是 ||none|
|» confirm_password|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|

# 玄学

## POST 六爻

POST /trigram/sixline

> Body 请求参数

```json
{
  "gua_type": 1,
  "lines": "876797",
  "hseb": {
    "day": "丙子"
  },
  "gua_time": {
    "year": 2024,
    "month": 9,
    "day": 14,
    "hour": 3,
    "minute": 47
  }
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» gua_type|body|integer| 是 | 起卦类型|1 指定卦  2 时间起卦  3 梅花卦|
|» lines|body|string| 是 | 卦值|示例：987678   6 老阴  7 少阳  8 少阴 9老阳|
|» hseb|body|object| 是 | 干支信息|none|
|»» year|body|string| 是 ||丙子|
|»» month|body|string| 是 ||甲午|
|»» day|body|string| 是 ||none|
|»» hour|body|string| 是 ||none|
|» gua_time|body|object| 是 | 起卦时间|none|
|»» year|body|integer| 是 | 年|none|
|»» month|body|integer| 是 | 月|none|
|»» day|body|integer| 是 | 日|none|
|»» hour|body|integer| 是 | 时|none|
|»» minute|body|integer| 是 | 分|none|
|» address|body|string| 是 | 地址|none|
|» question|body|string| 是 | 问题|none|
|» country|body|string| 是 | 国家|none|
|» input_key|body|string| 是 | 请求MD5|none|
|» is_save|body|integer| 是 | 是否保存|1 是 2 否|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "record_id": 22,
    "gua": {
      "gong": "离宫",
      "ying": 0,
      "gua": "游魂",
      "dizhi": [
        "寅",
        "辰",
        "午",
        "午",
        "申",
        "戌"
      ],
      "shi": 3,
      "liuqin": [
        "父",
        "子",
        "兄",
        "兄",
        "妻",
        "子"
      ],
      "liushou": [
        "雀",
        "陈",
        "蛇",
        "虎",
        "武",
        "龙"
      ],
      "name": "天水讼",
      "tiangan": [
        "戊",
        "戊",
        "戊",
        "壬",
        "壬",
        "壬"
      ],
      "fushen": [
        {
          "name": "官己亥",
          "index": 2
        }
      ],
      "he": "",
      "value": "876797"
    },
    "change_gua": {
      "gong": "离宫",
      "ying": 1,
      "gua": "二世",
      "dizhi": [
        "丑",
        "亥",
        "酉",
        "酉",
        "未",
        "巳"
      ],
      "shi": 4,
      "liuqin": [
        "子",
        "官",
        "妻",
        "妻",
        "子",
        "兄"
      ],
      "liushou": [
        "雀",
        "陈",
        "蛇",
        "虎",
        "武",
        "龙"
      ],
      "name": "火风鼎",
      "tiangan": [
        "辛",
        "辛",
        "辛",
        "己",
        "己",
        "己"
      ],
      "fushen": [
        {
          "name": "父己卯",
          "index": 0
        }
      ],
      "he": "",
      "value": "877787"
    }
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» record_id|integer|true|none|记录id|none|
|»» gua|object|true|none|主卦|none|
|»»» gua|string|true|none|卦名|none|
|»»» name|string|true|none|卦|none|
|»»» gong|string|true|none|卦宫|none|
|»»» ying|integer|true|none|应所在位置|none|
|»»» shi|integer|true|none|世所在位置|none|
|»»» dizhi|[string]|true|none|地址|none|
|»»» liuqin|[string]|true|none|六亲|none|
|»»» liushou|[string]|true|none|六兽|none|
|»»» tiangan|[string]|true|none|天干|none|
|»»» fushen|[object]|true|none|伏神|none|
|»»»» name|string|false|none|伏神名称|none|
|»»»» index|integer|false|none|伏神所在位置|none|
|»»» he|string|true|none|六冲 六合|none|
|»»» value|string|true|none|卦的值|none|
|»» change_gua|object|true|none|变卦|none|
|»»» gong|string|true|none||none|
|»»» ying|integer|true|none||none|
|»»» gua|string|true|none||none|
|»»» dizhi|[string]|true|none||none|
|»»» shi|integer|true|none||none|
|»»» liuqin|[string]|true|none||none|
|»»» liushou|[string]|true|none||none|
|»»» name|string|true|none||none|
|»»» tiangan|[string]|true|none||none|
|»»» fushen|[object]|true|none||none|
|»»»» name|string|false|none||none|
|»»»» index|integer|false|none||none|
|»»» he|string|true|none||none|
|»»» value|string|true|none||none|

## POST 六壬

POST /trigram/liuren

> Body 请求参数

```json
{
  "gua_type": 1,
  "hseb": {
    "day": "丙辰",
    "hour": "丙申"
  },
  "gua_time": {
    "year": 2024,
    "month": 11,
    "day": 14,
    "hour": 3,
    "minute": 47
  },
  "jieqi": "立秋",
  "month": "六"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» gua_type|body|integer| 是 | 卦排盘|1 横排 2 三宫|
|» hseb|body|object| 是 | 天干地支|none|
|»» day|body|string| 是 | 日|none|
|»» hour|body|string| 是 | 时|none|
|» jieqi|body|string| 是 | 节气|none|
|» month|body|string| 是 | 农历月份|none|
|» address|body|string| 是 | 地址|none|
|» question|body|string| 是 | 问题|none|
|» country|body|string| 是 | 国家|none|
|» hour_num|body|integer| 是 | 活时|数字|
|» gua_time|body|[string]| 是 ||none|
|» input_key|body|string| 是 | 请求MD5|none|
|» is_save|body|string| 是 | 是否保存|1 是  2 否|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "sanchuan": {
      "1": "子空丑雀",
      "2": "官癸亥贵",
      "3": "财辛酉阴"
    },
    "tianpan": {
      "申": "午",
      "酉": "未",
      "戌": "申",
      "亥": "酉",
      "子": "戌",
      "丑": "亥",
      "寅": "子",
      "卯": "丑",
      "辰": "寅",
      "巳": "卯",
      "午": "辰",
      "未": "巳"
    },
    "record_id": 24,
    "sike": {
      "1": "勾卯丙",
      "2": "雀丑卯",
      "3": "合寅辰",
      "4": "蛇子寅"
    },
    "yuejiang": "午",
    "geju": [
      "贼克",
      "重审"
    ],
    "dipan": {
      "天盘": [
        "午",
        "未",
        "申",
        "酉",
        "戌",
        "亥",
        "子",
        "丑",
        "寅",
        "卯",
        "辰",
        "巳"
      ],
      "地盘": [
        "申",
        "酉",
        "戌",
        "亥",
        "子",
        "丑",
        "寅",
        "卯",
        "辰",
        "巳",
        "午",
        "未"
      ],
      "天将": [
        "虎",
        "常",
        "玄",
        "阴",
        "后",
        "贵",
        "蛇",
        "雀",
        "合",
        "勾",
        "龙",
        "空"
      ]
    },
    "tianjiang": {
      "申": "虎",
      "酉": "常",
      "戌": "玄",
      "亥": "阴",
      "子": "后",
      "丑": "贵",
      "寅": "蛇",
      "卯": "雀",
      "辰": "合",
      "巳": "勾",
      "午": "龙",
      "未": "空"
    }
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» sanchuan|object|true|none|四传|none|
|»»» 1|string|true|none||none|
|»»» 2|string|true|none||none|
|»»» 3|string|true|none||none|
|»» tianpan|object|true|none|天盘|none|
|»»» 申|string|true|none||none|
|»»» 酉|string|true|none||none|
|»»» 戌|string|true|none||none|
|»»» 亥|string|true|none||none|
|»»» 子|string|true|none||none|
|»»» 丑|string|true|none||none|
|»»» 寅|string|true|none||none|
|»»» 卯|string|true|none||none|
|»»» 辰|string|true|none||none|
|»»» 巳|string|true|none||none|
|»»» 午|string|true|none||none|
|»»» 未|string|true|none||none|
|»» record_id|integer|true|none|记录id|none|
|»» sike|object|true|none|四课|none|
|»»» 1|string|true|none||none|
|»»» 2|string|true|none||none|
|»»» 3|string|true|none||none|
|»»» 4|string|true|none||none|
|»» yuejiang|string|true|none|月将|none|
|»» geju|[string]|true|none|格局|none|
|»» dipan|object|true|none|地盘|none|
|»»» 天盘|[string]|true|none||none|
|»»» 地盘|[string]|true|none||none|
|»»» 天将|[string]|true|none||none|
|»» tianjiang|object|true|none|天将|none|
|»»» 申|string|true|none||none|
|»»» 酉|string|true|none||none|
|»»» 戌|string|true|none||none|
|»»» 亥|string|true|none||none|
|»»» 子|string|true|none||none|
|»»» 丑|string|true|none||none|
|»»» 寅|string|true|none||none|
|»»» 卯|string|true|none||none|
|»»» 辰|string|true|none||none|
|»»» 巳|string|true|none||none|
|»»» 午|string|true|none||none|
|»»» 未|string|true|none||none|

## POST 奇门

POST /trigram/qimen

> Body 请求参数

```json
{
  "gua_type": 1,
  "gua_time": {
    "year": 2024,
    "month": 5,
    "day": 7,
    "hour": 15,
    "minute": 14
  },
  "jieqi": "大暑",
  "month": "七"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» gua_type|body|integer| 是 | 起卦方式|1 拆补  2 置润|
|» gua_time|body|object| 是 | 时间|none|
|»» year|body|integer| 是 ||none|
|»» month|body|integer| 是 ||none|
|»» day|body|integer| 是 ||none|
|»» hour|body|integer| 是 ||none|
|»» minute|body|integer| 是 ||none|
|» address|body|string| 是 | 地址|none|
|» question|body|string| 是 | 问题|none|
|» country|body|string| 是 | 国家|none|
|» input_key|body|string| 是 | 请求MD5|none|
|» is_save|body|string| 是 | 是否保存|1 是   2 否|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|

## POST 手动增加/修改记录

POST /trigram/add_record

> Body 请求参数

```json
{
  "input": {},
  "output": {},
  "extras": {},
  "type": 0,
  "input_key": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» input|body|object| 是 | 输入信息|none|
|» output|body|object| 是 | 输出信息|none|
|» extras|body|object| 是 ||none|
|» type|body|integer| 是 | 类型|1八字 2 六爻 3 六壬 4 奇门|
|» input_key|body|string| 是 | 请求MD5|none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|

## POST 起卦记录-档案

POST /trigram/record_list

> Body 请求参数

```json
{
  "page": 0,
  "page_size": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» page|body|integer| 是 ||none|
|» page_size|body|integer| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "total": "string",
    "data": {
      "type": 0,
      "input": {},
      "output": {},
      "extras": {},
      "id": 0,
      "save_type": 0
    }
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|
|»» total|string|true|none||none|
|»» data|object|true|none||none|
|»»» type|integer|true|none|类型|1八字 2 六爻 3 六壬 4 奇门|
|»»» input|object|true|none|用户输入信息|none|
|»»» output|object|true|none|输出结果信息|none|
|»»» extras|object|true|none|其他配置|none|
|»»» id|integer|true|none||ID 编号|
|»»» save_type|integer|true|none||1 自动  2 手动|

## POST 首页金刚区

POST /trigram/quick_link

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": [
    {
      "id": "string",
      "name": "string",
      "logo": "string",
      "ident": "string"
    }
  ]
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|[object]|false|none||none|
|»» id|string|true|none||none|
|»» name|string|true|none||none|
|»» logo|string|true|none||none|
|»» ident|string|true|none|标识|none|

## POST 删除档案记录

POST /trigram/del_record

> Body 请求参数

```json
{
  "id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» id|body|integer| 是 ||ID 编号|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|

# 起卦簿

## POST 起卦簿列表

POST /trigram_book/list

> 返回示例

> 200 Response

```json
{
  "code": 6,
  "msg": "sunt Excepteur",
  "data": {
    "total": 1,
    "data": [
      {
        "id": "79",
        "avatar": "http://dummyimage.com/100x100",
        "name": "百参交委观选前",
        "sex": 9,
        "birthday": "1985-12-30",
        "residence_province_id": 45,
        "residence_city_id": "51",
        "residence_district_id": "41",
        "birth_province_id": "7",
        "birth_city_id": "7",
        "birth_district_id": "44"
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» total|integer|true|none||none|
|»» data|[object]|true|none||none|
|»»» id|string|false|none||none|
|»»» name|string|false|none||none|
|»»» sex|integer|false|none||none|
|»»» birthday|string|false|none||none|
|»»» residence_province_id|integer|false|none|现居住省id|none|
|»»» residence_city_id|string|false|none|现居住市id|none|
|»»» residence_district_id|string|false|none|现居住区id|none|
|»»» birth_province_id|string|false|none|出生省id|none|
|»»» birth_city_id|string|false|none|出生城市id|none|
|»»» birth_district_id|string|false|none|出生区id|none|
|»»» relation|string|true|none|关系|none|

## POST 修改起卦人

POST /trigram_book/modify

> Body 请求参数

```json
{
  "id": "string",
  "avatar": "string",
  "name": "string",
  "sex": 0,
  "birthday": "string",
  "residence_province_id": 0,
  "residence_city_id": "string",
  "residence_district_id": "string",
  "birth_province_id": "string",
  "birth_city_id": "string",
  "birth_district_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» id|body|string| 是 ||none|
|» name|body|string| 是 ||none|
|» sex|body|integer| 是 ||none|
|» birthday|body|string| 是 ||none|
|» residence_province_id|body|integer| 是 ||none|
|» residence_city_id|body|string| 是 ||none|
|» residence_district_id|body|string| 是 ||none|
|» birth_province_id|body|string| 是 ||none|
|» birth_city_id|body|string| 是 ||none|
|» birth_district_id|body|string| 是 ||none|
|» relation|body|string| 是 | 关系|none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|

## POST 添加 起卦人

POST /trigram_book/add

> Body 请求参数

```json
{
  "id": "string",
  "avatar": "string",
  "name": "string",
  "sex": 0,
  "birthday": "string",
  "residence_province_id": 0,
  "residence_city_id": "string",
  "residence_district_id": "string",
  "birth_province_id": "string",
  "birth_city_id": "string",
  "birth_district_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» name|body|string| 是 ||none|
|» sex|body|integer| 是 ||none|
|» birthday|body|string| 是 ||none|
|» residence_province_id|body|integer| 是 ||none|
|» residence_city_id|body|string| 是 ||none|
|» residence_district_id|body|string| 是 ||none|
|» birth_province_id|body|string| 是 ||none|
|» birth_city_id|body|string| 是 ||none|
|» birth_district_id|body|string| 是 ||none|
|» relation|body|string| 是 | 关系|none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|

## POST 删除信息

POST /trigram_book/del

> Body 请求参数

```json
{
  "id": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» id|body|integer| 是 ||ID 编号|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|

# 后台

## POST 登录

POST /admin/user/login

> Body 请求参数

```json
{
  "username": "string",
  "password": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» username|body|string| 是 ||none|
|» password|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "token": "string"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|
|»» token|string|true|none||none|

## POST 用户列表

POST /admin/consumer/list

> Body 请求参数

```json
{
  "page": 0,
  "page_size": 0
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» page|body|integer| 是 ||none|
|» page_size|body|integer| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "total": 0,
    "data": [
      {
        "id": 0,
        "avatar": "string",
        "name": "string",
        "sex": 0,
        "birthday": "string",
        "residence_province_id": 0,
        "residence_city_id": 0,
        "residence_district_id": 0,
        "birth_province_id": 0,
        "birth_city_id": 0,
        "birth_district_id": 0,
        "wx_openid": "string",
        "wx_unionid": "string",
        "status": 0,
        "create_time": "string",
        "modified_time": "string"
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» total|integer|true|none||none|
|»» data|[object]|true|none||none|
|»»» id|integer|false|none||none|
|»»» avatar|string|false|none||none|
|»»» name|string|false|none||none|
|»»» sex|integer|false|none||none|
|»»» birthday|string|false|none||none|
|»»» residence_province_id|integer|false|none||none|
|»»» residence_city_id|integer|false|none||none|
|»»» residence_district_id|integer|false|none||none|
|»»» birth_province_id|integer|false|none||none|
|»»» birth_city_id|integer|false|none||none|
|»»» birth_district_id|integer|false|none||none|
|»»» wx_openid|string|false|none||none|
|»»» wx_unionid|string|false|none||none|
|»»» status|integer|false|none||none|
|»»» create_time|string|false|none||none|
|»»» modified_time|string|false|none||none|

## POST 用户反馈列表

POST /admin/suggest/list

> Body 请求参数

```json
{
  "page": "string",
  "page_size": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» page|body|string| 是 ||none|
|» page_size|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "total": 0,
    "data": [
      {
        "id": 0,
        "user_id": 0,
        "content": "string",
        "name": "string",
        "status": 0,
        "create_time": "string",
        "modified_time": "string"
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» total|integer|true|none||none|
|»» data|[object]|true|none||none|
|»»» id|integer|false|none||none|
|»»» user_id|integer|false|none||none|
|»»» content|string|false|none|内容|none|
|»»» name|string|false|none|姓名|none|
|»»» status|integer|false|none||none|
|»»» create_time|string|false|none||none|
|»»» modified_time|string|false|none||none|

## POST 金刚区列表

POST /admin/quick_link/list

> Body 请求参数

```json
{}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "success",
  "data": [
    {
      "id": 1,
      "name": "八字",
      "sort": 1,
      "ident": "bazi",
      "status": 1,
      "create_time": "2024-09-03T17:31:29.000+00:00",
      "modified_time": "2024-09-03T17:31:29.000+00:00",
      "logo": "1"
    },
    {
      "id": 2,
      "name": "六爻",
      "sort": 2,
      "ident": "liuyao",
      "status": 1,
      "create_time": "2024-09-03T17:31:39.000+00:00",
      "modified_time": "2024-09-03T17:31:39.000+00:00",
      "logo": "2"
    },
    {
      "id": 3,
      "name": "奇门",
      "sort": 3,
      "ident": "qimen",
      "status": 1,
      "create_time": "2024-09-03T17:31:51.000+00:00",
      "modified_time": "2024-09-03T17:31:51.000+00:00",
      "logo": "3"
    },
    {
      "id": 4,
      "name": "六壬",
      "sort": 4,
      "ident": "liuren",
      "status": 1,
      "create_time": "2024-09-03T17:32:03.000+00:00",
      "modified_time": "2024-09-03T17:32:03.000+00:00",
      "logo": "4"
    }
  ]
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|[object]|true|none||none|
|»» id|integer|true|none||none|
|»» name|string|true|none||none|
|»» sort|integer|true|none||none|
|»» ident|string|true|none||none|
|»» status|integer|true|none||none|
|»» create_time|string|true|none||none|
|»» modified_time|string|true|none||none|
|»» logo|string|true|none||none|

## POST 修改金刚区

POST /admin/quick_link/modify

> Body 请求参数

```json
{
  "id": 1,
  "name": "八字",
  "sort": 1
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» id|body|integer| 是 ||none|
|» name|body|string| 是 ||none|
|» sort|body|integer| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|

## POST 工具使用情况

POST /admin/data/tools_use

> Body 请求参数

```json
{
  "start_time": "2024-05-01 23:59:59",
  "end_time": "2024-09-01 23:59:59"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» start_time|body|string| 是 ||none|
|» end_time|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "trigram-bazi": {
      "module": "trigram",
      "operate": "bazi",
      "count": 1
    },
    "trigram-liuyao": {
      "module": "trigram",
      "operate": "liuyao",
      "count": 1
    },
    "trigram-qimen": {
      "module": "trigram",
      "operate": "qimen",
      "count": 11
    },
    "trigram-liuren": {
      "module": "trigram",
      "operate": "liuren",
      "count": 67
    }
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» trigram-bazi|object|true|none||none|
|»»» module|string|true|none||none|
|»»» operate|string|true|none||none|
|»»» count|integer|true|none||none|
|»» trigram-liuyao|object|true|none||none|
|»»» module|string|true|none||none|
|»»» operate|string|true|none||none|
|»»» count|integer|true|none||none|
|»» trigram-qimen|object|true|none||none|
|»»» module|string|true|none||none|
|»»» operate|string|true|none||none|
|»»» count|integer|true|none||none|
|»» trigram-liuren|object|true|none||none|
|»»» module|string|true|none||none|
|»»» operate|string|true|none||none|
|»»» count|integer|true|none||none|

## POST 用户活跃情况

POST /admin/data/app_user

> Body 请求参数

```json
{
  "start_time": "2024-05-01 23:59:59",
  "end_time": "2024-09-01 23:59:59"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» start_time|body|string| 是 ||none|
|» end_time|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "code": 96,
  "msg": "cillum ea do culpa",
  "data": {
    "addUser": 56,
    "openUser": 31,
    "open": 90,
    "users": 13
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» addUser|integer|true|none|新增用户|none|
|»» openUser|integer|true|none|打开app用户数|none|
|»» open|integer|true|none|打开次数|none|
|»» users|integer|true|none|累计用户|none|

## POST 用户地区情况

POST /admin/data/user_region

> Body 请求参数

```json
{}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "77777777": 0
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» 77777777|number|true|none|省份code|none|

## POST 删除用户建议

POST /admin/suggest/del

> Body 请求参数

```json
{
  "id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» id|body|string| 是 ||ID 编号|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|false|none||none|

# 数据模型

