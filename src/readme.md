
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ${模版名称}` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

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

ModelScope应用(fc3.0)

</description>

<codeUrl>

- [:smiley_cat: 代码](https://github.com/devsapp/start-modelscope/tree/v3)

</codeUrl>
<preview>

- [:eyes: 预览](https://github.com/devsapp/start-modelscope/tree/v3)

</preview>


## 前期准备

使用该项目，您需要有开通以下服务并拥有对应权限：

<service>



| 服务/业务 |  权限  | 相关文档 |
| --- |  --- | --- |
| 函数计算 |  创建函数 | [帮助文档](https://help.aliyun.com/product/2508973.html) [计费文档](https://help.aliyun.com/document_detail/2512928.html) |

</service>

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
  - 初始化项目：`s init start-modelscope-v3 -d start-modelscope-v3`
  - 进入项目，并进行项目部署：`cd start-modelscope-v3 && s deploy -y`
   
</deploy>

## 案例介绍

<appdetail id="flushContent">

本案例支持将魔搭社区的各种开源模型，快速部署到阿里云函数计算FC，并提供相应的推理API服务。

魔搭社区是一个开源的模型部署平台，旨在为开发者提供便捷、高效的模型部署解决方案。该社区整合了各类机器学习和深度学习模型部署的最佳实践，为开发者提供了一个共享、学习和交流的平台。在魔搭社区，开发者可以利用提供的一键部署功能，轻松将他们的模型部署到云端，无需繁琐的配置和复杂的命令。该平台支持多种类型的模型，包括但不限于机器学习、深度学习、自然语言处理和计算机视觉模型等，满足了开发者的各种需求。

* a). 支持模型种类：魔搭社区可通过SwingDeploy快速部署的模型，均可通过本案例进行快速部署。
    * ![图片alt](https://img.alicdn.com/imgextra/i2/O1CN01UslwQu1pYt0OHARiP_!!6000000005373-0-tps-3246-1122.jpg)

* b). 魔搭SwingDeploy For FC说明文档：https://www.modelscope.cn/docs/%E9%83%A8%E7%BD%B2FC

将魔搭模型部署至函数计算Serverless GPU具有以下优势：

* a). 成本效益： Serverless 架构使得资源利用更加灵活，可以根据需求动态分配和释放资源，从而降低成本。利用 Serverless GPU，开发者可以根据实际需要分配 GPU 资源，而不必一直支付固定的 GPU 租用费用。

* b). 弹性扩展： 在需求量增加时，Serverless GPU 能够自动扩展以满足更高的负载，而不会因为硬件限制导致性能瓶颈。这种弹性扩展使得系统能够更好地应对突发流量和高负载情况。

* c). 简化管理： 使用 Serverless GPU，开发者无需关心底层硬件和软件的管理维护工作，如服务器配置、操作系统更新等。平台提供商负责管理基础设施，开发者只需专注于模型开发和部署。

* d). 高可用性： Serverless GPU 架构通常具有高可用性，因为服务商会自动处理故障转移和容错机制。这样可以确保模型服务的持续可用性，提高系统稳定性和可靠性。

* e). 灵活部署： Serverless GPU 可以根据应用程序的需求部署到不同的地理位置，以降低延迟和提高性能。同时，也可以轻松地跨多个云平台进行部署，提高了系统的灵活性和可移植性。

综上所述，将魔搭模型部署至 函数计算 GPU 上具有降低成本、弹性扩展、简化管理、高可用性和灵活部署等必要性，可以帮助开发者更高效地部署和管理模型服务。



</appdetail>

## 使用流程

<usedetail id="flushContent">

[ModelScope一键部署模型：新手村实操FAQ篇](https://developer.aliyun.com/article/1307460?spm=5176.28261954.J_7341193060.1.43f42fdewvfTyq&scm=20140722.S_community@@%E6%96%87%E7%AB%A0@@1307460._.ID_1307460-RL_%E9%AD%94%E6%90%AD%20%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2-LOC_search~UND~community~UND~item-OR_ser-V_3-P0_0)

</usedetail>

## 注意事项

<matters id="flushContent">
</matters>


<devgroup>


## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">  

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <center>微信公众号：`serverless`</center>                                                                                         | <center>微信小助手：`xiaojiangwh`</center>                                                                                        | <center>钉钉交流群：`33947367`</center>                                                                                           |
</p>
</devgroup>
