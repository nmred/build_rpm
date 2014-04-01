<?php
/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4 foldmethod=marker: */
// +---------------------------------------------------------------------------
// | SWAN [ $_SWANBR_SLOGAN_$ ]
// +---------------------------------------------------------------------------
// | Copyright $_SWANBR_COPYRIGHT_$
// +---------------------------------------------------------------------------
// | Version  $_SWANBR_VERSION_$
// +---------------------------------------------------------------------------
// | Licensed ( $_SWANBR_LICENSED_URL_$ )
// +---------------------------------------------------------------------------
// | $_SWANBR_WEB_DOMAIN_$
// +---------------------------------------------------------------------------
 
/**
+------------------------------------------------------------------------------
* 打包核心处理程序 全局变量
+------------------------------------------------------------------------------
*  
* @version $_SWANBR_VERSION_$
* @copyright $_SWANBR_COPYRIGHT_$
* @author $_SWANBR_AUTHOR_$ 
+------------------------------------------------------------------------------
*/

// {{{ 软件详细信息

// 软件名称
define('SWAN_ROOT', '/usr/local/swan/smeta/');

// 软件名称
define('SWAN_SOFTNAME', 'smeta');

// 软件版本号
define('SWAN_VERSION', '0.1.0');

// 软件发行号
define('SWANBR_RELEASE', 'beta');

//软件宣言 ------一切为了方便
define('SWANBR_SLOGAN', 'Everything in order to facilitate');

//版权声明
define('SWANBR_COPYRIGHT', '© 2012-2014 swanlinux');

//许可协议 
define('SWANBR_LICENSED_URL', 'BSD');

// 官方网址
define('SWANBR_WEB_DOMAIN', 'http://www.swanlinux.net');

// 作者
define('SWANBR_AUTHOR', 'swanteam <nmred_2008@126.com>');

// 默认时区设置
define('SWAN_TIMEZONE_DEFAULT', 'Asia/Chongqing');

date_default_timezone_set(SWAN_TIMEZONE_DEFAULT);
// }}}
