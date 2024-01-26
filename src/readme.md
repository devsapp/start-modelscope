
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、服务名、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# start-modelscope-v3 帮助文档
<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-modelscope-v3&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-modelscope-v3" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-modelscope-v3&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-modelscope-v3" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-modelscope-v3&type=packageDownload">
  </a>
</p>

<description>

ModelScope应用

</description>

<codeUrl>

- [:smiley_cat: 代码](https://github.com/devsapp/start-modelscope/tree/v3)

</codeUrl>
<preview>

- [:eyes: 预览](https://github.com/devsapp/start-modelscope/tree/v3)

</preview>


## 前期准备

使用该项目，您需要有开通以下服务：

<service>

| 服务 |  备注  |
| --- |  --- |
| 函数计算 FC |  下载并加载模型 |
| 文件存储 NAS |  存储模型，加快模型启动速度 |

</service>

推荐您拥有以下的产品权限 / 策略：
<auth>



| 服务/业务 |  权限 |  备注  |
| --- |  --- |   --- |
| 函数计算 | AliyunFCFullAccess |  需要创建函数资源，通过函数下载及加载模型 |
| NAS | AliyunNASFullAccess |  先将模型从公网下载到NAS，应用启动时加载NAS上的模型使用 |
| VPC | AliyunVPCFullAccess |  使用NAS需要同时使用VPC |

</auth>

<remark>



</remark>

<disclaimers>

免责声明：   
本项目会将模型下载到NAS，并且使用函数计算的GPU实例，模型的大小会影响文件存储占用以及函数执行时间，需根据情况具验证模型下载及加载所产生的费用。

</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-modelscope-v3) ，
  [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-modelscope-v3) 该应用。
   
</appcenter>
<deploy>
    
- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://docs.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init start-modelscope-v3 -d start-modelscope-v3 `
  - 进入项目，并进行项目部署：`cd start-modelscope-v3 && s deploy - y`
   
</deploy>

## 应用详情

<appdetail id="flushContent">
</appdetail>

## 使用文档

<usedetail id="flushContent">
</usedetail>


<devgroup>


## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">  

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <center>微信公众号：`serverless`</center>                                                                                         | <center>微信小助手：`xiaojiangwh`</center>                                                                                        | <center>钉钉交流群：`33947367`</center>                                                                                           |
</p>
</devgroup>
