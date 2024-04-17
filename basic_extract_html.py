from bs4 import BeautifulSoup

html_code = """



<!DOCTYPE HTML>
<!--[if lt IE 7]>      <html lang="en-US"  class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html lang="en-US" class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html lang="en-US" class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html lang="en-US" class="no-js"> <!--<![endif]-->


<head>
	<meta name="localeLanguage" content="en-US"/>
	
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    
    
    <script type="application/ld+json">{"@context":"http://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"item":{"@id":"https://www.colgate.com/en-us","name":"Home"}},{"@type":"ListItem","position":2,"item":{"@id":"https://www.colgate.com/en-us/oral-health","name":"Oral Health, Dental Conditions \u0026 Treatments"}},{"@type":"ListItem","position":3,"item":{"@id":"https://www.colgate.com/en-us/oral-health/cleft-lip-palate","name":"Cleft Lip/Palate"}}]}</script>


	<script type="application/ld+json">{"@context":"http://schema.org","@type":"Article","mainEntityOfPage":{"@type":"WebPage","@id":"https://www.colgate.com/en-us/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth"},"headline":"Cleft Palate And Your Child\u0026#39;s Teeth","image":["https://www.colgate.com/content/dam/cp-sites/oral-care/oral-care-center/global/article/1055622.jpg"],"datePublished":"2023-01-09T21:43:03.968Z","dateModified":"2022-02-10T19:40:01.826Z","author":{"@type":"Organization","name":"Colgate"},"publisher":{"@type":"Organization","name":"Colgate","logo":{"@type":"ImageObject","url":"https://www.colgate.com/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/logos/logo.png"}},"description":"How does a cleft palate affect your child\u0026#39;s oral health? What can you do to take care of their smile? Learn more about oral clefts and teeth, here."}</script>





    <meta name="description" content="How does a cleft palate affect your child&#39;s oral health? What can you do to take care of their smile? Learn more about oral clefts and teeth, here."/>

    <meta name="custom_ranking" data-type="integer" class="swiftype" content="100"/>

    <meta name="occ_type" data-type="string" class="swiftype" content="article"/>

    <meta name="occ_format" data-type="string" class="swiftype" content="article"/>

    <meta name="occ_category" data-type="string" class="swiftype" content="cleft-lip-palate"/>

    <meta name="occ_tag" data-type="string" class="swiftype" content="colgate:article/palate"/>

    <meta name="occ_tag" data-type="string" class="swiftype" content="colgate:article/baby-teeth"/>

    <meta name="occ_tag" data-type="string" class="swiftype" content="colgate:campaign/total-whitening-toothpaste"/>

    <meta name="occ_tag" data-type="string" class="swiftype" content="colgate:campaign/360-floss-tip-powered-sonic-toothbrush"/>

    <meta property="og:image" content="https://www.colgate.com/content/dam/cp-sites/oral-care/oral-care-center/global/article/1055622.jpg"/>

    <meta name="twitter:title" content="Cleft Palate And Your Child&#39;s Teeth | Colgate®"/>

    <meta name="published_date" data-type="date" class="swiftype" content="2022-05-02"/>

    <meta name="title" data-type="string" class="swiftype" content="Cleft Palate And Your Child&#39;s Teeth | Colgate®"/>

    <meta name="twitter:description" content="How does a cleft palate affect your child&#39;s oral health? What can you do to take care of their smile? Learn more about oral clefts and teeth, here."/>

    <meta property="og:title" content="Cleft Palate And Your Child&#39;s Teeth | Colgate®"/>

    <meta name="image" data-type="enum" class="swiftype" content="https://www.colgate.com/content/dam/cp-sites/oral-care/oral-care-center/global/article/1055622.jpg"/>

    <meta property="og:description" content="How does a cleft palate affect your child&#39;s oral health? What can you do to take care of their smile? Learn more about oral clefts and teeth, here."/>

    <meta name="shortDescription" data-type="string" class="swiftype" content="How does a cleft palate affect your child&#39;s oral health? What can you do to take care of their smile? Learn more about oral clefts and teeth, here."/>



	<link rel="alternate" href="https://www.colgate.com/en-ca/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="EN-CA"/>

	<link rel="alternate" href="https://www.colgate.com/es-cr/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ES-CR"/>

	<link rel="alternate" href="https://www.colgate.co.il/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="HE-IL"/>

	<link rel="alternate" href="https://www.colgate.com/en-us/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth" hreflang="EN-US"/>

	<link rel="alternate" href="https://www.colgate.com/es-gt/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth" hreflang="ES-GT"/>

	<link rel="alternate" href="https://www.colgate.com/es-bo/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth" hreflang="ES-BO"/>

	<link rel="alternate" href="https://www.colgate.com/es-ec/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ES-EC"/>

	<link rel="alternate" href="https://www.colgate.com/es-pa/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ES-PA"/>

	<link rel="alternate" href="https://www.colgate.com/es-do/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth" hreflang="ES-DO"/>

	<link rel="alternate" href="https://www.colgate.ru/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="RU-RU"/>

	<link rel="alternate" href="https://www.colgate.ch/fr-ch/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="FR-CH"/>

	<link rel="alternate" href="https://www.colgate.com/es-ar/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ES-AR"/>

	<link rel="alternate" href="https://www.colgate.com/en-za/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="EN-ZA"/>

	<link rel="alternate" href="https://www.colgate.com/es-hn/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ES-HN"/>

	<link rel="alternate" href="https://www.colgate.com.tw/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ZH-TW"/>

	<link rel="alternate" href="https://www.colgate.com.cn/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ZH-CN"/>

	<link rel="alternate" href="https://www.colgate.com/en-sg/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="EN-SG"/>

	<link rel="alternate" href="https://www.colgate.com/es-uy/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ES-UY"/>

	<link rel="alternate" href="https://www.colgate.fr/oral-health/oral-health-and-other-diseases/cleft-palate-and-your-childs-teeth-0613" hreflang="FR-FR"/>

	<link rel="alternate" href="https://www.colgate.com/es-py/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ES-PY"/>

	<link rel="alternate" href="https://www.colgate.com/en-sa/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="EN-SA"/>

	<link rel="alternate" href="https://www.colgate.com/es-cl/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ES-CL"/>

	<link rel="alternate" href="https://www.colgate.by/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="RU-BY"/>

	<link rel="alternate" href="https://www.colgate.com/en-in/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="EN-IN"/>

	<link rel="alternate" href="https://www.colgate.com/en-my/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="EN-MY"/>

	<link rel="alternate" href="https://www.colgate.ie/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="EN-IE"/>

	<link rel="alternate" href="https://www.colgate.com/es-us/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ES-US"/>

	<link rel="alternate" href="https://www.colgate.com/es-pe/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ES-PE"/>

	<link rel="alternate" href="https://www.colgate.com.br/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="PT-BR"/>

	<link rel="alternate" href="https://www.colgate.com/es-sv/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ES-SV"/>

	<link rel="alternate" href="https://www.colgate.com/es-co/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ES-CO"/>

	<link rel="alternate" href="https://www.colgate.com/es-ni/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ES-NI"/>

	<link rel="alternate" href="https://www.colgate.com/es-mx/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="ES-MX"/>

	<link rel="alternate" href="https://www.colgate.com/kz-kz/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="RU-KZ"/>

	<link rel="alternate" href="https://www.colgate.com/en-ph/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth-0613" hreflang="EN-PH"/>




<title>Cleft Palate And Your Child's Teeth | Colgate®</title>


		
<script>
	window.dataLayer = [
  {
    "environmentInformation": {
      "datalayerVersion": "2.0",
      "environment": "production"
    }
  },
  {
    "siteInformation": {
      "audience": "b2c",
      "brand": "Colgate",
      "careCategory": "oral care",
      "careSubCategory": "Oral Care",
      "countryCode": "US",
      "purpose": "brand",
      "region": "North America",
      "siteId": "89D59CC7-B7FC-479E-9F97-4E66F0942721",
      "siteName": "Colgate en-us",
      "domain": "www.colgate.com",
      "platform": "aem",
      "type": "web",
      "productionDate": "2020-10-14",
      "contentPath": "/content/cp-sites/oral-care/oral-care-center/en_us/home/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth",
      "urlPath": "/en-us/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth",
      "platformVersion": "6.5.15.0-SSP1",
      "language": "EN"
    }
  },
  {
    "pageInformation": {
      "phase": "",
      "stage": "",
      "species": "",
      "author": "",
      "topic": "",
      "title": "Cleft Palate And Your Child's Teeth",
      "publicationDate": "",
      "tags": ""
    }
  }
]
</script>
<link rel="canonical" href="https://www.colgate.com/en-us/oral-health/cleft-lip-palate/cleft-palate-and-your-childs-teeth"/>
        <link rel="stylesheet" href="/etc/designs/zg/cpcolgate2020/desktop/css.asset.css/core/design.default.bootstrap.v0-0-1.css"/>
<!--[if lte IE 6]>
		<![endif]-->
	
	<!--[if IE 7]>
		<![endif]-->
	
	<!--[if IE 8]>
		<link rel="stylesheet" href="/etc/designs/zg/cpcolgate2020/desktop/css.fileAsset.css/zg/basic/desktop/css/utils/ie8.v0-0-1.css" />
<![endif]-->
<link rel="shortcut icon" href="/etc/designs/zg/cpcolgate2020/desktop/assets/img/favicon.ico" type="image/x-icon"/>
	<script type="text/javascript" src="/etc/designs/zg/cpcolgate2020/desktop/js.fileAsset.js/zg/cpcolgate2020/desktop/js/head/head.v0-0-1.js"></script>
<style>
		.breadcrumbs-occ-optimization {
    width: 100vw;
    right: 15px;

}







@media screen and (max-width: 1024px) {

  body[class*='whitening-hub'] .breadcrumbs-occ-optimization {

    top: -5px!important;

  }

}

</style>
<link rel="preload" href="/etc/designs/zg/cpcolgate2020/desktop/assets/fonts/ColgateReady/ColgateReadyCyWebRegular/colgatereadycy_web-regular.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="/etc/designs/zg/cpcolgate2020/desktop/assets/fonts/ColgateRelaunchIcons/ColgateRelaunchIcons.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="/etc/designs/zg/cpcolgate2020/desktop/assets/fonts/ColgateReady/ColgateReadyCyWebBold/colgatereadycy_web-bold.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="/etc/designs/zg/cpcolgate2020/desktop/assets/fonts/ColgateReady/ColgateReadyWebBoldItalic/colgate_ready_web-bold_italic.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="/etc/designs/zg/cpcolgate2020/desktop/assets/fonts/materialicons/MaterialIcons-Regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/etc/designs/zg/cpcolgate2020/desktop/assets/fonts/openSans/open-sans-v18-latin_cyrillic-regular.woff2" as="font" type="font/woff2" crossorigin><!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-TRZ4CFM');</script>
<!-- End Google Tag Manager -->

<!-- PR -->
<script type="text/javascript">window.PowerReviewsConfig = { api_key: 'f5dc3d69-3169-493d-93e1-f2ac7ada457f', locale: 'en_US', merchant_group_id: '77811', merchant_id: '748880', review_wrapper_url: '/write-a-review?pageId=___PAGE_ID___'};</script>

<!-- BlueConic Base Script -->
<script src="https://u939.colgate.com/script.js"></script>

<!-- Mopinion Pastea.se  start -->
<script type="text/javascript">(function(){var id="N0WGM6c0tH4Rs3u06LSyezrZEM28wkPfWyNWEq2Z";var js=document.createElement("script");js.setAttribute("type","text/javascript");js.setAttribute("src","//deploy.mopinion.com/js/pastease.js");js.async=true;document.getElementsByTagName("head")[0].appendChild(js);var t=setInterval(function(){try
{Pastease.load(id);clearInterval(t)}
catch(e){}},50)})();</script>
<!-- Mopinion Pastea.se end -->

<script>(window.BOOMR_mq=window.BOOMR_mq||[]).push(["addVar",{"rua.upush":"false","rua.cpush":"false","rua.upre":"false","rua.cpre":"false","rua.uprl":"false","rua.cprl":"false","rua.cprf":"false","rua.trans":"SJ-8b222c2f-a90c-401f-81f9-4c940073b6d0","rua.cook":"false","rua.ims":"false","rua.ufprl":"false","rua.cfprl":"true","rua.isuxp":"false","rua.texp":"norulematch"}]);</script>
                              <script>!function(e){var n="https://s.go-mpulse.net/boomerang/";if("False"=="True")e.BOOMR_config=e.BOOMR_config||{},e.BOOMR_config.PageParams=e.BOOMR_config.PageParams||{},e.BOOMR_config.PageParams.pci=!0,n="https://s2.go-mpulse.net/boomerang/";if(window.BOOMR_API_key="C6K9Z-GK3DW-JVVWU-28XJ9-V3TR5",function(){function e(){if(!o){var e=document.createElement("script");e.id="boomr-scr-as",e.src=window.BOOMR.url,e.async=!0,i.parentNode.appendChild(e),o=!0}}function t(e){o=!0;var n,t,a,r,d=document,O=window;if(window.BOOMR.snippetMethod=e?"if":"i",t=function(e,n){var t=d.createElement("script");t.id=n||"boomr-if-as",t.src=window.BOOMR.url,BOOMR_lstart=(new Date).getTime(),e=e||d.body,e.appendChild(t)},!window.addEventListener&&window.attachEvent&&navigator.userAgent.match(/MSIE [67]\./))return window.BOOMR.snippetMethod="s",void t(i.parentNode,"boomr-async");a=document.createElement("IFRAME"),a.src="about:blank",a.title="",a.role="presentation",a.loading="eager",r=(a.frameElement||a).style,r.width=0,r.height=0,r.border=0,r.display="none",i.parentNode.appendChild(a);try{O=a.contentWindow,d=O.document.open()}catch(_){n=document.domain,a.src="javascript:var d=document.open();d.domain='"+n+"';void(0);",O=a.contentWindow,d=O.document.open()}if(n)d._boomrl=function(){this.domain=n,t()},d.write("<bo"+"dy onload='document._boomrl();'>");else if(O._boomrl=function(){t()},O.addEventListener)O.addEventListener("load",O._boomrl,!1);else if(O.attachEvent)O.attachEvent("onload",O._boomrl);d.close()}function a(e){window.BOOMR_onload=e&&e.timeStamp||(new Date).getTime()}if(!window.BOOMR||!window.BOOMR.version&&!window.BOOMR.snippetExecuted){window.BOOMR=window.BOOMR||{},window.BOOMR.snippetStart=(new Date).getTime(),window.BOOMR.snippetExecuted=!0,window.BOOMR.snippetVersion=12,window.BOOMR.url=n+"C6K9Z-GK3DW-JVVWU-28XJ9-V3TR5";var i=document.currentScript||document.getElementsByTagName("script")[0],o=!1,r=document.createElement("link");if(r.relList&&"function"==typeof r.relList.supports&&r.relList.supports("preload")&&"as"in r)window.BOOMR.snippetMethod="p",r.href=window.BOOMR.url,r.rel="preload",r.as="script",r.addEventListener("load",e),r.addEventListener("error",function(){t(!0)}),setTimeout(function(){if(!o)t(!0)},3e3),BOOMR_lstart=(new Date).getTime(),i.parentNode.appendChild(r);else t(!1);if(window.addEventListener)window.addEventListener("load",a,!1);else if(window.attachEvent)window.attachEvent("onload",a)}}(),"".length>0)if(e&&"performance"in e&&e.performance&&"function"==typeof e.performance.setResourceTimingBufferSize)e.performance.setResourceTimingBufferSize();!function(){if(BOOMR=e.BOOMR||{},BOOMR.plugins=BOOMR.plugins||{},!BOOMR.plugins.AK){var n="true"=="true"?1:0,t="",a="ramph3yx3ckyqzq7edca-f-93ef5edaf-clientnsv4-s.akamaihd.net",i="false"=="true"?2:1,o={"ak.v":"37","ak.cp":"932177","ak.ai":parseInt("586332",10),"ak.ol":"0","ak.cr":10,"ak.ipv":4,"ak.proto":"h2","ak.rid":"175f6f2c","ak.r":43973,"ak.a2":n,"ak.m":"dsca","ak.n":"essl","ak.bpcip":"136.24.243.0","ak.cport":50836,"ak.gh":"23.216.148.136","ak.quicv":"","ak.tlsv":"tls1.3","ak.0rtt":"","ak.csrc":"-","ak.acc":"","ak.t":"1713316036","ak.ak":"hOBiQwZUYzCg5VSAfCLimQ==CefKoJh5/F/CtRNLUlxKc/bW3iztSccG0SIUDdeBrPQVGo5RQuruRYzjlINXEAbrf3KAV/v83463SrCOsYeMeVkkPM1BYnHGjq39AYlrLg/BATSbBkcu2Mrcz6vf1QpYdIkOmRUJf87kEK7tmYCGEEihAll64tVYgqnMPwMieRfo9SXmVWiObTp3n7xgRfNAyUTzhdN1g831YCTKbqPRfH4COrDPh192rd8AfHnBeW/UOrUks1Uy7wOV3tqAAQqZ5785SVCvHXF2nEzgs6p6/x7MmOosUWFWtgbFbpPqHMcjSa7nn/wCqcmnd+zk3fw+TJZI+Xa/F9F+KoYg1nuxMiBNHZGFVf0aWYEdrmCiYznrIu/5iN+/j/fsK2Y5p4kVCCiSEMdDxHwaAMspmFmWA6L5pu0sAjS6pvGcENKdpSY=","ak.pv":"70","ak.dpoabenc":"","ak.tf":i};if(""!==t)o["ak.ruds"]=t;var r={i:!1,av:function(n){var t="http.initiator";if(n&&(!n[t]||"spa_hard"===n[t]))o["ak.feo"]=void 0!==e.aFeoApplied?1:0,BOOMR.addVar(o)},rv:function(){var e=["ak.bpcip","ak.cport","ak.cr","ak.csrc","ak.gh","ak.ipv","ak.m","ak.n","ak.ol","ak.proto","ak.quicv","ak.tlsv","ak.0rtt","ak.r","ak.acc","ak.t","ak.tf"];BOOMR.removeVar(e)}};BOOMR.plugins.AK={akVars:o,akDNSPreFetchDomain:a,init:function(){if(!r.i){var e=BOOMR.subscribe;e("before_beacon",r.av,null,null),e("onbeacon",r.rv,null,null),r.i=!0}return this},is_complete:function(){return!0}}}}()}(window);</script></head>
<body class="page-oral-health page-cleft-lip-palate page-cleft-palate-and-your-childs-teeth  layout-left-rail-2020 template-article-no-amp grid-bootstrap" data-theme-path="/etc/designs/zg/cpcolgate2020/desktop" data-path-id="434c760355f0fa0d7d7b64afdd4d9223">
	<script src="/etc.clientlibs/clientlibs/granite/jquery.min.js"></script>
<script src="/etc.clientlibs/clientlibs/granite/utils.min.js"></script>
<script src="/etc.clientlibs/clientlibs/granite/jquery/granite.min.js"></script>
<script src="/etc.clientlibs/foundation/clientlibs/jquery.min.js"></script>
<script src="/etc.clientlibs/foundation/clientlibs/shared.min.js"></script>
<script src="/etc.clientlibs/cq/personalization/clientlib/underscore.min.js"></script>
<script src="/etc.clientlibs/cq/personalization/clientlib/personalization/kernel.min.js"></script>
<script type="text/javascript">
	$CQ(function() {
		CQ_Analytics.SegmentMgr.loadSegments("/etc/segmentation/contexthub");
	});
</script>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TRZ4CFM"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<!-- Company Schema -->
<script type="application/ld+json">{"@context": "http://schema.org","@type": "Organization","name": "Colgate","description": "Discover the Colgate Oral Care Center. The Oral Care Center provides information on dental health, oral health products, oral health guides, and much more.","url": "https://www.colgate.com/en-us","logo": "https://www.colgate.com/content/dam/cp-sites/oral-care/oral-care-center/global/general/logos/colgate-logo-desktop.png","address": {"streetAddress": "300 Park Avenue","addressLocality": "New York","addressRegion": "NY","postalCode": "10022","addressCountry": "USA"},"telephone": "2123102000","faxNumber": "","sameAs" : ["https://www.facebook.com/Colgate/","https://twitter.com/colgate","","","https://www.youtube.com/channel/UCx-GyWJYwa8CbQ38jH8C3Uw","https://www.linkedin.com/company/colgate-palmolive","https://en.wikipedia.org/wiki/Colgate-Palmolive"]}</script>
<!-- End Company Schema -->

<!-- Sitelink Searchbox Schema -->
<script type="application/ld+json">{"@context": "http://schema.org","@type": "WebSite","url": "https://www.colgate.com/en-us","potentialAction": {"@type": "SearchAction","target": "https://www.colgate.com/en-us/search-results#stq={search_term_string}","query-input": "required name=search_term_string"}}</script>
<!-- End Sitelink Searchbox Schema -->
<style>
.keep-small img {
width: 140px;
}
</style>	
<!--TrustArc Banner DIV -->
<style>
#consent_blackbar {
position:fixed;
bottom:0px;
margin:auto;
padding-left:10%;
padding-right:10%;
z-index:9999999;}
</style>
<div id="consent_blackbar"></div>
<!--End TrustArc Banner DIV -->
<!--
Start of Swaven tag
This tag must be placed between the <body> and </body> tags, as close as possible to the opening tag. Please, do not modify.

-->
<script>
(function(e){try{var a=window.swnDataLayer=window.swnDataLayer||{};a.appId=e||a.appId,a.eventBuffer=a.eventBuffer||[],a.loadBuffer=a.loadBuffer||[],a.push=a.push||function(e){a.eventBuffer.push(e)},a.load=a.load||function(e){a.loadBuffer.push(e)};var t=document.getElementsByTagName("script")[0],n=document.createElement("script");n.async=!0,n.src="//wtb-tag.swaven.com/scripts/"+a.appId+"/tag.min.js",t.parentNode.insertBefore(n,t)}catch(e){console.log(e)}}("6411cc9403641a0e38e15115"));
</script>
<!-- End of Swaven tag -->
<div class="container-fluid"><div class="row"><div id="header" class="col-xs-12"><div class="row"><div class="layout-outer"><div class="layout-inner"><div class="col-xs-12 col-md-12 default-style"><div class="snippetReference component section header-2022 col-xs-12 reference-header header fixed-component" data-id="swiftype" data-swiftype-index="false">
 <div class="inner"> 
  <div class="component-content"> 
   <a id="458709434" style="visibility:hidden" aria-hidden="true"></a> 
   <div class="richText component section skip-navigation-button first odd grid_3"> 
    <div class="component-content"> 
     <div class="richText-content"> 
      <p style="margin: 0;"><a href="#content"><span class="focus-border">Skip Navigation</span></a></p> 
     </div> 
    </div> 
   </div>
   <div class="box component section utility-bar even"> 
     
    <div class="component-content" id="694920745"> 
     <div class="paragraphSystem content"> 
      <a id="832494611" style="visibility:hidden" aria-hidden="true"></a> 
      <div class="richText component section wh-explore-dropdown first odd"> 
       <div class="component-content"> 
        <div class="richText-content"> 
         <div class="dropdown"> 
          <button id="wh-explore-dropdown-button">Explore Colgate.com</button> 
          <ul id="wh-explore-list"> 
           <li><a href="/en-us/oral-health">Oral Health</a></li> 
           <li><a href="/en-us/products">Products</a></li> 
           <li><a href="/en-us/our-mission">About</a></li> 
          </ul> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="box component section utility-links even last"> 
        
       <div class="component-content" id="0385042865"> 
        <div class="paragraphSystem content"> 
         <a id="156788281" style="visibility:hidden" aria-hidden="true"></a> 
         <div class="image component section default-style first odd"> 
          <div class="component-content left"> 
           <div class="analytics-image-tracking"></div> 
           <a href="https://www.colgateprofessional.com/" title="For professionals" target="_blank" rel="noopener noreferrer"><img src="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/header/utility-links/professional.svg" alt="  For professionals icon" title="For professionals icon"> </a> 
          </div> 
         </div> 
         <div class="image component section default-style even"> 
          <div class="component-content left"> 
           <div class="analytics-image-tracking"></div> 
           <a href="/en-us/where-to-buy" title="Where to Buy"><img src="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/header/utility-links/where-to-buy.svg" alt="Where to Buy icon" title="Where to Buy icon"> </a> 
          </div> 
         </div> 
         <div class="image component section default-style odd"> 
          <div class="component-content left"> 
           <div class="analytics-image-tracking"></div> 
           <a href="/en-us/smiles/special-offers" title="Coupons"><img src="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/header/utility-links/offers.svg" alt="Coupons icon" title="Coupons icon"> </a> 
          </div> 
         </div> 
         <div class="image component section default-style even"> 
          <div class="component-content left"> 
           <div class="analytics-image-tracking"></div> 
           <a href="/en-us/contact-us" title="Contact"><img src="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/header/utility-links/contact.svg" alt="Contact icon" title="Contact icon"> </a> 
          </div> 
         </div> 
         <div class="image component section default-style odd"> 
          <div class="component-content left"> 
           <div class="analytics-image-tracking"></div> 
           <a href="#lightbox" title="Sign up"><img src="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/header/utility-links/sign-up.svg" alt="Sign up icon" title="Sign up icon"> </a> 
          </div> 
         </div> 
         <div class="image component section default-style even last"> 
          <div class="component-content left"> 
           <div class="analytics-image-tracking"></div> 
           <a href="/en-us/locations" title="United States (US English)"><img src="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/header/utility-links/location-pin.svg" alt="Location icon" title="Location icon"> </a> 
          </div> 
         </div> 
        </div> 
       </div> 
      </div> 
     </div> 
    </div> 
   </div>
   <div class="box component section main-header odd"> 
     
    <div class="component-content" id="01958346844"> 
     <div class="paragraphSystem content"> 
      <a id="552700558" style="visibility:hidden" aria-hidden="true"></a> 
      <div class="image component section logo first odd grid_4"> 
       <div class="component-content left"> 
        <div class="analytics-image-tracking"></div> 
        <a href="/en-us" title="home"><img src="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/logos/colgate-smile-badge.svg" alt="Colgate® Logo" title="Colgate® Logo"> </a> 
       </div> 
      </div> 
      <div class="image component section wh-logo even"> 
       <div class="component-content left"> 
        <div class="analytics-image-tracking"></div> 
        <a href="/en-us/whitening-hub" title="Whitening Hub Home"><picture><!--[if IE 9]><video style="display: none;"><![endif]-->
 <source srcset="/content/dam/cp-sites/oral-care/oral-care-center/en_us/whitening-hub/wh-logo.png.rendition.157.156.png" media="(max-width: 320px)">
 <source srcset="/content/dam/cp-sites/oral-care/oral-care-center/en_us/whitening-hub/wh-logo.png.rendition.157.156.png" media="(max-width: 767px)">
 <source srcset="/content/dam/cp-sites/oral-care/oral-care-center/en_us/whitening-hub/wh-logo.png.rendition.157.156.png" media="(min-width: 768px) and (max-width: 991px)">
 <source srcset="/content/dam/cp-sites/oral-care/oral-care-center/en_us/whitening-hub/wh-logo.png.rendition.157.156.png" media="(min-width: 992px) and (max-width: 1199px)">
 <source srcset="/content/dam/cp-sites/oral-care/oral-care-center/en_us/whitening-hub/wh-logo.png.rendition.157.156.png" media="(min-width: 1200px) and (max-width: 1920px)"><!--[if IE 9]></video><![endif]-->
 <img src="/content/dam/cp-sites/oral-care/oral-care-center/en_us/whitening-hub/wh-logo.png" alt="Whitening Hub Logo" title="Whitening Hub Logo">
</picture> </a> 
       </div> 
      </div> 
      <div class="richText component section menu-2022 odd"> 
       <div class="component-content"> 
        <div class="richText-content"> 
         <ul class="menu"> 
          <li><button id="oral-health-button" aria-controls="oral-health-submenu" data-path="/oral-health/">Oral Health</button></li> 
          <li><button id="products-button" aria-controls="products-submenu" data-path="/products/">Products</button></li> 
          <li><button id="about-button" aria-controls="about-submenu" data-path="/power-of-optimism/">About</button></li> 
         </ul> 
        </div> 
       </div> 
      </div> 
      <div class="richText component section wh-menu even"> 
       <div class="component-content"> 
        <div class="richText-content"> 
         <p><button class="mobile-menu-button" id="wh-menu-button">Whitening Products</button></p> 
         <div class="menu-items" id="wh-menu"> 
          <p class="landing"><a href="/en-us/whitening-hub">Whitening Solutions</a></p> 
          <div class="products"> 
           <button id="wh-products-button">Whitening Products</button> 
           <ul id="wh-products-list"> 
            <li><a href="/en-us/whitening-hub/products">All Optic White® products</a></li> 
            <li><a href="/en-us/whitening-hub/products/colgate-optic-proseries-toothpaste">Pro Series Toothpaste</a></li> 
            <li><a href="/en-us/whitening-hub/products/colgate-optic-white-comfortfit-led-device">ComfortFit LED Device</a></li> 
            <li><a href="/en-us/whitening-hub/products/colgate-optic-white-overnight-teeth-whitening-pen">Overnight Teeth Whitening Pen</a><br> </li> 
            <li><a href="/en-us/whitening-hub/products/colgate-optic-white-express-teeth-whitening-pen">Express Teeth Whitening Pen</a></li> 
            <li><a href="/en-us/whitening-hub/products/ow-renewal">Renewal Toothpaste</a></li> 
            <li><a href="/en-us/whitening-hub/products/ow-advanced">Advanced Toothpaste</a></li> 
            <li><a href="/en-us/whitening-hub/products/ow-stain-fighter">Stain Fighter® Toothpaste</a></li> 
            <li><a href="/en-us/whitening-hub/products/ow-charcoal">Charcoal Toothpaste</a></li> 
            <li><a href="/en-us/whitening-hub/products/ow-high-impact-white">Whitening Mouthwash</a></li> 
           </ul> 
          </div> 
         </div> 
        </div> 
       </div> 
      </div> 
      <div class="parametrizedhtml component section default-style odd last reference-header-buttons"> 
       <div class="component-content"> 
        <div class="search-box-container" custom-col-size="three-columns" articles-title="Oral Care" more-articles-label="{0} more articles" products-title="Products" more-products-label="{0} more products" no-results="We could not find anything for" another-search="To see more results, try another search term." data-action="/search?cacheclear"> 
         <form role="search"> 
          <div class="search-wrapper"> 
           <span class="icon-search"></span> 
           <label class="searchBox-label" for="site-search">Search Box</label> 
           <input type="text" maxlength="2048" class="search-box" id="site-search" placeholder="Search..." autocomplete="off" aria-label="Search Box"> 
           <div class="action-box"> 
            <button type="reset" class="clear-btn">Clear</button> 
            <button type="submit" class="submit-btn" aria-label="Search"></button> 
           </div> 
          </div> 
          <button class="search-btn" aria-label="Search Box Button"></button> 
         </form> 
         <div class="bg"></div> 
        </div> 
        <button class="menu" aria-label="Menu" aria-expanded="false"></button> 
       </div> 
      </div> 
     </div> 
    </div> 
   </div>
   <div class="richText component section submenu-2022 even"> 
    <div class="component-content"> 
     <div class="richText-content"> 
      <ul class="submenu" id="oral-health-submenu"> 
       <li> 
        <ul class="column"> 
         <li><p class="heading">A - C</p> </li> 
         <li><a href="/en-us/oral-health/adult-orthodontics">Adult Orthodontics (Braces)</a></li> 
         <li><a href="/en-us/oral-health/bad-breath">Bad Breath (Halitosis)</a></li> 
         <li><a href="/en-us/oral-health/bridges-and-crowns">Bridges &amp; Crowns</a></li> 
         <li><a href="/en-us/oral-health/brushing-and-flossing">Brushing &amp; Flossing</a></li> 
         <li><a href="/en-us/oral-health/cavities">Cavities</a></li> 
         <li><a href="/en-us/oral-health/cleft-lip-palate">Cleft Lip /Palate</a></li> 
         <li><a href="/en-us/oral-health/cracked-tooth-syndrome">Cracked Tooth Syndrome</a></li> 
        </ul> </li> 
       <li> 
        <ul class="column"> 
         <li><p class="heading">D - E</p> </li> 
         <li><a href="/en-us/oral-health/dental-emergencies-and-sports-safety">Dental Emergencies &amp; Sports Safety</a></li> 
         <li><a href="/en-us/oral-health/threats-to-dental-health">Dental Health Threats</a></li> 
         <li><a href="/en-us/oral-health/selecting-dental-products">Dental Product Guidance</a></li> 
         <li><a href="/en-us/oral-health/sealants">Dental Sealants</a></li> 
         <li><a href="/en-us/oral-health/dental-visits">Dental Visits</a></li> 
         <li><a href="/en-us/oral-health/dentures">Dentures</a></li> 
         <li><a href="/en-us/oral-health/developmental-disabilities">Developmental Conditions</a></li> 
         <li><a href="/en-us/oral-health/diabetes-and-other-endocrine-disorders">Diabetes &amp; Endocrine Disorders</a></li> 
         <li><a href="/en-us/oral-health/gastrointestinal-disorders">Digestive (Gastrointestinal) Disorders</a></li> 
         <li><a href="/en-us/oral-health/dry-mouth">Dry Mouth</a></li> 
         <li><a href="/en-us/oral-health/early-orthodontics">Early Orthodontics (Braces)</a></li> 
        </ul> </li> 
       <li> 
        <ul class="column"> 
         <li><p class="heading">F - N</p> </li> 
         <li><a href="/en-us/oral-health/fillings">Fillings</a></li> 
         <li><a href="/en-us/oral-health/fluoride">Fluoride</a></li> 
         <li><a href="/en-us/oral-health/gum-disease">Gum Disease (Gingivitis)</a></li> 
         <li><a href="/en-us/oral-health/heart-disease">Heart Disease</a></li> 
         <li><a href="/en-us/oral-health/hiv-aids-and-stds">HIV/AIDS &amp; STDS</a></li> 
         <li><a href="/en-us/oral-health/immune-disorders">Immune Disorders</a></li> 
         <li><a href="/en-us/oral-health/implants">Implants</a></li> 
         <li><a href="/en-us/oral-health/temporomandibular-disorder">Jaw Pain (TMD)</a></li> 
         <li><a href="/en-us/oral-health/mouth-and-teeth-anatomy">Mouth &amp; Teeth Anatomy</a></li> 
         <li><a href="/en-us/oral-health/mouth-sores-and-infections">Mouth Sores &amp; Infections</a></li> 
         <li><a href="/en-us/oral-health/nutrition-and-oral-health">Nutrition &amp; Oral Health</a></li> 
        </ul> </li> 
       <li> 
        <ul class="column"> 
         <li><p class="heading">O - R</p> </li> 
         <li><a href="/en-us/oral-health/cancer">Oral Cancers</a></li> 
         <li><a href="/en-us/oral-health/infant-oral-care">Oral Care: Babies (0-4)</a></li> 
         <li><a href="/en-us/oral-health/kids-oral-care">Oral Care: Kids (5-12)</a></li> 
         <li><a href="/en-us/oral-health/teen-oral-care">Oral Care: Teens (13-17)</a></li> 
         <li><a href="/en-us/oral-health/adult-oral-care">Oral Care: Adults (18+)</a></li> 
         <li><a href="/en-us/oral-health/oral-care-age-55-up">Oral Care: Adults (55+)</a></li> 
         <li><a href="/en-us/oral-health/anesthesia">Pain Management (Anesthesia)</a></li> 
         <li><a href="/en-us/oral-health/plaque-and-tartar">Plaque &amp; Tartar</a></li> 
         <li><a href="/en-us/oral-health/oral-care-during-pregnancy">Pregnancy Oral Care</a></li> 
         <li><a href="/en-us/oral-health/respiratory-conditions">Respiratory Conditions</a></li> 
         <li><a href="/en-us/oral-health/root-canals">Root Canals</a></li> 
        </ul> </li> 
       <li> 
        <ul class="column"> 
         <li><p class="heading">S - Z</p> </li> 
         <li><a href="/en-us/oral-health/special-occasions">Special Occasions</a></li> 
         <li><a href="/en-us/oral-health/bonding">Teeth Bonding</a></li> 
         <li><a href="/en-us/oral-health/bruxism">Teeth Grinding (Bruxism)</a></li> 
         <li><a href="/en-us/oral-health/teeth-whitening">Teeth Whitening</a></li> 
         <li><a href="/en-us/oral-health/tooth-removal">Tooth Extraction</a></li> 
         <li><a href="/en-us/oral-health/tooth-fairy">Tooth Fairy</a></li> 
         <li><a href="/en-us/oral-health/tooth-sensitivity">Tooth Sensitivity</a></li> 
         <li><a href="/en-us/oral-health/veneers">Veneers</a></li> 
         <li><a href="/en-us/oral-health/wisdom-teeth">Wisdom Teeth</a></li> 
         <li><a href="/en-us/oral-health/x-rays">X-Rays</a></li> 
        </ul> </li> 
       <li> 
        <ul class="column"> 
         <li><a href="/en-us/oral-health">View All Article Categories &gt;</a></li> 
        </ul> </li> 
      </ul> 
      <ul class="submenu" id="products-submenu"> 
       <li> 
        <ul class="column"> 
         <li><p class="heading">Types</p> </li> 
         <li><a href="/en-us/products/toothpaste">Toothpastes</a></li> 
         <li><a href="/en-us/products/toothbrush">Toothbrushes</a></li> 
         <li><a href="/en-us/products/mouthwash">Mouthwashes &amp; Rinses</a></li> 
         <li><a href="/en-us/products/prescription-only-products">Prescription Products</a></li> 
         <li><a href="/en-us/products/specialty">Specialty Products</a></li> 
         <li><a href="/en-us/whitening-hub/products">Teeth Whitening Products</a></li> 
         <li><a href="/en-us/products/kids">For Kids</a></li> 
        </ul> </li> 
       <li> 
        <ul class="column"> 
         <li><p class="heading">Brands</p> </li> 
         <li><a href="/en-us/colgate-total">Colgate<sup>®</sup> Total</a></li> 
         <li><a href="/en-us/360">Colgate<sup>®</sup> 360º</a></li> 
         <li><a href="/en-us/max-fresh">Colgate<sup>®</sup> MaxFresh<sup>®</sup></a></li> 
         <li><a href="/en-us/charcoal-toothpaste">Colgate<sup>®</sup> with Charcoal</a></li> 
         <li><a href="/en-us/enamel-health">Colgate<sup>®</sup> Enamel Health<sup>™</sup></a></li> 
         <li><a href="/en-us/whitening-hub">Colgate<sup>®</sup> Optic White<sup>®</sup></a></li> 
         <li><a href="/en-us/kids">Colgate<sup>®</sup> Kids</a></li> 
         <li><a href="/en-us/sensitive">Colgate<sup>®</sup> Sensitive</a></li> 
         <li><a href="/en-us/keep">Colgate<sup>®</sup> Keep</a></li> 
         <li><a href="/en-us/renewal">Colgate<sup>®</sup> Renewal</a></li> 
         <li><a href="/en-us/hum">Colgate<sup>®</sup> Hum</a></li> 
        </ul> </li> 
       <li> 
        <ul class="column"> 
         <li><a href="/en-us/products">View all products &gt;</a></li> 
        </ul> </li> 
      </ul> 
      <ul class="submenu" id="about-submenu"> 
       <li> 
        <ul class="column"> 
         <li><a href="/en-us/our-mission" class="heading">Our Mission</a></li> 
         <li><a href="/en-us/our-mission" class="hide-on-desktop">About our Mission</a></li> 
         <li><a href="/en-us/our-mission/smile-first">Smile First</a></li> 
         <li><a href="/en-us/our-mission/accessible-oral-care">Accessible Oral Care</a></li> 
         <li><a href="/en-us/our-mission/dental-experts">Innovation Champions</a></li> 
        </ul> </li> 
       <li> 
        <ul class="column"> 
         <li><a href="/en-us/oral-health-education" class="heading">Bright Smiles, Bright Futures</a></li> 
         <li><a href="/en-us/oral-health-education" class="hide-on-desktop">About the Program</a></li> 
         <li><a href="/en-us/oral-health-education/my-bright-smile-global-art-contest">Art Contest</a></li> 
         <li><a href="/en-us/oral-health-education/program-kits">Classroom Kit &amp; Samples</a></li> 
         <li><a href="/en-us/oral-health-education/educational-resources">Material and Resources</a></li> 
         <li><a href="/en-us/oral-health-education/mobile-dental-van">Mobile Dental Vans</a></li> 
         <li><a href="/en-us/oral-health-education/dental-volunteers">Volunteer</a></li> 
        </ul> </li> 
       <li> 
        <ul class="column"> 
         <li><a href="/en-us/our-mission/sustainability" class="heading">Sustainability</a></li> 
         <li><a href="/en-us/our-mission/sustainability" class="hide-on-desktop">About Sustainability</a></li> 
         <li><a href="/en-us/our-mission/sustainability/faq">Recyclable Tube</a></li> 
         <li><a href="/en-us/everydropcounts">Save Water</a></li> 
         <li><a href="/en-us/our-mission/sustainability/products">Sustainable Products</a></li> 
         <li><a href="/en-us/our-mission/sustainability/actions">Sustainable Habits</a></li> 
        </ul> </li> 
       <li> 
        <ul class="column"> 
         <li><a href="/en-us/make-the-u" class="heading">Haz La U Grants</a></li> 
        </ul> </li> 
      </ul> 
      <p><button class="close" aria-label="Close Menu">&nbsp;</button></p> 
     </div> 
    </div> 
   </div>
   <div class="richText component section quick-links odd"> 
    <div class="component-content"> 
     <div class="richText-content"> 
      <ul> 
       <li><a data-path="/en-us/oral-health/" href="/en-us/oral-health">Oral Health</a></li> 
       <li><a data-path="/en-us/products/" href="/en-us/products">Products</a></li> 
       <li><a data-path="/en-us/power-of-optimism/" href="/en-us/our-mission">About</a></li> 
      </ul> 
     </div> 
    </div> 
   </div>
   <div class="box component section breadcrumbs-occ-optimization even last"> 
     
    <div class="component-content" id="0904833738"> 
     <div class="paragraphSystem content"> 
      <a id="01398854112" style="visibility:hidden" aria-hidden="true"></a> 
      <div class="breadcrumbs component section default-style first odd last"> 
       <nav aria-label="Breadcrumb" class="component-content"> 
        <div class="analytics-breadcrumbs-tracking"></div> 
        <ol class="breadcrumbs-list breadcrumbs-without-separator"> 
         <li class="breadcrumb-list-item odd first "> <a href="/en-us" aria-label="Home">Home</a> <span class="breadcrumbs-separator"></span> </li> 
         <li class="breadcrumb-list-item even "> <a href="/en-us/oral-health" aria-label="Oral Health, Dental Conditions &amp; Treatments">Oral Health, Dental Conditions &amp; Treatments</a> <span class="breadcrumbs-separator"></span> </li> 
         <li class="breadcrumb-list-item odd last "> <a href="/en-us/oral-health/cleft-lip-palate" aria-label="Cleft Lip/Palate">Cleft Lip/Palate</a></li> 
        </ol> 
       </nav> 
      </div> 
     </div> 
    </div> 
   </div>
  </div> 
 </div> 
</div></div></div></div></div></div><div id="content" class="col-xs-12"><div class="row"><div class="layout-outer"><div class="layout-inner"><div class="col-xs-12 default-style"><a id="0496297996" style="visibility:hidden" aria-hidden="true"></a>
    <div class="box component section breadcrumbs-occ-optimization first odd col-xs-12"> 
  
 <div class="component-content" id="0739979996"> 
  <div class="paragraphSystem content"></div> 
 </div> 
</div><div class="parametrizedhtml component section default-style even last col-xs-12 reference-amp-data-capture-config">
 <div class="component-content"> 
  <div class="amp-dc-config" data-display="true" data-url="https://lightbox.amp.colgate.com/signup/" data-lang="en-us" data-api-key="3_LsM2sSgcInWXXRguY_IOOyhZgT1lOg1KHQd6-mn8T5ivEBnz4a9S7nVST_MIxq5d"></div> 
  <style>
  .reference-amp-data-capture-config,
  .amp-dc-config {
    display: none;
  }

  .aem-AuthorLayer-Edit .reference-amp-data-capture-config,
  .aem-AuthorLayer-Edit .amp-dc-config {
    display: block;
  }
</style>
 </div> 
</div><div class="Header paragraphSystem"><a id="01573777634" style="visibility:hidden" aria-hidden="true"></a>
    <div class="box component section article-header-panel ruby-background first odd last col-xs-12"> 
  
 <div class="component-content" id="766859098"> 
  <div class="paragraphSystem content">
   <a id="1435225796" style="visibility:hidden" aria-hidden="true"></a> 
   <div class="image component section default-style first odd col-xs-12 col-lg-12"> 
    <div class="component-content left"> 
     <div class="analytics-image-tracking"></div> 
     <picture><!--[if IE 9]><video style="display: none;"><![endif]-->
 <source srcset="/content/dam/cp-sites/oral-care/oral-care-center/global/article/1055622.jpg.rendition.640.360.jpg" media="(max-width: 320px)">
 <source srcset="/content/dam/cp-sites/oral-care/oral-care-center/global/article/1055622.jpg.rendition.640.360.jpg" media="(max-width: 767px)">
 <source srcset="/content/dam/cp-sites/oral-care/oral-care-center/global/article/1055622.jpg.rendition.640.360.jpg" media="(min-width: 768px) and (max-width: 991px)">
 <source srcset="/content/dam/cp-sites/oral-care/oral-care-center/global/article/1055622.jpg.rendition.640.360.jpg" media="(min-width: 992px) and (max-width: 1199px)">
 <source srcset="/content/dam/cp-sites/oral-care/oral-care-center/global/article/1055622.jpg.rendition.640.360.jpg" media="(min-width: 1200px) and (max-width: 1920px)"><!--[if IE 9]></video><![endif]-->
 <img src="/content/dam/cp-sites/oral-care/oral-care-center/global/article/1055622.jpg" alt="Mom is teaching daughter how to brush" title="Mom is teaching daughter how to brush">
</picture> 
    </div> 
   </div>
   <div class="box component section title-and-date-box even last col-xs-12"> 
     
    <div class="component-content" id="0103438336"> 
     <div class="paragraphSystem content"> 
      <a id="02000938646" style="visibility:hidden" aria-hidden="true"></a> 
      <div class="parametrizedhtml component section default-style col-xs-12 reference-new-badge parametrizedhtml_1767553788"></div> 
      <div class="title component section col-xs-12 col-lg-12 default-style"> 
       <div class="component-content"> 
        <h1 class="title-heading">How Does Your Child’s Cleft Palate Affect Their Oral Health?</h1> 
       </div> 
      </div> 
      <div class="parametrizedhtml component section col-xs-12 col-lg-12 reference-published-date default-style"></div> 
     </div> 
    </div> 
   </div>
  </div> 
 </div> 
</div></div>
</div><div id="left-rail" class="col-xs-12 col-sm-12 col-md-4 col-lg-3 default-style"><div class="row"><div class="col-xs-12 default-style"><a id="1472118066" style="visibility:hidden" aria-hidden="true"></a>
    <div class="parametrizedhtml component section default-style first odd last col-xs-12 reference-top-rated-articles">
 <div class="component-content"> 
  <div class="top-rated-articles" role="navigation" aria-label="Top rated articles"> 
   <div class="category-title"> 
    <h2>Top Articles</h2> 
   </div> 
   <div class="tpl-links"></div> 
   <div class="more-articles"> 
    <a href="#"><h2>More Articles</h2></a> 
   </div> 
  </div> 
  <script>
  // override more articles href pointing to #
  var moreArticles = document.querySelector('.top-rated-articles .more-articles a');

  if (moreArticles && moreArticles.href === window.location + '#') {
    var lastSegment = window.location.pathname.split("/").pop();
    var categoryPath = window.location.pathname.replace("/" + lastSegment, '');
    moreArticles.href = categoryPath;
  }
</script>
 </div> 
</div><div class="left-rail-first paragraphSystem"></div>
</div></div></div><div id="main-body" class="col-xs-12 col-sm-12 col-md-8 col-lg-9 default-style"><div class="row"><div class="col-xs-12 default-style"><a id="620797877" style="visibility:hidden" aria-hidden="true"></a>
    <div class="parametrizedhtml component section default-style first odd col-xs-12 reference-article-overview-dropdown">
 <div class="component-content"> 
  <div class="overview-ddcontainer"> 
   <button class="ddbtn">Overview</button> 
   <div class="dropdown-content"> 
    <div class="chapters"> 
    </div> 
   </div> 
  </div>
 </div> 
</div><div class="parametrizedhtml component section published-date--visible even col-xs-12 reference-published-date">
 <div class="component-content"> 
  <div class="published-date"> 
   <span class="hiddenField">Published date field</span> 
   <span>Last Updated:</span> 
   <span id="published-date"></span> 
  </div>
 </div> 
</div><div class="parametrizedhtml component section default-style odd col-xs-12 reference-medical-review-attribution">
 <div class="component-content"> 
  <p class="medical-review-attribution">Medically Reviewed By <span>Colgate Global Scientific Communications</span></p> 
  <script>
  let metaTag = document.querySelector('meta[content*="colgate:reviewer"]');
  const reviewerP = document.querySelector('.medical-review-attribution');

  if (metaTag) {
    metaTag = metaTag.content;
    const reviewerName = metaTag.substring(metaTag.indexOf('/') + 1);
    const reviewerSpan = reviewerP.querySelector('span');
    reviewerSpan.innerHTML = reviewerName;
  }

  reviewerP.style.display = 'block';
</script>
 </div> 
</div><div class="parametrizedhtml component section default-style even last col-xs-12 reference-vertical-spacer-2-0">
 <div class="component-content"> 
  <div class="vertical-spacer" data-hide-indicator="false"> 
   <div class="lg" style="height: 40px"></div> 
   <div class="md" style="height: 40px"></div> 
   <div class="sm" style="height: 40px"></div> 
   <div class="xs" style="height: 5px"></div> 
  </div>
 </div> 
</div><div class="body-header paragraphSystem"><a id="127842119" style="visibility:hidden" aria-hidden="true"></a>
    <div class="box component section article-main-container chapter first odd last col-xs-12"> 
  
 <div class="component-content" id="527079171"> 
  <div class="paragraphSystem content">
   <a id="2059359597" style="visibility:hidden" aria-hidden="true"></a> 
   <div class="richText component section article-content checklist first odd"> 
    <div class="component-content"> 
     <div class="richText-content"> 
      <p>If your child has a cleft palate, you may be wondering what you can do to help them maintain good oral hygiene. And you would not be alone in this quest to help your little one. This common birth condition is a concern for a lot of other parents, too. Thankfully, with a little bit of know-how and a great dentist (in some circumstances, a team of specialists), your child can have healthy teeth that will make you both smile.</p> 
     </div> 
    </div> 
   </div>
   <div class="richText component section article-content checklist even"> 
    <div class="component-content"> 
     <div class="richText-content"> 
      <h2><a id="what-is-a-cleft?"></a>What Is a Cleft Palate?</h2> 
      <p>Clefts develop during the first few weeks of pregnancy if the tissue that forms the roof of the mouth or the lip doesn't join correctly. According to the <a href="https://www.mayoclinic.org/diseases-conditions/cleft-palate/symptoms-causes/syc-20370985" target="_blank" rel="noopener noreferrer"><strong>Mayo Clinic</strong></a>, openings in the lip and the roof of the mouth are among the most commonly occurring congenital anomalies in newborns. The <a href="https://www.nidcr.nih.gov/health-info/cleft-lip-palate#:~:text=Cleft%20lip%20or%20palate%20are,or%20without%20a%20cleft%20palate." target="_blank" rel="noopener noreferrer"><strong>National Institute of Craniofacial Research</strong></a><strong> </strong>estimates that 2,650 babies are born with cleft palates each year in the United States. And 4,440 babies are born with a cleft lip, with or without a cleft palate. There are various surgeries and corrective appliances available to treat cosmetic and health issues associated with clefts depending on the severity.</p> 
      <p><em>Learn more about </em><a href="https://www.colgate.com/en-us/oral-health/cleft-lip-palate/what-to-expect-with-cleft-palate-surgery"><em><strong>cleft palate surgery</strong>.</em></a></p> 
     </div> 
    </div> 
   </div>
   <div class="richText component section article-content checklist odd"> 
    <div class="component-content"> 
     <div class="richText-content"> 
      <h2><a id="how-are-teeth-affected?"></a>What Causes a Cleft?</h2> 
      <p>There is no one definitive cause, but the CDC cites studies showing that these factors may increase risk:</p> 
      <ul> 
       <li>Smoking during pregnancy</li> 
       <li>Maternal diabetes</li> 
       <li>Maternal diet</li> 
       <li>Use of certain medicines by the mother (mainly medication used to treat epilepsy)</li> 
       <li>Exposure to air pollutants</li> 
       <li>And <a href="https://www.colgate.com/en-us/oral-health/cleft-lip-palate/is-cleft-lip-genetic"><strong>genetic factors</strong></a> all may play a role.</li> 
      </ul> 
     </div> 
    </div> 
   </div>
   <div class="richText component section article-content checklist even"> 
    <div class="component-content"> 
     <div class="richText-content"> 
      <h2><a id="how-are-teeth-affected?"></a>How Can Teeth Be Affected by a Cleft Palate?</h2> 
      <p>Clefts can affect more than just the lip and the roof of your child's mouth – it can also impact the positioning, size, shape, and number of their teeth. And consistent exposure to the air can dry up saliva and allow bacteria to flourish. According to studies performed by the <a href="https://dental.washington.edu/dental-problems-cleft-lip-palate-linked-abnormal-salivary-glands/" target="_blank" rel="noopener noreferrer"><strong>University of Washington</strong></a>, people with this facial difference may have abnormal salivary glands that can adversely affect their oral health, too. Accordingly, people with clefts tend to have a higher than average rate of tooth decay.</p> 
     </div> 
    </div> 
   </div>
   <div class="richText component section article-content checklist odd last"> 
    <div class="component-content"> 
     <div class="richText-content"> 
      <h2><a id="how-are-teeth-affected?"></a>What Can You Do to Help Your Child Maintain Good Oral Hygiene?</h2> 
      <p>For children with a cleft lip or palate, practicing good oral hygiene and seeing a dentist for regular checkups is of the utmost importance to ensure a future with healthy teeth. Start brushing early, at least twice a day.</p> 
      <p>It's recommended that you schedule your child's first dental appointment early. Many dentists suggest bringing children with clefts in for a checkup well before their first birthday so they can identify potential issues. Be sure to ask if they have any recommendations on how to best care for your child's specific needs. If you return regularly for checkups, your dental professional will be able to monitor for any developing tooth decay.</p> 
      <p>Remember that any time spent with your little one is a chance to have some fun. Happy brushing – you've got this!</p> 
     </div> 
    </div> 
   </div>
  </div> 
 </div> 
</div></div>
</div><div class="col-xs-12 default-style"><div class="mid-body paragraphSystem"></div>
</div><div class="col-xs-12 default-style"><a id="224116556" style="visibility:hidden" aria-hidden="true"></a>
    <div class="parametrizedhtml component section default-style first odd col-xs-12 reference-in-article-module">
 <div class="component-content"> 
  <div banner-position="false" class="richText component section tips-and-offers-banner even last col-xs-12 col-md-12 col-lg-12"> 
   <div class="component-content"> 
    <picture> 
     <source srcset="/content/dam/cp-sites/oral-care/oral-care-center/global/general/banners/tips_bannerdesktop.png.rendition.767.767.png" media="(max-width: 767px)"> 
     <img src="/content/dam/cp-sites/oral-care/oral-care-center/global/general/banners/tips_bannerdesktop.png" class="richText-image pull-left" alt="$altImage"> 
    </picture> 
    <div class="richText-content"> 
     <h2>Want more tips and offers sent directly to your inbox? </h2> 
     <p><a href="#lightbox" class="button" data-tracking-id="article-banner">Sign up now</a></p> 
    </div> 
   </div> 
  </div> 
  <script>
        (function(){
            var pathsList = [];

            console.log("Paths list: ", pathsList);

            $(function () {
                if (!ignoreThisPage()) {
                    console.log("Banner Visible");
                } else {
                    console.log("Banner Hidden");
                    $('.reference-in-article-module').hide();
                }
            })

            function ignoreThisPage() {
                var currentPath = window.location.pathname + window.location.search;
                var ignoreThis = false
                pathsList.forEach(function (path) {
                    var pathFound = (currentPath.search(path) > -1);

                    if (pathFound) { ignoreThis = true; }
                });
                return ignoreThis;
            }

            $(window).load(function () {
               var bannerPosition = $('.tips-and-offers-banner').attr("banner-position") === "true";
                if (bannerPosition){
                    positionHandler();
                }
            })

            function positionHandler () {
                $('.article-main-container p').each(function(){
                    if($(this).text().length > 100){
                        $(this).addClass("long")
                    }
                })

               var paraCount = $('.article-main-container .long').length;
               var targetPara = Math.ceil(paraCount/2) - 1;
               var targetParagraph = $('.article-main-container .long').eq(targetPara);
                $('.reference-in-article-module').detach().insertAfter(targetParagraph);
            }
        })();
    </script> 
  <style>
        .reference-in-article-module {
            padding: 0;
        }

        .tips-and-offers-banner {
            margin: 30px 0;
            padding: 0;
        }
      
        .tips-and-offers-banner .component-content .richText-content p .button {
            font-family: ColgateReady, Arial, sans-serif;
            font-weight: 700;
            height: 25px;
            letter-spacing: -0.19px;
            text-decoration: none;
        }

        @media only screen and (min-width: 992px) and (max-width: 1199px) {
            .tips-and-offers-banner .component-content picture {
                left: 20px;
            }
        }
    </style> 
 </div> 
</div><div class="parametrizedhtml component section card-red-title wh-product-cards wh-white-cards even last col-xs-12 reference-related-by-tags">
 <div class="component-content"> 
  <div class="related-elements" related-type="product" button-aria-label="View More" data-cta-label="" number-of-cards="3" pinned-page1="" pinned-page2="" pinned-page3="" custom-col-size="col-xs-6 col-sm-6 col-md-4" format="all" campaign-sort="false"> 
   <h2 class="small-title">Recommended Products</h2> 
  </div> 
  <script>
 $(function () {
   var ctaValue =  document.querySelector('.related-elements').getAttribute('data-cta-label');
   
   setTimeout(function() {
   $('.buyBtnCanvas').each(function (i, item) {
     if(ctaValue === '') {
     	item.style.display = 'none';
     }
	})
   }, 3800)
   
 })
</script>
 </div> 
</div><div class="body-last paragraphSystem"></div>
</div></div></div><div class="col-xs-12 default-style"><a id="642148118" style="visibility:hidden" aria-hidden="true"></a>
    <div class="parametrizedhtml component section default-style first odd col-xs-12 reference-medical-schema-article">
 <div class="component-content"> 
  <script>  
window.addEventListener('DOMContentLoaded', (event) => {
  
  const h1 = document.querySelector('.Header h1').innerHTML;
  const title = document.querySelector('meta[name="title"]').content;
  const headline = h1 !== "" ? h1 : title;
  const description = document.querySelector('meta[name="description"]').content;
  const url = window.location.href;
  const imageURL = document.querySelector('.Header .box .component-content .image picture img').src;
  const logoURL = document.querySelector('.main-header .logo .component-content a picture img');
  const datePublished = document.querySelector('meta[name="published_date"]').content;
  const reviewerTag = document.querySelector('meta[content*="colgate:reviewer"]');
  let reviewer = "";
  
  if (reviewerTag !== null) {
    reviewer = reviewerTag.content.split("/")[1];
    console.log(reviewer);
  }
  
  let schemaDataText = {
    "@context": "https://schema.org/",
    "@type": "MedicalWebPage",
    "headline": headline,
    "description": description,
    "url": url,
    "Image": {
      "@type":"ImageObject",
      "url": imageURL,
    },
    "author": {
      "@type": "Organization",
      "name": "Colgate"
    },
    "publisher": {
      "@type": "Organization",
      "name":"Colgate",
      "logo": {
        "@type": "ImageObject",
        "url": logoURL,
      }
    },
    "reviewedBy": {
      "@type": "Person",
      "name": reviewer 
    },
    "datePublished": datePublished
  };
    
  const script = document.createElement('script');
  script.setAttribute('type', 'application/ld+json');
  script.textContent = JSON.stringify(schemaDataText);
  document.head.appendChild(script);
}); 
</script>
 </div> 
</div><div class="ssiSnippetReference snippetReference section default-style even component col-xs-12 col-lg-12 col-lg-offset-0 reference-article-disclaimer">
 <div class="inner"> 
  <div class="component-content"> 
   <div>
	<div>
	<a id="01827845427" style="visibility:hidden" aria-hidden="true"></a>
    <div class="richText component section default-style first odd last">
 <div class="component-content"> 
  <div class="richText-content"> 
   <p><em><span class="disclaimer">This article is intended to promote understanding of and knowledge about general oral health topics. It is not intended to be a substitute for professional advice, diagnosis or treatment. Always seek the advice of your dentist or other qualified healthcare provider with any questions you may have regarding a medical condition or treatment.</span></em></p> 
  </div> 
 </div> 
</div></div>
</div> 
  </div> 
 </div> 
</div><div class="box component section four-rounded-corners light-grey-background odd last col-xs-12 col-lg-12 col-lg-offset-0"> 
  
 <div class="component-content" id="0770481086"> 
  <div class="paragraphSystem content">
   <a id="1327657900" style="visibility:hidden" aria-hidden="true"></a> 
   <div class="parametrizedhtml component section default-style first odd col-xs-12 col-lg-10 col-lg-offset-1 reference-Mopinion-feedback"> 
    <div class="component-content"> 
     <!-- Mopinion Pastea.se  start --> 
     <script type="text/javascript">(function(){var id="89s8h4lqkr7ndw2ynnx2xqbed6lurq6fn63";var js=document.createElement("script");js.setAttribute("type","text/javascript");js.setAttribute("src","//deploy.mopinion.com/js/pastease.js");document.getElementsByTagName("head")[0].appendChild(js);var t=setInterval(function(){try{new Pastease.load(id);clearInterval(t)}catch(e){}},50)})();</script> 
     <!-- Mopinion Pastea.se end --> 
     <img src="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/mopinion-bg-toothpaste.png" alt="Mobile Top Image" class="mobile-top-img"> 
     <div id="surveyContent" back-btn-text="No thanks" bg-image="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/mopinion_bg.png" bg-image-alt="Background Image Alt"> 
      <fieldset class="reaction-container"> 
       <legend class="reaction-title">Was this article helpful?</legend> 
       <div class="custom-radio"> 
        <input id="like-id" type="radio" tabindex="-1"> 
        <label for="like-id" class="btn smile" tabindex="0"><i class="icon-ColgateIcons_Smile"></i>Like</label> 
       </div> 
       <div class="custom-radio"> 
        <input id="neutral-id" type="radio" tabindex="-1"> 
        <label for="neutral-id" class="btn neutral" tabindex="0"><i class="icon-ColgateIcons_Emoji---Meh"></i>Neutral</label> 
       </div> 
      </fieldset> 
     </div> 
     <p class="message-text" tabindex="0" aria-live="polite">Thank you for submitting your feedback!</p> 
     <p class="contact-text">If you’d like a response, <a href="/en-us/contact-us">Contact Us</a>.</p> 
     <img src="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/mopinion-bg-toothbrush.png" alt="Mobile Bottom Image" class="mobile-bottom-img"> 
    </div> 
   </div>
   <div class="parametrizedhtml component section default-style even last col-xs-12 col-lg-10 col-lg-offset-1 reference-related-by-tags"> 
    <div class="component-content"> 
     <div class="related-elements" related-type="article" button-aria-label="View More" data-cta-label="" number-of-cards="2" pinned-page1="" pinned-page2="" pinned-page3="" custom-col-size="" format="all" campaign-sort="false"> 
      <h2 class="small-title">You also might like</h2> 
     </div> 
     <script>
 $(function () {
   var ctaValue =  document.querySelector('.related-elements').getAttribute('data-cta-label');
   
   setTimeout(function() {
   $('.buyBtnCanvas').each(function (i, item) {
     if(ctaValue === '') {
     	item.style.display = 'none';
     }
	})
   }, 3800)
   
 })
</script> 
    </div> 
   </div>
  </div> 
 </div> 
</div><div class="related-content paragraphSystem"></div>
</div></div></div></div></div><div id="footer" class="col-xs-12"><div class="row"><div class="layout-outer"><div class="layout-inner"><div class="col-xs-12 col-md-12 default-style"><div class="ssiSnippetReference snippetReference section default-style component col-xs-12 reference-footer footer fixed-component" data-id="swiftype" data-swiftype-index="false">
 <div class="inner"> 
  <div class="component-content"> 
   <div>
	<div>
	<a id="0887827996" style="visibility:hidden" aria-hidden="true"></a>
    <div class="box component section dark-grey-background red-border-bottom first odd col-xs-12 col-sm-12 col-sm-offset-0"> 
  
 <div class="component-content" id="01360520416"> 
  <div class="paragraphSystem content">
   <a id="1379495050" style="visibility:hidden" aria-hidden="true"></a> 
   <div class="image component section footer-curve first odd col-xs-12 col-lg-12"> 
    <div class="component-content right"> 
     <div class="analytics-image-tracking"></div> 
     <picture><!--[if IE 9]><video style="display: none;"><![endif]-->
 <source srcset="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/footer/graycurvefooter.png.rendition.767.767.png" media="(max-width: 320px)">
 <source srcset="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/footer/graycurvefooter.png.rendition.767.767.png" media="(max-width: 767px)">
 <source srcset="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/footer/graycurvefooter.png.rendition.44.44.png" media="(min-width: 768px) and (max-width: 991px)">
 <source srcset="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/footer/graycurvefooter.png.rendition.44.44.png" media="(min-width: 992px) and (max-width: 1199px)">
 <source srcset="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/footer/graycurvefooter.png.rendition.44.44.png" media="(min-width: 1200px) and (max-width: 1920px)"><!--[if IE 9]></video><![endif]-->
 <img src="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/footer/graycurvefooter.png" alt="Rounded corner">
</picture> 
    </div> 
   </div>
   <div class="box component section footer-cta-module even col-xs-12"> 
     
    <div class="component-content" id="02024607034"> 
     <div class="paragraphSystem content"> 
      <a id="01103282640" style="visibility:hidden" aria-hidden="true"></a> 
      <div class="parametrizedhtml component section default-style first odd col-xs-12 col-lg-9 reference-responsive-element"> 
       <div class="component-content"> 
        <p class="responsive-element pending this-is-test" data-styles="
  #unique-id {
      color: #fff;
  margin: 0 5px 24px;
  font-size: 26px;
  font-style: italic;
  font-weight: bold;
  letter-spacing: -0.26px;
  line-height: 32px;
  margin-bottom: 30px;
}

html:not(.aem-AuthorLayer-Edit) .footer-cta-module.hidden {
  display: none;
  }

  @media (min-width: 768px) {
    #unique-id {
      ${smStyles}
    }
  }
  
  @media (min-width: 992px) {
    #unique-id {
      margin: 6px -15px 0;
padding-right: 73px;
margin-bottom: 30px;
    }
  }

  @media (min-width: 1200px) {
    #unique-id {
      margin-bottom: 30px;
    }
  }" data-content=" Want more tips and offers sent directly to your inbox?
"></p> 
        <script>
  (function(){
    var e = document.querySelector('.responsive-element.pending');
    var randomNumber = Math.floor((Math.random() * 9999999) + 1);
    var randomId = "responsive-element-" + randomNumber;
    e.id = randomId;

    var styles = e.getAttribute('data-styles').replace(/unique-id/g, randomId);
    var styleTag = document.createElement("style");
    styleTag.innerHTML = styles;
    document.getElementById(randomId).insertAdjacentElement('afterend', styleTag);

    var txt = document.createElement("textarea");
    txt.innerHTML = document.getElementById(randomId).getAttribute('data-content');
    document.getElementById(randomId).innerHTML = txt.value;

    //e.removeAttribute('data-styles');
    //e.removeAttribute('data-content');
    e.classList.remove('pending');
  })();
</script> 
       </div> 
      </div> 
      <div class="parametrizedhtml component section default-style even col-xs-12 col-lg-3 reference-responsive-element"> 
       <div class="component-content"> 
        <p class="responsive-element pending footer-sign-up-button" data-styles="
  #unique-id {
      margin: 0 5px;
}

.footer-sign-up-button a {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  width: 179px;
  height: 45px;
  border-radius: 99999px 0 99999px 99999px;
  background: white;
  font-size: 16px;
  font-weight: bold;
  font-style: italic;
  color: #d2010d;
}

.footer-sign-up-button a:hover {
  text-decoration: none;
}

.footer-sign-up-button a::before {
  content: '\e158';
  font-family: 'Material Icons';
  display: inline-block;
  margin-right: 10px;
  position: relative;
  top: 2px;
  }

  @media (min-width: 768px) {
    #unique-id {
      ${smStyles}
    }
  }
  
  @media (min-width: 992px) {
    #unique-id {
      margin: 0 -15px;
    }
  }

  @media (min-width: 1200px) {
    #unique-id {
      ${lgStyles}
    }
  }" data-content="<a href='#lightbox' data-tracking-id='footer-cta'> Sign up now</a>"></p> 
        <script>
  (function(){
    var e = document.querySelector('.responsive-element.pending');
    var randomNumber = Math.floor((Math.random() * 9999999) + 1);
    var randomId = "responsive-element-" + randomNumber;
    e.id = randomId;

    var styles = e.getAttribute('data-styles').replace(/unique-id/g, randomId);
    var styleTag = document.createElement("style");
    styleTag.innerHTML = styles;
    document.getElementById(randomId).insertAdjacentElement('afterend', styleTag);

    var txt = document.createElement("textarea");
    txt.innerHTML = document.getElementById(randomId).getAttribute('data-content');
    document.getElementById(randomId).innerHTML = txt.value;

    //e.removeAttribute('data-styles');
    //e.removeAttribute('data-content');
    e.classList.remove('pending');
  })();
</script> 
       </div> 
      </div> 
      <div class="parametrizedhtml component section default-style odd last col-xs-12 reference-responsive-element"> 
       <div class="component-content"> 
        <div class="responsive-element pending ${classes}" data-styles="
  #unique-id {
    margin: 0;
height: 44px;
  }

  @media (min-width: 768px) {
    #unique-id {
      ${smStyles}
    }
  }
  
  @media (min-width: 992px) {
    #unique-id {
      margin: 22px -15px 28px;
height: 0;
border-bottom: 2px solid #585554;
    }
  }

  @media (min-width: 1200px) {
    #unique-id {
      ${lgStyles}
    }
  }" data-content=" "></div> 
        <script>
  (function(){
    var e = document.querySelector('.responsive-element.pending');
    var randomNumber = Math.floor((Math.random() * 9999999) + 1);
    var randomId = "responsive-element-" + randomNumber;
    e.id = randomId;

    var styles = e.getAttribute('data-styles').replace(/unique-id/g, randomId);
    var styleTag = document.createElement("style");
    styleTag.innerHTML = styles;
    document.getElementById(randomId).insertAdjacentElement('afterend', styleTag);

    var txt = document.createElement("textarea");
    txt.innerHTML = document.getElementById(randomId).getAttribute('data-content');
    document.getElementById(randomId).innerHTML = txt.value;

    //e.removeAttribute('data-styles');
    //e.removeAttribute('data-content');
    e.classList.remove('pending');
  })();
</script> 
       </div> 
      </div> 
     </div> 
    </div> 
   </div>
   <div class="box component section default-style odd col-xs-12 col-md-12 col-md-offset-0 col-lg-12 col-lg-offset-0"> 
     
    <div class="component-content" id="2059597231"> 
     <div class="paragraphSystem content"> 
      <a id="01126938599" style="visibility:hidden" aria-hidden="true"></a> 
      <div class="richText component section default-style first odd col-xs-12 col-sm-12 col-sm-offset-0 col-md-4 col-md-offset-0 col-lg-4 col-lg-offset-0"> 
       <div class="component-content"> 
        <div class="richText-content"> 
         <h3><a href="/en-us/oral-health" title="Click here to know all the information we have in our oral care center"><u>Oral Health</u></a></h3> 
         <h3><a href="/en-us/oral-health-education" class="button" title="Click here to learn about the commitment we have with thousands of children to improve their oral health"><u>Social Impact</u></a></h3> 
         <h3><a href="/en-us/products" class="button" title="Click here to learn about all Colgate® products and brands"><u>Products</u></a></h3> 
        </div> 
       </div> 
      </div> 
      <div class="richText component section default-style even col-xs-12 col-sm-12 col-sm-offset-0 col-md-2 col-md-offset-0 col-lg-2 col-lg-offset-0"> 
       <div class="component-content"> 
        <div class="richText-content"> 
         <p style="text-align: left;"><a href="/en-us/smiles/special-offers" class="colgate-relaunch-icons link-offers" title="Click here to see all the coupons we have available for you"><u>Coupons</u></a></p> 
         <p style="text-align: left;"><a href="/en-us/where-to-buy" class="link-where-to-buy-icon" title="Click here to find out where you can buy our products"><u>Where to Buy</u></a></p> 
         <p style="text-align: left;"><a href="/en-us/our-mission" class="colgate-relaunch-icons link-our-story" title="Click here to know the power of the optimist"><u>Mission</u></a></p> 
        </div> 
       </div> 
      </div> 
      <div class="richText component section default-style odd col-xs-12 col-sm-12 col-sm-offset-0 col-md-3 col-md-offset-0 col-lg-3 col-lg-offset-0"> 
       <div class="component-content"> 
        <div class="richText-content"> 
         <p style="text-align: left;"><a href="/en-us/contact-us" class="colgate-relaunch-icons link-contact-us" title="Click here to contact us"><u>Contact</u></a></p> 
         <p style="text-align: left;"><a href="/en-us/locations" class="colgate-relaunch-icons link-country-selector" title="Click here if you want to update your location"><u>United States <span>(US English)</span></u></a></p> 
        </div> 
       </div> 
      </div> 
      <div class="box component section default-style even last col-xs-12 col-sm-12 col-sm-offset-0 col-md-3 col-md-offset-0 col-lg-3 col-lg-offset-0"> 
        
       <div class="component-content" id="506903829"> 
        <div class="paragraphSystem content"> 
         <a id="02099951233" style="visibility:hidden" aria-hidden="true"></a> 
         <div class="richText component section default-style first odd col-xs-12 col-lg-12 col-lg-offset-0"> 
          <div class="component-content"> 
           <div class="richText-content"> 
            <p style="text-align: left;"><a href="https://www.colgateprofessional.com" target="_blank" rel="noopener noreferrer" title="Click here to go to our Colgate® Professional page"><u>ColgateProfessional.com</u></a></p> 
            <p style="text-align: left;"><a href="https://shop.colgate.com/" target="_blank" rel="noopener noreferrer" title="Click here to go to our virtual store"><u>Shop.Colgate.com</u></a></p> 
            <p style="text-align: left;"><a href="https://colgatepalmolive.yet2.com" target="_blank" rel="noopener noreferrer" title="Click here if you have an innovative idea to improve oral health"><u>Submit an Idea</u></a></p> 
           </div> 
          </div> 
         </div> 
         <div class="parametrizedhtml component section default-style even last col-xs-12 col-lg-6 reference-social-links"> 
          <div class="component-content"> 
           <div class="social-icons"> 
            <a target="_blank" href="https://www.facebook.com/Colgate" title="Facebook"><img src="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/logos/facebook.png" alt="Facebook"></a> 
            <a target="_blank" href="https://twitter.com/colgate" title="Twitter"><img src="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/logos/twitter.png" alt="Twitter"></a> 
            <a target="_blank" href="https://www.youtube.com/user/ColgateOralCare" title="YouTube"><img src="/content/dam/cp-sites/oral-care/oral-care-center-relaunch/global/logos/youtube.png" alt="Youtube"></a> 
           </div> 
          </div> 
         </div> 
        </div> 
       </div> 
      </div> 
     </div> 
    </div> 
   </div>
   <div class="divider component section grey-divider even col-xs-12 col-md-12 col-md-offset-0 col-lg-12 col-lg-offset-0"> 
    <div class="component-content"> 
    </div> 
   </div>
   <div class="box component section legal-footer odd last col-xs-12 col-md-12 col-md-offset-0 col-lg-12 col-lg-offset-0"> 
     
    <div class="component-content" id="1487408845"> 
     <div class="paragraphSystem content"> 
      <a id="0191536329" style="visibility:hidden" aria-hidden="true"></a> 
      <div class="richText component section copyright first odd col-xs-12 col-sm-12 col-sm-offset-0 col-md-4 col-md-offset-0 col-lg-4 col-lg-offset-0"> 
       <div class="component-content"> 
        <div class="richText-content"> 
         <p style="text-align: left;"><a rel="noopener noreferrer" href="http://www.colgatepalmolive.com/?_ga=2.35904997.493700495.1583777357-384380465.1571842666" target="_blank" title="Click here to enter our corporate page"><u>Brand Logo</u></a></p> 
         <p style="text-align: left;">© <span class="current-year">YYYY</span> Colgate-Palmolive Company.<br> All rights reserved.</p> 
        </div> 
       </div> 
      </div> 
      <div class="richText component section default-style even col-xs-12 col-sm-12 col-sm-offset-0 col-md-2 col-md-offset-0 col-lg-2 col-lg-offset-0"> 
       <div class="component-content"> 
        <div class="richText-content"> 
         <p><u><a rel="noopener noreferrer" href="https://www.colgatepalmolive.com/en-us/legal-privacy-policy/terms-of-use?_ga=2.268169291.493700495.1583777357-384380465.1571842666" target="_blank" title="Click here to know our terms of use">Terms Of Use</a></u></p> 
         <p><u><a rel="noopener noreferrer" href="https://www.colgatepalmolive.com/en-us/legal-privacy-policy" target="_blank" title="Click here to know our privacy policies">Privacy Policy</a></u></p> 
         <p><u><a href="/en-us/all-products" title="Click here to see all the products we have available">All Products</a></u></p> 
        </div> 
       </div> 
      </div> 
      <div class="richText component section default-style odd col-xs-12 col-sm-12 col-sm-offset-0 col-md-3 col-md-offset-0 col-lg-3"> 
       <div class="component-content"> 
        <div class="richText-content"> 
         <p><u><a rel="noopener noreferrer" href="http://optout.aboutads.info/?c=2&amp;lang=EN&amp;_ga=2.267517003.493700495.1583777357-384380465.1571842666" target="_blank" title="Click here to learn more about the ads present on the site">About Our Ads</a></u></p> 
         <p><u><a rel="noopener noreferrer" href="https://www.colgatepalmolive.com/en-us/legal-privacy-policy/childrens-privacy-statement" target="_blank" title="Click here to learn about our children's privacy policy">Children's Privacy Policy</a></u></p> 
         <p><u><a href="/en-us/all-articles" title="Click here to see all the articles we have available">All Articles</a></u></p> 
        </div> 
       </div> 
      </div> 
      <div class="richText component section default-style even last col-xs-12 col-sm-12 col-sm-offset-0 col-md-3 col-md-offset-0 col-lg-3"> 
       <div class="component-content"> 
        <div class="richText-content"> 
         <p><u><a href="#" onclick="truste.eu &amp;&amp; truste.eu.clickListener(2)" title="Click here to learn more about the site's cookies">Cookie Consent Tool</a></u></p> 
         <p><u><a rel="noopener noreferrer" href="https://www.colgatepalmolive.com/en-us/do-not-sell-my-personal-information" target="_blank" title="Click here to learn more about the treatment of personal information on the site">Do Not Sell My Personal Information</a></u></p> 
         <p><u><a href="/en-us/all-resources" title="Click here to learn more about the educational resources available on the site">All Educational Resources</a></u></p> 
        </div> 
       </div> 
      </div> 
     </div> 
    </div> 
   </div>
  </div> 
 </div> 
</div><div class="parametrizedhtml component section default-style even col-xs-12 reference-site-configs">
 <div class="component-content"> 
  <!-- 
This is a list of site-wide config variables, please do not remove or change anything unless 
you know what you are doing
--> 
  <script>
window.ColPalConstants =  {};
//commented as per JSD-40678
//window.ColPalConstants.swiftypeEngineKey = '_u_chNY3DaYoU-waq51Q'; 
  window.ColPalConstants.swiftypeEngineKey = 'Nd8dcSH4mHKAJV8puWyT';
  window.ColPalConstants.swiftypeUrl = 'https://api.swiftype.com/api/v1/public/engines';
  window.ColPalConstants.defaultSearch = '/en-us/search/'
</script>
 </div> 
</div><div class="parametrizedhtml component section default-style odd col-xs-12 reference-automatic-selection-styles-1-0">
 <div class="component-content"> 
  <script>
  (function(){
    const elements = document.querySelectorAll("[class*='js-ss']");
    const styleTag = document.createElement("style");
    let elementsClasses = [];

    elements.forEach(function(e) {
      e.classList.forEach(function(c) {
        elementsClasses.push(c);
      })
    });

    let classesToRender = [];

    elementsClasses.forEach(function(e) {
      if (!classesToRender.includes(e) && e.includes("js-ss")) {
        classesToRender.push(e);
        const cssArray = e.split("--");
        const prefix = cssArray[0];
        let pseudoClass = "";
        let property;
        let value;
        const isResponsive = prefix.includes("min") || prefix.includes("max");
        let mediaFeature;
        const hasPseudoClass = cssArray.length == 4;
        
        if (prefix.includes("min")) {
            mediaFeature = "min";
        } else if (prefix.includes("max")) {
            mediaFeature = "max";
        }

        if (hasPseudoClass) {
          pseudoClass = `:${cssArray[1]}`;
          property = cssArray[2];
          value = cssArray[3].replace("_", ".");
        } else {
          property = cssArray[1];
          value = cssArray[2].replace("_", ".");
        }
        
        let cssRule;

        if (isResponsive) {
          const maxQueryValue = prefix.replace(`js-ss-${mediaFeature}`, "");
          cssRule = document.createTextNode(`@media (${mediaFeature}-width: ${maxQueryValue}px) { .${e}${pseudoClass} {${property}: ${value}} }`);
          styleTag.appendChild(cssRule);
        } else {
          cssRule = document.createTextNode(`.${e}${pseudoClass} {${property}: ${value}}`);
          styleTag.prepend(cssRule);
        }
      }
    });

    document.body.appendChild(styleTag);
  })();
</script>
 </div> 
</div><div class="parametrizedhtml component section default-style even col-xs-12 reference-faq-schema-setup">
 <div class="component-content"> 
  <script>  
window.addEventListener('DOMContentLoaded', (event) => {
  let structuredDataText = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": new Array()
  };
  
  const accordionSlides = document.querySelectorAll('.accordion--faq .accordion-slide');
  
  if (accordionSlides.length) {
    accordionSlides.forEach(function(slide) {
      const question = slide.querySelector('.accordion-title-text').innerHTML;
      const answer = slide.querySelector('.accordion-content .richText-content').innerHTML.trim();
      structuredDataText.mainEntity.push({
        '@type': 'Question',
        'name': question,
        'acceptedAnswer': {
          '@type': 'Answer',
          'text': answer
        }
      });
    });

    const script = document.createElement('script');
    script.setAttribute('type', 'application/ld+json');
    script.textContent = JSON.stringify(structuredDataText);
    document.head.appendChild(script);
  }
});
</script>
 </div> 
</div><div class="parametrizedhtml component section default-style odd col-xs-12 reference-youtube-video-schema">
 <div class="component-content"> 
  <script>
  document.addEventListener('DOMContentLoaded', function () {
    const hasVideo = document.querySelector('.reference-youtube-video') !== null;

    if (hasVideo) {
      const agent = window.navigator.userAgent;
      const botUserAgentsArray = [
        'aolbuild',
        'baidu',
        'googlebot',
        'adsbot-google',
        'mediapartners-google',
        'bingbot',
        'duckduckgo',
        'bingpreview',
        'msnbot',
        'teoma',
        'slurp',
        'linkedinbot',
        'yandexbot',
      ];

      let isBotUserAgent = 0;
      for (let j = 0; j < botUserAgentsArray.length; j++) {
        if (agent.toLowerCase().indexOf(botUserAgentsArray[j].toLowerCase()) !== -1) {
          console.log("botUserAgent found: " + botUserAgentsArray[j].toLowerCase());
          isBotUserAgent = 1;
          break;
        }
      }

      if (isBotUserAgent == 1) {

        let structuredDataText = {
          "@context": "https://schema.org",
          "@type": null
        };

        let iframes = $('iframe[src*=youtube]'),
          youTubeIframes = iframes.filter('[src*=youtube]');

        let jsonObj = {
          "@type": "VideoObject",
          "name": null,
          "description": null,
          "thumbnailUrl": null,
          "uploadDate": null,
          "duration": null,
          "embedUrl": null,
          "interactionStatistic": null,
          "position": null
        };

        let multiple = false;

        let position = 1;

        if (iframes.length > 1) {
          multiple = true;
          structuredDataText["@type"] = "ItemList";
          structuredDataText["itemListElement"] = new Array();
        } else {
          structuredDataText["@type"] = "VideoObject";
          ["@type", 'position'].forEach(key => delete jsonObj[key]);
        }

        const parseYouTube = (youTubeIframes, jsonObj, multiple) => {
          youTubeIframes.each(function (i, v) {
            const url = v.src,
              regExp = /http(s)?:\/\/(www\.)?youtube.com\/embed\/([^?]+)/gi,
              match = url.match(regExp);
            if (match) {
              const id = match[0].split(/[/\s]/)[4];


              $.getJSON(`https://www.googleapis.com/youtube/v3/videos?id=${id}&key=AIzaSyCIMBirzxd9vCi_tm0rBVYwai_pjrFtH6E&part=contentDetails,snippet,statistics`).done(function (data) {
                let jsonObjV = {
                  "@type": "VideoObject",
                  "name": null,
                  "description": null,
                  "thumbnailUrl": null,
                  "uploadDate": null,
                  "duration": null,
                  "embedUrl": null,
                  "interactionStatistic": null,
                  "position": position
                };

                const res = data.items[0];

                jsonObjV.name = res.snippet.title;
                jsonObjV.description = res.snippet.description;
                jsonObjV.thumbnailUrl = [res.snippet.thumbnails.medium.url, res.snippet.thumbnails.high.url];
                jsonObjV.uploadDate = res.snippet.publishedAt;
                jsonObjV.duration = res.contentDetails.duration;
                jsonObjV.embedUrl = url;
                jsonObjV.interactionStatistic = [
                  {
                    "@type": "InteractionCounter",
                    "interactionService": {
                      "@type": "WebSite",
                      "name": "YouTube",
                      "@id": "https://youtube.com"
                    },
                    "interactionType": "https://schema.org/LikeAction",
                    "userInteractionCount": res.statistics.likeCount
                  },
                  {
                    "@type": "InteractionCounter",
                    "interactionService": {
                      "@type": "WebSite",
                      "name": "YouTube",
                      "@id": "https://youtube.com"
                    },
                    "interactionType": "https://schema.org/WatchAction",
                    "userInteractionCount": res.statistics.viewCount
                  }
                ];

                if (multiple) {
                  structuredDataText.itemListElement.push(jsonObjV);
                  jsonObjV.position = position++;
                } else {
                  structuredDataText = Object.assign(structuredDataText, jsonObjV);
                  position++;
                }
              });
            }
          });
        }

        const writeSchema = (structuredDataText) => {
          const script = document.createElement('script');
          script.setAttribute('type', 'application/ld+json');
          script.textContent = JSON.stringify(structuredDataText);
          document.head.appendChild(script);
        }

        if (youTubeIframes.length > 0) parseYouTube(youTubeIframes, jsonObj, multiple);

        const iframesInterval = setInterval(() => {
          if (iframes.length === position - 1) {
            writeSchema(structuredDataText);
            clearInterval(iframesInterval);
          }
        }, 100);
      }
    }
  });
</script>
 </div> 
</div><div class="parametrizedhtml component section default-style even col-xs-12 reference-pdp-product-schema">
 <div class="component-content"> 
  <script> 
 
var occTypeTag = document.querySelector('meta[name="occ_type"]')?.content;

var currentURL = window.location.href;
var url = currentURL.includes('#') ? currentURL.split('#')[0] : currentURL;

  if(occTypeTag && occTypeTag !== 'article') {
    var title = document.querySelector('meta[name="title"]')?.content || "";
    var description = document.querySelector('meta[name="description"]')?.content || "";
    var sku = document.querySelector('meta[name="skuCode"]')?.content || "";
    var imageURL = document.querySelector('meta[name="image"]')?.content || "";
    var brand = document.querySelector('meta[name="occ_brand"]')?.content || "Colgate®";

    var schemaDataText = {
        "@context": "https://schema.org/",
        "@type": "Product",
        "@id": url,
        "name": title,
        "image": imageURL,
        "description": description,
        "sku": sku,
        "brand": brand
      };

      var script = document.createElement('script');
      script.setAttribute('type', 'application/ld+json');
      script.textContent = JSON.stringify(schemaDataText);
     
      setTimeout(function(){
         document.head.appendChild(script);
      }, 1000)
  } 

      </script>
 </div> 
</div><div class="parametrizedhtml component section default-style odd last col-xs-12 reference-scripts-integration">
 <div class="component-content"> 
  <!-- 
Please do not remove unless you know what you are doing.
--> 
  <script>
  (() => {
    if (!document.body.matches('[class*=wcm-edit]')) {
      const bvScript = document.createElement('script');
      bvScript.src = 'https://apps.bazaarvoice.com/deployments/colgate/main_site/production/en_US/bv.js';
      bvScript.async = true;
      document.head.appendChild(bvScript);
    }
  })()
</script>
 </div> 
</div></div>
</div> 
  </div> 
 </div> 
</div></div></div></div></div></div></div></div><!--TrustArc Javascript -->
<script async="async" src="//consent.trustarc.com/notice?domain=colgate.com&c=teconsent
&js=nj&noticeType=bb&pn=2&gtm=1" crossorigin></script>
<!--End TrustArc Javascript -->
<div class="cloudservices servicecomponents"><div class="cloudservice analyticsTrackingImprint"></div>
</div>
<script type="text/javascript" src="/etc/designs/zg/cpcolgate2020/desktop/js.asset.js/core/design.default.bootstrap.v0-0-1.js"></script>
</body>
</html>



"""

# Parse the HTML code
soup = BeautifulSoup(html_code, 'html.parser')

# Extract the title
title = soup.title.string

# If 'Colgate' is in the title, only use the part before ' | Colgate'
if ' | Colgate' in title:
    title = title.split(' | Colgate')[0]

# Modify the title to be used as the filename
filename = title.lower().replace(' ', '_') + '.txt'

# Extract the content
content_div = soup.find('div', class_='article-main-container')
content = ""
for p in content_div.find_all('p'):
    content += p.get_text(separator='\n') + '\n'

# Create a text file and write the title and content
with open(filename, 'w', encoding='utf-8') as file:
    file.write(title + '\n\n')
    file.write(content)

print(f"Article saved as '{filename}'")