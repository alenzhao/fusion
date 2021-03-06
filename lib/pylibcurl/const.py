from ctypes import *

STRING = c_char_p


CURLOPT_SSLENGINE_DEFAULT = 90
CURLOPT_UNRESTRICTED_AUTH = 105
CURLE_REMOTE_DISK_FULL = 70
CURLOPT_FTP_SSL_CCC = 154
CURLFORM_END = 17
CURLE_OPERATION_TIMEDOUT = 28
CURLE_OPERATION_TIMEOUTED = CURLE_OPERATION_TIMEDOUT # alias
CURLOPT_TRANSFERTEXT = 53
CURLOPT_SOCKOPTFUNCTION = 20148
CURL_LOCK_DATA_SHARE = 1
CURLOPT_ENCODING = 10102
CURLOPT_KEYPASSWD = 10026
CURLOPT_SSLKEYPASSWD = CURLOPT_KEYPASSWD # alias
CURLFORM_STREAM = 19
CURLOPT_PROXY = 10004
CURLPROXY_SOCKS4 = 4
CURLINFO_RESPONSE_CODE = 2097154
CURLOPT_NEW_DIRECTORY_PERMS = 160
CURLE_FTP_WEIRD_SERVER_REPLY = 8
CURL_HTTP_VERSION_LAST = 3
CURLVERSION_LAST = 4
CURLOPT_HEADERFUNCTION = 20079
CURLOPT_POSTFIELDSIZE_LARGE = 30120
CURLFORM_FILECONTENT = 7
CURLINFO_SPEED_UPLOAD = 3145738
CURLFTPAUTH_DEFAULT = 0
CURLE_PEER_FAILED_VERIFICATION = 51
CURLSHE_INVALID = 3
CURLOPT_DIRLISTONLY = 48
CURLOPT_FTPLISTONLY = CURLOPT_DIRLISTONLY # alias
CURLE_OBSOLETE4 = 4
CURLE_TFTP_UNKNOWNID = 72
CURLE_HTTP_RETURNED_ERROR = 22
CURLE_HTTP_NOT_FOUND = CURLE_HTTP_RETURNED_ERROR # alias
CURLOPT_COOKIEFILE = 10031
CURLINFO_REDIRECT_TIME = 3145747
CURLE_FUNCTION_NOT_FOUND = 41
CURLOPT_POSTFIELDSIZE = 60
CURLE_URL_MALFORMAT_USER = CURLE_OBSOLETE4 # alias
CURLOPT_SSH_HOST_PUBLIC_KEY_MD5 = 10162
CURLOPT_UPLOAD = 46
CURLFORM_CONTENTTYPE = 14
CURLE_OBSOLETE16 = 16
CURLE_OBSOLETE40 = 40
CURLOPT_COOKIE = 10022
CURLUSESSL_LAST = 4
CURLOPT_PROGRESSFUNCTION = 20056
CURLMOPT_TIMERFUNCTION = 20004
CURLFORM_PTRCONTENTS = 5
CURLE_URL_MALFORMAT = 3
CURLOPT_KRBLEVEL = 10063
CURLE_SSL_ENGINE_SETFAILED = 54
CURLOPT_PORT = 3
CURLE_OBSOLETE24 = 24
CURLOPT_CONV_TO_NETWORK_FUNCTION = 20143
CURLOPT_LOCALPORTRANGE = 140
CURLOPT_POSTQUOTE = 10039
CURL_LOCK_DATA_COOKIE = 2
def curl_multi_socket(x,y,z): return curl_multi_socket_action(x,y,0,z) # macro
CURLM_OUT_OF_MEMORY = 3
CURLFORM_NAMELENGTH = 3
CURLOPT_CAINFO = 10065
CURLE_OBSOLETE44 = 44
CURLOPT_NOSIGNAL = 99
CURL_LOCK_DATA_SSL_SESSION = 4
CURLOPT_MAXFILESIZE = 114
CURLFORM_COPYCONTENTS = 4
CURLMOPT_LASTENTRY = 7
CURLPROXY_HTTP = 0
CURLE_REMOTE_FILE_NOT_FOUND = 78
CURLOPT_DNS_USE_GLOBAL_CACHE = 91
CURLINFO_SSL_ENGINES = 4194331
CURLUSESSL_CONTROL = 2
CURLE_USE_SSL_FAILED = 64
CURLE_FTP_SSL_FAILED = CURLE_USE_SSL_FAILED # alias
CURLINFO_OS_ERRNO = 2097177
CURLOPT_SSL_CIPHER_LIST = 10083
CURLOPT_COOKIELIST = 10135
CURLMSG_NONE = 0
CURLFTPSSL_CCC_PASSIVE = 1
CURLPROXY_SOCKS5 = 5
CURLE_FTP_CANT_GET_HOST = 15
CURL_SSLVERSION_DEFAULT = 0
CURLE_FILE_COULDNT_READ_FILE = 37
CURLOPT_STDERR = 10037
CURLE_SSL_CERTPROBLEM = 58
CURLSHOPT_USERDATA = 5
CURLVERSION_FIRST = 0
CURLOPT_FTP_FILEMETHOD = 138
CURLFTPSSL_CCC_NONE = 0
CURLSHE_BAD_OPTION = 1
CURLOPT_USE_SSL = 119
CURLOPT_FTP_SSL = CURLOPT_USE_SSL # alias
CURLE_COULDNT_RESOLVE_HOST = 6
CURLE_OBSOLETE57 = 57
CURLFTPAUTH_LAST = 3
CURLE_TOO_MANY_REDIRECTS = 47
CURLOPT_INFILE = 10009
CURLOPT_READDATA = CURLOPT_INFILE # alias
def curl_easy_getinfo(handle,info,arg): return curl_easy_getinfo(handle,info,arg) # macro
CURLUSESSL_NONE = 0
CURLFTPSSL_NONE = CURLUSESSL_NONE # alias
CURLE_SEND_FAIL_REWIND = 65
CURLOPT_SOCKOPTDATA = 10149
CURLFTPMETHOD_MULTICWD = 1
CURLINFO_PROXYAUTH_AVAIL = 2097176
CURLMOPT_TIMERDATA = 10005
CURLOPT_USERPWD = 10005
CURLINFO_CONNECT_TIME = 3145733
CURL_SOCKET_BAD = -1 # Variable c_int '-0x000000001'
CURL_SOCKET_TIMEOUT = CURL_SOCKET_BAD # alias
CURLFTPMETHOD_LAST = 4
CURLSHOPT_UNSHARE = 2
CURLM_INTERNAL_ERROR = 4
CURLVERSION_FOURTH = 3
CURLOPT_TCP_NODELAY = 121
CURL_FORMADD_MEMORY = 1
CURLFTPMETHOD_NOCWD = 2
CURLFORM_BUFFERPTR = 12
CURLOPT_SHARE = 10100
CURLFORM_BUFFERLENGTH = 13
CURLOPT_INFILESIZE_LARGE = 30115
CURLE_LIBRARY_NOT_FOUND = CURLE_OBSOLETE40 # alias
CURLVERSION_NOW = CURLVERSION_FOURTH # alias
CURL_LAST = 82
CURL_FORMADD_ILLEGAL_ARRAY = 6
CURLOPT_OPENSOCKETFUNCTION = 20163
def curl_easy_setopt(handle,opt,param): return curl_easy_setopt(handle,opt,param) # macro
CURLE_GOT_NOTHING = 52
CURLE_RANGE_ERROR = 33
CURLOPT_SEEKDATA = 10168
CURLOPT_HTTP_VERSION = 84
CURLINFO_STARTTRANSFER_TIME = 3145745
CURLOPT_CONV_FROM_UTF8_FUNCTION = 20144
CURLCLOSEPOLICY_NONE = 0
CURLOPT_NOPROGRESS = 43
CURLOPT_HTTPGET = 80
CURLOPT_CRLF = 27
CURLINFO_HTTP_CONNECTCODE = 2097174
CURLE_REMOTE_FILE_EXISTS = 73
CURLE_TFTP_EXISTS = CURLE_REMOTE_FILE_EXISTS # alias
CURL_TIMECOND_NONE = 0
CURLINFO_PRETRANSFER_TIME = 3145734
CURL_LOCK_DATA_CONNECT = 5
CURLSHE_IN_USE = 2
CURL_LOCK_DATA_DNS = 3
CURLE_FILESIZE_EXCEEDED = 63
CURLOPT_PREQUOTE = 10093
CURL_SSLVERSION_SSLv3 = 3
CURLOPT_TIMEOUT_MS = 155
CURL_NETRC_OPTIONAL = 1
CURLOPT_FTP_ACCOUNT = 10134
CURLE_OBSOLETE32 = 32
CURLE_FTP_COULDNT_GET_SIZE = CURLE_OBSOLETE32 # alias
CURLINFO_FTP_ENTRY_PATH = 1048606
CURLOPT_REFERER = 10016
CURL_LOCK_ACCESS_SHARED = 1
CURLE_BAD_CONTENT_ENCODING = 61

# values for enumeration 'curl_usessl'
CURLUSESSL_TRY = 1
CURLUSESSL_ALL = 3
curl_usessl = c_int # enum
curl_ftpssl = curl_usessl # alias
CURL_FORMADD_OK = 0
CURLE_OBSOLETE29 = 29
CURLE_FTP_COULDNT_SET_ASCII = CURLE_OBSOLETE29 # alias
CURLFTPMETHOD_SINGLECWD = 3
CURLOPT_IGNORE_CONTENT_LENGTH = 136
CURLE_SSL_ENGINE_NOTFOUND = 53
CURLINFO_SPEED_DOWNLOAD = 3145737
CURLPROXY_SOCKS5_HOSTNAME = 7
CURLE_BAD_FUNCTION_ARGUMENT = 43
CURL_LOCK_DATA_LAST = 6
CURLE_LOGIN_DENIED = 67
CURLOPT_POSTFIELDS = 10015
CURLE_HTTP_RANGE_ERROR = CURLE_RANGE_ERROR # alias
CURLM_CALL_MULTI_PERFORM = -1
CURLM_CALL_MULTI_SOCKET = CURLM_CALL_MULTI_PERFORM # alias
CURL_FORMADD_OPTION_TWICE = 2
CURLE_SSH = 79
CURLOPT_LOCALPORT = 139
CURLE_TFTP_NOTFOUND = 68
CURLOPT_PROTOCOLS = 181
CURLOPT_RESUME_FROM = 21
CURLOPT_PROXYTYPE = 101
CURLE_QUOTE_ERROR = 21
CURLE_FTP_QUOTE_ERROR = CURLE_QUOTE_ERROR # alias
CURLOPT_RESUME_FROM_LARGE = 30116
CURLCLOSEPOLICY_LEAST_RECENTLY_USED = 2
CURLMOPT_SOCKETDATA = 10002
CURLIOCMD_RESTARTREAD = 1
CURL_TIMECOND_LASTMOD = 3
CURLOPT_APPEND = 50
CURLOPT_RANDOM_FILE = 10076
CURLOPT_NOBODY = 44
CURLOPT_SSL_CTX_FUNCTION = 20108
CURLOPT_FTPPORT = 10017
CURLOPT_FTP_USE_EPSV = 85
CURLOPT_SSL_SESSIONID_CACHE = 150
CURLOPT_COOKIESESSION = 96
CURLE_SSL_SHUTDOWN_FAILED = 80
CURLFTPAUTH_SSL = 1
CURLOPT_TIMEVALUE = 34
CURLE_FTP_COULDNT_RETR_FILE = 19
CURLOPT_FOLLOWLOCATION = 52
CURLM_UNKNOWN_OPTION = 6
CURLOPT_INFILESIZE = 14
CURL_LOCK_ACCESS_SINGLE = 2
CURLE_OBSOLETE50 = 50
CURLOPT_FTPSSLAUTH = 129
CURLOPT_SSLVERSION = 32
CURLE_COULDNT_RESOLVE_PROXY = 5
CURLOPT_KRB4LEVEL = CURLOPT_KRBLEVEL # alias
CURLSHOPT_SHARE = 1
CURLINFO_NAMELOOKUP_TIME = 3145732
CURLE_TFTP_DISKFULL = CURLE_REMOTE_DISK_FULL # alias
CURLE_PARTIAL_FILE = 18
CURL_HTTP_VERSION_NONE = 0
CURL_LOCK_DATA_NONE = 0
CURLE_UPLOAD_FAILED = 25
CURLE_FTP_COULDNT_STOR_FILE = CURLE_UPLOAD_FAILED # alias
CURLE_SSL_ENGINE_INITFAILED = 66
CURLINFO_DATA_IN = 3
CURLINFO_REDIRECT_COUNT = 2097172
CURLE_OBSOLETE10 = 10
CURLE_SEND_ERROR = 55
CURLOPT_HEADER = 42
CURL_FORMADD_LAST = 8
CURLOPT_OPENSOCKETDATA = 10164
CURLE_CONV_FAILED = 75
CURLFORM_OBSOLETE = 9
CURLE_FTP_WEIRD_227_FORMAT = 14
def curl_share_setopt(share,opt,param): return curl_share_setopt(share,opt,param) # macro
CURLOPT_HTTPPROXYTUNNEL = 61
CURLE_SHARE_IN_USE = CURLE_OBSOLETE57 # alias
CURL_HTTP_VERSION_1_1 = 2
CURLE_LDAP_SEARCH_FAILED = 39
CURLINFO_HTTPAUTH_AVAIL = 2097175
CURLOPT_WRITEHEADER = 10029
CURLOPT_HEADERDATA = CURLOPT_WRITEHEADER # alias
CURLE_RECV_ERROR = 56
CURLCLOSEPOLICY_SLOWEST = 4
CURLOPT_FRESH_CONNECT = 74
CURLOPT_HTTPPOST = 10024
CURLE_ABORTED_BY_CALLBACK = 42
CURLOPT_SSL_VERIFYHOST = 81
CURLE_FTP_COULDNT_SET_TYPE = 17
CURLE_FTP_COULDNT_SET_BINARY = CURLE_FTP_COULDNT_SET_TYPE # alias
CURLINFO_EFFECTIVE_URL = 1048577
CURLSHOPT_NONE = 0
CURLSHOPT_UNLOCKFUNC = 4
CURLFTPSSL_LAST = CURLUSESSL_LAST # alias
CURLE_UNKNOWN_TELNET_OPTION = 48
CURLOPT_MAXFILESIZE_LARGE = 30117
CURLMOPT_PIPELINING = 3
CURLSSH_AUTH_ANY = -1 # Variable c_int '-0x000000001'
CURLSSH_AUTH_DEFAULT = CURLSSH_AUTH_ANY # alias
CURLE_HTTP_POST_ERROR = 34
CURLOPT_NETRC = 51
CURLOPT_DEBUGFUNCTION = 20094
CURLOPT_SSL_CTX_DATA = 10109
CURLFORM_OBSOLETE2 = 18
CURLE_LDAP_CANNOT_BIND = 38
CURLOPT_MAXCONNECTS = 71
CURLE_OBSOLETE46 = 46
CURLE_BAD_PASSWORD_ENTERED = CURLE_OBSOLETE46 # alias
CURLOPT_SSLCERTTYPE = 10086
CURLOPT_SSH_PRIVATE_KEYFILE = 10153
CURLOPT_POST = 47
CURLE_MALFORMAT_USER = CURLE_OBSOLETE24 # alias
CURLE_SSL_CONNECT_ERROR = 35
CURLVERSION_THIRD = 2
CURL_FORMADD_UNKNOWN_OPTION = 4
CURLOPT_COOKIEJAR = 10082
CURLOPT_REDIR_PROTOCOLS = 182
CURLE_OBSOLETE12 = 12
CURLE_FTP_WEIRD_USER_REPLY = CURLE_OBSOLETE12 # alias
CURLE_INTERFACE_FAILED = 45
CURLE_HTTP_PORT_FAILED = CURLE_INTERFACE_FAILED # alias
CURL_GLOBAL_ALL = 3 # Variable c_int '3'
CURL_GLOBAL_DEFAULT = CURL_GLOBAL_ALL # alias
CURLE_TFTP_NOSUCHUSER = 74
CURLINFO_DATA_OUT = 4
CURLOPT_BUFFERSIZE = 98
CURLOPT_SSH_AUTH_TYPES = 151
CURLINFO_SSL_DATA_OUT = 6
CURLE_BAD_DOWNLOAD_RESUME = 36
CURLMSG_DONE = 1
CURLOPT_AUTOREFERER = 58
CURLM_OK = 0
CURLOPT_VERBOSE = 41
CURL_SSLVERSION_TLSv1 = 1
CURLOPT_WRITEINFO = 10040
CURLVERSION_SECOND = 1
CURLE_BAD_CALLING_ORDER = CURLE_OBSOLETE44 # alias
CURLOPT_EGDSOCKET = 10077
CURLOPT_IOCTLFUNCTION = 20130
CURLINFO_SSL_VERIFYRESULT = 2097165
CURLFORM_ARRAY = 8
CURLFTPAUTH_TLS = 2
CURLE_FTP_WEIRD_PASS_REPLY = 11
CURLSHE_LAST = 5
CURLINFO_SSL_DATA_IN = 5
CURLINFO_NONE = 0
CURLINFO_FILETIME = 2097166
CURLSOCKTYPE_IPCXN = 0
CURLE_AGAIN = 81
CURLCLOSEPOLICY_LAST = 6
CURLOPT_COPYPOSTFIELDS = 10165
CURLOPT_DEBUGDATA = 10095
CURLE_REMOTE_ACCESS_DENIED = 9
CURLE_FTP_ACCESS_DENIED = CURLE_REMOTE_ACCESS_DENIED # alias
CURLOPT_FTP_CREATE_MISSING_DIRS = 110
CURLE_TELNET_OPTION_SYNTAX = 49
CURLINFO_TEXT = 0
CURLE_FTP_USER_PASSWORD_INCORRECT = CURLE_OBSOLETE10 # alias
CURLE_FTP_PARTIAL_FILE = CURLE_PARTIAL_FILE # alias
CURLOPT_FAILONERROR = 45
CURLOPT_SSLKEY = 10087
CURLINFO_SIZE_UPLOAD = 3145735
CURLOPT_DNS_CACHE_TIMEOUT = 92
CURLFTPSSL_CCC_ACTIVE = 2
CURLOPT_MAX_RECV_SPEED_LARGE = 30146
CURLE_FTP_BAD_DOWNLOAD_RESUME = CURLE_BAD_DOWNLOAD_RESUME # alias
CURLE_LDAP_INVALID_URL = 62
CURLOPT_TIMEOUT = 13
CURLOPT_FILE = 10001
CURLOPT_WRITEDATA = CURLOPT_FILE # alias
CURLCLOSEPOLICY_LEAST_TRAFFIC = 3
CURLINFO_REQUEST_SIZE = 2097164
CURLOPT_QUOTE = 10028
CURLE_SSL_CIPHER = 59
CURL_FORMADD_INCOMPLETE = 5
CURLFORM_LASTENTRY = 20
CURLOPT_NETRC_FILE = 10118
CURLE_COULDNT_CONNECT = 7
CURLE_FAILED_INIT = 2
CURLOPT_HTTP_TRANSFER_DECODING = 157
CURLINFO_HTTP_CODE = CURLINFO_RESPONSE_CODE # alias
CURLINFO_REDIRECT_URL = 1048607
CURLOPT_HTTPAUTH = 107
CURL_NETRC_IGNORED = 0
CURL_TIMECOND_IFMODSINCE = 1
CURLINFO_LASTSOCKET = 2097181
CURLFTPSSL_TRY = CURLUSESSL_TRY # alias
CURLOPT_HTTP_CONTENT_DECODING = 158
CURL_FORMADD_NULL = 3
CURLOPT_MAX_SEND_SPEED_LARGE = 30145
CURL_SSLVERSION_SSLv2 = 2
CURLOPT_SSLCERT = 10025
CURLIOE_UNKNOWNCMD = 1
CURLOPT_PROXYPORT = 59
CURLINFO_TOTAL_TIME = 3145731
CURLOPT_CONNECT_ONLY = 141
CURLE_FTP_CANT_RECONNECT = CURLE_OBSOLETE16 # alias
def curl_multi_setopt(handle,opt,param): return curl_multi_setopt(handle,opt,param) # macro
CURLE_SSL_PEER_CERTIFICATE = CURLE_PEER_FAILED_VERIFICATION # alias
CURLOPT_LASTENTRY = 183
CURLINFO_CONTENT_LENGTH_DOWNLOAD = 3145743
CURLIOE_FAILRESTART = 2
CURLOPT_TIMECONDITION = 33
CURLIOE_LAST = 3
CURLPROXY_SOCKS4A = 6
CURLINFO_HEADER_IN = 1
CURLOPT_PROXYAUTH = 111
CURLE_OBSOLETE20 = 20
CURLE_FTP_WRITE_ERROR = CURLE_OBSOLETE20 # alias
CURLE_OBSOLETE = CURLE_OBSOLETE50 # alias
CURLOPT_FTP_USE_EPRT = 106
CURLOPT_SSH_PUBLIC_KEYFILE = 10152
CURLOPT_PUT = 54
CURLFTPSSL_CCC_LAST = 3
CURLE_OUT_OF_MEMORY = 27
CURLE_SSL_CACERT_BADFILE = 77
CURLOPT_SSLKEYTYPE = 10088
CURLOPT_PRIVATE = 10103
CURLE_READ_ERROR = 26
CURLINFO_HEADER_OUT = 2
CURLIOCMD_LAST = 2
CURLE_FTP_COULDNT_USE_REST = 31
CURLOPT_IOCTLDATA = 10131
CURLFTPMETHOD_DEFAULT = 0
CURLOPT_URL = 10002
CURLINFO_LASTONE = 31
CURL_HTTP_VERSION_1_0 = 1
CURLOPT_FTPAPPEND = CURLOPT_APPEND # alias
CURLE_TFTP_PERM = 69
CURLFORM_PTRNAME = 2
CURLOPT_PROXYUSERPWD = 10006
CURLFORM_NOTHING = 0
CURLOPT_WRITEFUNCTION = 20011
CURLOPT_PROXY_TRANSFER_MODE = 166
CURLOPT_CLOSEPOLICY = 72
CURLSHOPT_LOCKFUNC = 3
CURLOPT_POST301 = 161
CURLM_BAD_SOCKET = 5
CURLOPT_CONNECTTIMEOUT = 78
CURLSHE_OK = 0
CURLM_BAD_EASY_HANDLE = 2
CURLOPT_CUSTOMREQUEST = 10036
CURLIOCMD_NOP = 0
CURLE_SSL_CACERT = 60
CURL_TIMECOND_IFUNMODSINCE = 2
CURLOPT_FORBID_REUSE = 75
CURLE_TFTP_ILLEGAL = 71
CURLCLOSEPOLICY_OLDEST = 1
CURLOPT_PROGRESSDATA = 10057
CURLOPT_FTP_ALTERNATIVE_TO_USER = 10147
CURLOPT_READFUNCTION = 20012
CURLFORM_CONTENTSLENGTH = 6
CURLE_FTP_PORT_FAILED = 30
CURLFTPSSL_ALL = CURLUSESSL_ALL # alias
CURLOPT_TELNETOPTIONS = 10070
CURLOPT_MAXREDIRS = 68
CURL_FORMADD_DISABLED = 7
CURLOPT_FTP_SKIP_PASV_IP = 137
CURL_LOCK_ACCESS_NONE = 0
CURLFORM_FILE = 10
CURLMOPT_MAXCONNECTS = 6
CURLOPT_CONNECTTIMEOUT_MS = 156
CURLOPT_INTERFACE = 10062
CURLFORM_FILENAME = 16
CURLE_FTP_WEIRD_PASV_REPLY = 13
CURLINFO_END = 7
CURLOPT_SSLCERTPASSWD = CURLOPT_KEYPASSWD # alias
CURLOPT_HTTPHEADER = 10023
CURLOPT_CAPATH = 10097
CURLOPT_FTP_RESPONSE_TIMEOUT = 112
CURLMOPT_SOCKETFUNCTION = 20001
CURLMSG_LAST = 2
CURLINFO_SIZE_DOWNLOAD = 3145736
CURLOPT_SSLENGINE = 10089
CURLOPT_HTTP200ALIASES = 10104
CURLE_CONV_REQD = 76
CURLE_OK = 0
CURL_SSLVERSION_LAST = 4
CURLINFO_PRIVATE = 1048597
CURLOPT_LOW_SPEED_TIME = 20
CURLSHE_NOMEM = 4
CURLOPT_LOW_SPEED_LIMIT = 19
CURLOPT_CONV_FROM_NETWORK_FUNCTION = 20142
CURLOPT_RANGE = 10007
CURLINFO_COOKIELIST = 4194332
CURLM_BAD_HANDLE = 1
CURLINFO_HEADER_SIZE = 2097163
CURLINFO_NUM_CONNECTS = 2097178
CURLCLOSEPOLICY_CALLBACK = 5
CURLFORM_BUFFER = 11
CURLINFO_CONTENT_LENGTH_UPLOAD = 3145744
CURLSOCKTYPE_LAST = 1
CURLOPT_NEW_FILE_PERMS = 159
CURLE_WRITE_ERROR = 23
CURL_NETRC_REQUIRED = 2
CURLINFO_CONTENT_TYPE = 1048594
CURLFORM_CONTENTHEADER = 15
CURLOPT_USERAGENT = 10018
CURLE_UNSUPPORTED_PROTOCOL = 1
CURLOPT_ERRORBUFFER = 10010
CURLIOE_OK = 0
CURLOPT_SEEKFUNCTION = 20167
CURLOPT_IPRESOLVE = 113
CURLOPT_FILETIME = 69
CURLM_LAST = 7
CURL_LOCK_ACCESS_LAST = 3
CURLFTPSSL_CONTROL = CURLUSESSL_CONTROL # alias
CURL_NETRC_LAST = 3
CURLSHOPT_LAST = 6
CURLOPT_SSL_VERIFYPEER = 64
CURL_TIMECOND_LAST = 4
CURLFORM_COPYNAME = 1
CURLINFO_MASK = 1048575 # Variable c_int '1048575'
CURL_CSELECT_ERR = 4 # Variable c_int '4'
CURLSSH_AUTH_HOST = 4 # Variable c_int '4'
CURLPROTO_DICT = 512 # Variable c_int '512'
CURL_READFUNC_PAUSE = 268435457 # Variable c_int '268435457'
CURLPROTO_SFTP = 32 # Variable c_int '32'
CURL_READFUNC_ABORT = 268435456 # Variable c_int '268435456'
CURLE_ALREADY_COMPLETE = 99999 # Variable c_int '99999'
CURLAUTH_GSSNEGOTIATE = 4 # Variable c_int '4'
CURLSSH_AUTH_NONE = 0 # Variable c_int '0'
CURLPROTO_LDAP = 128 # Variable c_int '128'
CURL_VERSION_CONV = 4096 # Variable c_int '4096'
CURLSSH_AUTH_PUBLICKEY = 1 # Variable c_int '1'
CURL_VERSION_ASYNCHDNS = 128 # Variable c_int '128'
CURL_VERSION_LIBZ = 8 # Variable c_int '8'
CURL_GLOBAL_SSL = 1 # Variable c_int '1'
CURLPAUSE_CONT = 0 # Variable c_int '0'
CURLINFO_STRING = 1048576 # Variable c_int '1048576'
CURLAUTH_NTLM = 8 # Variable c_int '8'
CURLPAUSE_RECV_CONT = 0 # Variable c_int '0'
CURL_POLL_IN = 1 # Variable c_int '1'
CURL_CSELECT_IN = 1 # Variable c_int '1'
CURLOPTTYPE_OFF_T = 30000 # Variable c_int '30000'
CURLOPTTYPE_LONG = 0 # Variable c_int '0'
CURLPAUSE_SEND_CONT = 0 # Variable c_int '0'
CURLPROTO_FTPS = 8 # Variable c_int '8'
CURL_POLL_INOUT = 3 # Variable c_int '3'
CURLAUTH_NONE = 0 # Variable c_int '0'
CURLINFO_SLIST = 4194304 # Variable c_int '4194304'
CURLAUTH_ANY = -1 # Variable c_int '-0x000000001'
CURL_VERSION_DEBUG = 64 # Variable c_int '64'
CURLAUTH_BASIC = 1 # Variable c_int '1'
CURL_POLL_OUT = 2 # Variable c_int '2'
CURL_VERSION_LARGEFILE = 512 # Variable c_int '512'
CURLINFO_TYPEMASK = 15728640 # Variable c_int '15728640'
CURL_GLOBAL_NOTHING = 0 # Variable c_int '0'
CURLPROTO_SCP = 16 # Variable c_int '16'
CURL_GLOBAL_WIN32 = 2 # Variable c_int '2'
CURLPROTO_ALL = -1 # Variable c_int '-0x000000001'
CURLPROTO_FTP = 4 # Variable c_int '4'
CURLOPTTYPE_OBJECTPOINT = 10000 # Variable c_int '10000'
CURL_IPRESOLVE_WHATEVER = 0 # Variable c_int '0'
CURLPROTO_HTTPS = 2 # Variable c_int '2'
CURLPROTO_TELNET = 64 # Variable c_int '64'
CURL_VERSION_NTLM = 16 # Variable c_int '16'
CURLPAUSE_SEND = 4 # Variable c_int '4'
CURL_VERSION_IPV6 = 1 # Variable c_int '1'
CURLINFO_DOUBLE = 3145728 # Variable c_int '3145728'
CURLPROTO_TFTP = 2048 # Variable c_int '2048'
CURL_MAX_WRITE_SIZE = 16384 # Variable c_int '16384'
CURL_VERSION_SSPI = 2048 # Variable c_int '2048'
CURLSSH_AUTH_PASSWORD = 2 # Variable c_int '2'
CURL_IPRESOLVE_V6 = 2 # Variable c_int '2'
CURL_IPRESOLVE_V4 = 1 # Variable c_int '1'
CURLSSH_AUTH_KEYBOARD = 8 # Variable c_int '8'
CURLPAUSE_ALL = 5 # Variable c_int '5'
CURL_POLL_REMOVE = 4 # Variable c_int '4'
CURL_POLL_NONE = 0 # Variable c_int '0'
CURLOPTTYPE_FUNCTIONPOINT = 20000 # Variable c_int '20000'
CURLPAUSE_RECV = 1 # Variable c_int '1'
CURLAUTH_ANYSAFE = -2 # Variable c_int '-0x000000002'
CURLAUTH_DIGEST = 2 # Variable c_int '2'
CURL_CSELECT_OUT = 2 # Variable c_int '2'
CURL_ERROR_SIZE = 256 # Variable c_int '256'
CURL_WRITEFUNC_PAUSE = 268435457 # Variable c_int '268435457'
CURLINFO_LONG = 2097152 # Variable c_int '2097152'
CURL_FORMAT_OFF_T = '%lld' # Variable STRING '(const char*)"%lld"'
CURLPROTO_HTTP = 1 # Variable c_int '1'
CURLPROTO_FILE = 1024 # Variable c_int '1024'
CURL_VERSION_KERBEROS4 = 2 # Variable c_int '2'
CURL_VERSION_IDN = 1024 # Variable c_int '1024'
CURL_VERSION_SSL = 4 # Variable c_int '4'
CURL_VERSION_GSSNEGOTIATE = 32 # Variable c_int '32'
CURL_VERSION_SPNEGO = 256 # Variable c_int '256'
CURLPROTO_LDAPS = 256 # Variable c_int '256'
CURL = c_void_p
__off_t = c_long
off_t = __off_t
curl_off_t = off_t
curl_socket_t = c_int
class curl_slist(Structure):
    pass
curl_slist._fields_ = [
        ('data', STRING),
        ('next', POINTER(curl_slist)),
    ]

class curl_httppost(Structure):
    pass
curl_httppost._fields_ = [
        ('next', POINTER(curl_httppost)),
        ('name', STRING),
        ('namelength', c_long),
        ('contents', STRING),
        ('contentslength', c_long),
        ('buffer', STRING),
        ('bufferlength', c_long),
        ('contenttype', STRING),
        ('contentheader', POINTER(curl_slist)),
        ('more', POINTER(curl_httppost)),
        ('flags', c_long),
        ('showfilename', STRING),
        ('userp', c_void_p),
    ]
curl_progress_callback = CFUNCTYPE(c_int, c_void_p, c_double, c_double, c_double, c_double)
size_t = c_uint
curl_write_callback = CFUNCTYPE(size_t, STRING, size_t, size_t, c_void_p)
curl_seek_callback = CFUNCTYPE(c_int, c_void_p, curl_off_t, c_int)
curl_read_callback = CFUNCTYPE(size_t, STRING, size_t, size_t, c_void_p)

# values for enumeration 'curlsocktype'
curlsocktype = c_int # enum
curl_sockopt_callback = CFUNCTYPE(c_int, c_void_p, curl_socket_t, curlsocktype)
class curl_sockaddr(Structure):
    pass
class sockaddr(Structure):
    pass
sa_family_t = c_ushort
sockaddr._fields_ = [
    ('sa_family', sa_family_t),
    ('sa_data', c_char * 14),
]
curl_sockaddr._fields_ = [
    ('family', c_int),
    ('socktype', c_int),
    ('protocol', c_int),
    ('addrlen', c_uint),
    ('addr', sockaddr),
]
curl_opensocket_callback = CFUNCTYPE(curl_socket_t, c_void_p, curlsocktype, POINTER(curl_sockaddr))
curl_passwd_callback = CFUNCTYPE(c_int, c_void_p, STRING, STRING, c_int)

# values for enumeration 'curlioerr'
curlioerr = c_int # enum

# values for enumeration 'curliocmd'
curliocmd = c_int # enum
curl_ioctl_callback = CFUNCTYPE(curlioerr, POINTER(CURL), c_int, c_void_p)
curl_malloc_callback = CFUNCTYPE(c_void_p, size_t)
curl_free_callback = CFUNCTYPE(None, c_void_p)
curl_realloc_callback = CFUNCTYPE(c_void_p, c_void_p, size_t)
curl_strdup_callback = CFUNCTYPE(STRING, STRING)
curl_calloc_callback = CFUNCTYPE(c_void_p, size_t, size_t)

# values for enumeration 'curl_infotype'
curl_infotype = c_int # enum
curl_debug_callback = CFUNCTYPE(c_int, POINTER(CURL), curl_infotype, STRING, size_t, c_void_p)

# values for enumeration 'CURLcode'
CURLcode = c_int # enum
curl_conv_callback = CFUNCTYPE(CURLcode, STRING, size_t)
curl_ssl_ctx_callback = CFUNCTYPE(CURLcode, POINTER(CURL), c_void_p, c_void_p)

# values for enumeration 'curl_proxytype'
curl_proxytype = c_int # enum

# values for enumeration 'curl_ftpccc'
curl_ftpccc = c_int # enum

# values for enumeration 'curl_ftpauth'
curl_ftpauth = c_int # enum

# values for enumeration 'curl_ftpmethod'
curl_ftpmethod = c_int # enum

# values for enumeration 'CURLoption'
CURLoption = c_int # enum

# values for enumeration 'CURL_NETRC_OPTION'
CURL_NETRC_OPTION = c_int # enum

# values for enumeration 'curl_TimeCond'
curl_TimeCond = c_int # enum

# values for enumeration 'CURLformoption'
CURLformoption = c_int # enum
class curl_forms(Structure):
    pass
curl_forms._fields_ = [
    ('option', CURLformoption),
    ('value', STRING),
]

# values for enumeration 'CURLFORMcode'
CURLFORMcode = c_int # enum
curl_formget_callback = CFUNCTYPE(size_t, c_void_p, STRING, size_t)

# values for enumeration 'CURLINFO'
CURLINFO = c_int # enum

# values for enumeration 'curl_closepolicy'
curl_closepolicy = c_int # enum

# values for enumeration 'curl_lock_data'
curl_lock_data = c_int # enum

# values for enumeration 'curl_lock_access'
curl_lock_access = c_int # enum
curl_lock_function = CFUNCTYPE(None, POINTER(CURL), curl_lock_data, curl_lock_access, c_void_p)
curl_unlock_function = CFUNCTYPE(None, POINTER(CURL), curl_lock_data, c_void_p)
CURLSH = c_void_p

# values for enumeration 'CURLSHcode'
CURLSHcode = c_int # enum

# values for enumeration 'CURLSHoption'
CURLSHoption = c_int # enum

# values for enumeration 'CURLversion'
CURLversion = c_int # enum

array_of_string = POINTER(STRING)

def __iter__(self):
    i = 0
    while self[i]:
        yield self[i]
        i += 1

array_of_string.__iter__ = __iter__
class curl_version_info_data(Structure):
    _fields_ = [
        ('age', CURLversion),
        ('version', STRING),
        ('version_num', c_uint),
        ('host', STRING),
        ('features', c_int),
        ('ssl_version', STRING),
        ('ssl_version_num', c_long),
        ('libz_version', STRING),
        ('protocols', array_of_string),
        ('ares', STRING),
        ('ares_num', c_int),
        ('libidn', STRING),
        ('iconv_ver_num', c_int),
        ('libssh_version', STRING),
    ]
CURLM = c_void_p

# values for enumeration 'CURLMcode'
CURLMcode = c_int # enum

# values for enumeration 'CURLMSG'
CURLMSG = c_int # enum
class CURLMsg(Structure):
    pass
class N7CURLMsg4DOT_49E(Union):
    pass
N7CURLMsg4DOT_49E._fields_ = [
    ('whatever', c_void_p),
    ('result', CURLcode),
]
CURLMsg._fields_ = [
    ('msg', CURLMSG),
    ('easy_handle', POINTER(CURL)),
    ('data', N7CURLMsg4DOT_49E),
]
curl_socket_callback = CFUNCTYPE(c_int, POINTER(CURL), curl_socket_t, c_int, c_void_p, c_void_p)
curl_multi_timer_callback = CFUNCTYPE(c_int, POINTER(CURLM), c_long, c_void_p)

class fd_set(Structure):
    _fields_ = [
        ('count', c_uint),
        ('fd', POINTER(c_int * 64))
    ]

# values for enumeration 'CURLMoption'
CURLMoption = c_int # enum
__all__ = ['CURLOPT_HTTP_TRANSFER_DECODING', 'CURLOPT_FTP_SSL_CCC',
           'CURL_FORMADD_INCOMPLETE', 'CURLINFO_SPEED_DOWNLOAD',
           'CURLOPT_SSL_CIPHER_LIST', 'CURLFTPMETHOD_NOCWD',
           'CURLM_UNKNOWN_OPTION', 'CURLFORM_END',
           'curl_multi_timer_callback', 'CURLINFO_MASK',
           'CURLFTPSSL_CONTROL', 'curl_usessl',
           'CURLINFO_SSL_DATA_OUT', 'CURLINFO_LASTONE',
           'CURLOPT_FORBID_REUSE', 'CURLFTPSSL_ALL',
           'CURL_FORMADD_NULL', 'CURLIOCMD_NOP',
           'CURLCLOSEPOLICY_CALLBACK', 'CURLOPT_PUT', 'curl_sockaddr',
           'CURLE_FTP_COULDNT_SET_BINARY', 'CURLE_PARTIAL_FILE',
           'CURLINFO_SIZE_DOWNLOAD', 'CURLOPT_RANGE',
           'CURL_POLL_NONE', 'CURLINFO_REDIRECT_COUNT',
           'CURLVERSION_FOURTH', 'CURLOPT_MAXREDIRS',
           'CURL_LOCK_DATA_COOKIE', 'CURLOPT_FTPAPPEND',
           'CURLOPT_FILE', 'curl_multi_socket', 'curl_seek_callback',
           'CURLE_OBSOLETE', 'CURL_READFUNC_PAUSE',
           'CURLINFO_LASTSOCKET', 'CURLOPT_PROTOCOLS',
           'CURLE_SEND_FAIL_REWIND', 'CURL_TIMECOND_IFMODSINCE',
           'CURLOPT_PROXYAUTH', 'CURLE_UNSUPPORTED_PROTOCOL',
           'CURLE_SSL_SHUTDOWN_FAILED', 'CURLOPT_DNS_CACHE_TIMEOUT',
           'CURLOPT_WRITEINFO', 'CURLSHOPT_LAST',
           'CURLPAUSE_SEND_CONT', 'CURLOPT_TIMEOUT_MS',
           'CURLOPT_FTP_RESPONSE_TIMEOUT', 'CURLOPT_USE_SSL',
           'CURLPROTO_DICT', 'CURLE_LOGIN_DENIED', 'CURLOPT_PROXY',
           'CURLE_BAD_DOWNLOAD_RESUME', 'CURLOPT_NETRC',
           'CURLE_SSL_ENGINE_NOTFOUND', 'CURLFTPAUTH_DEFAULT',
           'CURLINFO_NUM_CONNECTS', 'CURLPROTO_SFTP',
           'CURL_LOCK_DATA_NONE', 'CURL_MAX_WRITE_SIZE',
           'CURLINFO_HEADER_IN', 'CURLE_OBSOLETE29',
           'CURLE_OBSOLETE24', 'CURLE_OBSOLETE20', 'CURLOPT_POST',
           'CURLINFO_SSL_VERIFYRESULT', 'curl_formget_callback',
           'CURLOPT_TIMECONDITION', 'CURLOPT_SSLVERSION',
           'CURLFORM_STREAM', 'CURLOPT_SHARE', 'CURLINFO_OS_ERRNO',
           'CURLOPT_MAXFILESIZE_LARGE', 'CURL_SSLVERSION_LAST',
           'CURL_READFUNC_ABORT', 'CURLOPT_SEEKFUNCTION',
           'CURL_SSLVERSION_DEFAULT', 'CURLINFO_PROXYAUTH_AVAIL',
           'CURLOPT_URL', 'CURLMcode', 'CURLOPT_RESUME_FROM',
           'CURLM_LAST', 'CURLE_TELNET_OPTION_SYNTAX',
           'CURL_HTTP_VERSION_NONE', 'CURLOPT_SSH_PUBLIC_KEYFILE',
           'CURLOPT_SSLENGINE', 'CURLE_ALREADY_COMPLETE',
           'CURLOPT_FTP_ALTERNATIVE_TO_USER', 'CURLAUTH_GSSNEGOTIATE',
           'CURLE_CONV_REQD', 'CURLINFO_REDIRECT_URL',
           'CURL_HTTP_VERSION_LAST', 'CURLOPT_IOCTLDATA',
           'CURL_GLOBAL_DEFAULT', 'CURLE_OBSOLETE50',
           'CURLOPT_NOPROGRESS', 'CURLE_OBSOLETE57', 'CURLE_AGAIN',
           'CURLPROTO_LDAP', 'curl_unlock_function',
           'CURLOPT_IPRESOLVE', 'CURLOPT_CRLF', 'CURLFORM_BUFFERPTR',
           'CURLOPT_SSLCERTTYPE', 'CURL_VERSION_CONV',
           'CURLE_LDAP_CANNOT_BIND', 'CURLINFO_DATA_IN',
           'CURLE_FILE_COULDNT_READ_FILE', 'curl_lock_data',
           'curl_ioctl_callback', 'CURLE_SSH',
           'CURLOPT_SSL_SESSIONID_CACHE', 'CURLINFO_PRIVATE',
           'CURL_LOCK_DATA_DNS', 'sa_family_t', 'CURLFTPAUTH_LAST',
           'CURL_VERSION_LIBZ', 'off_t', 'CURLINFO_HTTP_CONNECTCODE',
           'CURLOPT_NEW_FILE_PERMS', 'CURLOPT_LOCALPORTRANGE',
           'CURLE_WRITE_ERROR', 'CURLOPT_CAINFO', 'CURLPROXY_HTTP',
           'CURL_LOCK_DATA_LAST', 'CURLFORM_LASTENTRY',
           'CURLCLOSEPOLICY_NONE', 'CURLOPT_CONNECTTIMEOUT',
           'CURLE_HTTP_RETURNED_ERROR', 'CURLOPT_SSL_CTX_FUNCTION',
           'CURLVERSION_FIRST', 'CURLSSH_AUTH_PUBLICKEY',
           'CURLE_GOT_NOTHING', 'CURLFTPMETHOD_DEFAULT',
           'CURLE_LDAP_INVALID_URL', 'CURL_GLOBAL_SSL',
           'CURLPAUSE_CONT', 'CURLOPT_KRB4LEVEL',
           'CURLMOPT_SOCKETDATA', 'CURLOPT_TIMEOUT',
           'CURLE_FTP_COULDNT_USE_REST', 'CURL_FORMADD_LAST',
           'curl_strdup_callback', 'CURLOPT_HTTPHEADER',
           'CURLINFO_STRING', 'CURLE_MALFORMAT_USER', 'size_t',
           'CURLMOPT_SOCKETFUNCTION', 'CURLE_UNKNOWN_TELNET_OPTION',
           'CURLoption', 'CURLAUTH_NTLM', 'CURL_VERSION_ASYNCHDNS',
           'CURLOPT_SSL_CTX_DATA', 'CURLINFO_REDIRECT_TIME',
           'CURL_TIMECOND_LAST', 'CURLPAUSE_RECV_CONT',
           'CURLSHOPT_LOCKFUNC', 'CURLOPT_TCP_NODELAY',
           'CURLOPT_FTP_SSL', 'CURLE_BAD_CONTENT_ENCODING',
           'CURLINFO_REQUEST_SIZE', 'CURLE_OBSOLETE16',
           'CURL_POLL_INOUT', 'CURLE_OBSOLETE10',
           'CURLOPT_HTTPPROXYTUNNEL', 'CURLE_OBSOLETE12',
           'CURLOPT_HTTP_CONTENT_DECODING', 'CURLAUTH_NONE',
           'CURLOPT_IGNORE_CONTENT_LENGTH', 'CURLSHOPT_USERDATA',
           'CURLE_FTP_ACCESS_DENIED', 'CURLINFO_SSL_ENGINES',
           'CURLINFO_TEXT', 'CURL_CSELECT_IN', 'CURLOPT_FTP_USE_EPSV',
           'CURLINFO_RESPONSE_CODE', 'CURLE_SEND_ERROR',
           'CURLOPT_CONV_TO_NETWORK_FUNCTION',
           'CURLE_FTP_WEIRD_USER_REPLY',
           'CURLINFO_CONTENT_LENGTH_DOWNLOAD', 'CURLINFO_FILETIME',
           'CURLINFO_HEADER_SIZE', 'CURLE_BAD_PASSWORD_ENTERED',
           'CURLE_FTP_WEIRD_PASS_REPLY', 'CURLOPT_TELNETOPTIONS',
           'CURLOPT_HEADERDATA', 'CURLE_FTP_CANT_GET_HOST',
           'CURLE_OK', 'CURLE_FTP_PARTIAL_FILE',
           'CURLM_CALL_MULTI_SOCKET', 'CURLOPT_PREQUOTE',
           'CURLMOPT_TIMERFUNCTION', 'CURLAUTH_ANY',
           'curl_lock_access', 'CURLOPT_FTP_SKIP_PASV_IP',
           'CURLUSESSL_CONTROL', 'CURLE_RECV_ERROR',
           'CURLOPTTYPE_LONG', 'CURLE_READ_ERROR',
           'CURLOPT_FAILONERROR', 'CURLPROXY_SOCKS4A', 'CURLSHoption',
           'curl_opensocket_callback', 'CURLSSH_AUTH_HOST',
           'CURLOPT_DEBUGDATA', 'CURLE_REMOTE_ACCESS_DENIED',
           'CURLOPT_POSTFIELDSIZE', 'CURLOPT_UPLOAD',
           'CURLOPT_SSLENGINE_DEFAULT', 'CURLOPT_FTP_ACCOUNT',
           'CURLOPT_COOKIESESSION', 'CURL_FORMADD_ILLEGAL_ARRAY',
           'CURLFORM_NOTHING', 'CURLE_FTP_QUOTE_ERROR',
           'CURLE_REMOTE_FILE_NOT_FOUND', 'CURLOPT_NOSIGNAL',
           'CURLOPT_SSLCERTPASSWD', 'CURLOPT_SOCKOPTFUNCTION',
           'CURLFORM_CONTENTTYPE', 'CURLINFO_TOTAL_TIME',
           'CURLINFO_SLIST', 'CURLCLOSEPOLICY_LAST', 'CURL',
           'CURLE_LIBRARY_NOT_FOUND', 'CURLOPT_NETRC_FILE',
           'CURLSHE_INVALID', 'CURLE_OPERATION_TIMEOUTED',
           'CURLOPT_FTPSSLAUTH', 'CURLOPT_NEW_DIRECTORY_PERMS',
           'CURLIOE_UNKNOWNCMD', 'curl_socket_t', 'curl_off_t',
           'CURLMSG_LAST', 'CURL_VERSION_DEBUG', 'CURLOPT_BUFFERSIZE',
           'CURLM_OK', 'CURL_HTTP_VERSION_1_1', 'CURLOPT_COOKIEFILE',
           'CURLPROTO_HTTPS', 'CURLFORM_CONTENTSLENGTH',
           'CURLOPT_CONV_FROM_NETWORK_FUNCTION', 'CURLAUTH_BASIC',
           'curl_proxytype', 'CURL_VERSION_NTLM',
           'curl_realloc_callback', 'CURLE_FTP_WEIRD_PASV_REPLY',
           'curl_forms', 'CURLM', 'CURLINFO', 'CURL_VERSION_IPV6',
           'curl_free_callback', 'CURL_POLL_OUT',
           'CURLFORM_CONTENTHEADER', 'CURLFTPAUTH_TLS',
           'CURLSHOPT_SHARE', 'CURL_WRITEFUNC_PAUSE',
           'CURLCLOSEPOLICY_SLOWEST', 'CURLM_BAD_EASY_HANDLE',
           'CURL_HTTP_VERSION_1_0', 'CURL_LOCK_DATA_SHARE',
           'CURLINFO_COOKIELIST', 'CURLE_SSL_CACERT',
           'CURL_FORMADD_DISABLED', 'CURLOPT_SSH_PRIVATE_KEYFILE',
           'CURLINFO_TYPEMASK', 'CURLVERSION_LAST',
           'CURLINFO_CONNECT_TIME', 'CURLOPT_SSLCERT',
           'CURLSOCKTYPE_LAST', 'CURLE_URL_MALFORMAT',
           'curl_TimeCond', 'CURLUSESSL_ALL', 'CURLOPT_KRBLEVEL',
           'CURL_LOCK_ACCESS_LAST', 'CURLE_TFTP_EXISTS',
           'CURLOPT_FTPLISTONLY', 'CURLPROTO_SCP', 'CURLE_OBSOLETE40',
           'CURLE_OBSOLETE46', 'CURLE_OBSOLETE44', 'CURLOPT_PORT',
           'curl_debug_callback', 'CURLOPT_DEBUGFUNCTION',
           'CURLPROXY_SOCKS5', 'curl_easy_setopt',
           'CURLOPT_RANDOM_FILE', 'CURLAUTH_DIGEST', 'CURLPROTO_ALL',
           'curl_passwd_callback', 'CURLPROTO_FTP',
           'CURLINFO_HTTPAUTH_AVAIL', 'CURLSHOPT_UNLOCKFUNC',
           'CURLIOCMD_LAST', 'CURLMSG_DONE', 'CURLFORMcode',
           'curl_share_setopt', 'CURL_TIMECOND_IFUNMODSINCE',
           'CURLSHcode', 'CURLMOPT_PIPELINING', 'curl_write_callback',
           'N7CURLMsg4DOT_49E', 'CURLFTPMETHOD_LAST', 'CURLSHE_NOMEM',
           'CURLOPT_COOKIEJAR', 'CURL_NETRC_IGNORED',
           'CURL_VERSION_SSPI', 'CURLE_FTP_COULDNT_RETR_FILE',
           'CURLE_BAD_CALLING_ORDER', 'CURLFTPSSL_CCC_ACTIVE',
           'CURL_LOCK_ACCESS_SHARED', 'CURLOPT_FTP_FILEMETHOD',
           'CURLOPTTYPE_OBJECTPOINT', 'CURLOPT_CLOSEPOLICY',
           'CURLOPT_EGDSOCKET', 'CURL_IPRESOLVE_WHATEVER',
           'CURLE_FUNCTION_NOT_FOUND', 'CURLFORM_PTRNAME',
           'CURLMOPT_MAXCONNECTS', 'CURLOPT_INFILESIZE',
           'CURLVERSION_THIRD', 'CURL_SOCKET_BAD',
           'CURLE_FTP_CANT_RECONNECT', 'CURLFORM_ARRAY',
           'curl_socket_callback', 'CURLE_SSL_CERTPROBLEM',
           'CURLOPT_INTERFACE', 'CURLcode', 'CURLOPT_FTPPORT',
           'CURLversion', 'CURL_NETRC_REQUIRED',
           'CURLOPT_MAX_RECV_SPEED_LARGE', 'CURL_POLL_IN',
           'CURLE_SSL_PEER_CERTIFICATE', 'CURLOPT_LOCALPORT',
           'CURLE_HTTP_POST_ERROR', 'CURLFTPMETHOD_MULTICWD',
           'CURLPROTO_TELNET', 'CURLOPT_DNS_USE_GLOBAL_CACHE',
           'CURLSHOPT_UNSHARE', 'CURLOPT_USERAGENT',
           'CURLOPT_LASTENTRY', 'CURLE_INTERFACE_FAILED',
           'CURLOPT_COOKIELIST', 'CURLIOE_OK',
           'CURLE_FTP_PORT_FAILED', 'CURLOPT_DIRLISTONLY',
           'CURLPAUSE_SEND', 'CURLFTPAUTH_SSL',
           'CURLE_SSL_CONNECT_ERROR', 'CURLOPT_TRANSFERTEXT',
           'CURLE_FTP_WRITE_ERROR', 'CURL_SSLVERSION_TLSv1',
           'CURL_FORMADD_UNKNOWN_OPTION',
           'CURLOPT_CONV_FROM_UTF8_FUNCTION',
           'CURLOPT_RESUME_FROM_LARGE', 'CURLOPT_CAPATH',
           'CURLINFO_STARTTRANSFER_TIME', 'CURLOPT_INFILESIZE_LARGE',
           'CURLSOCKTYPE_IPCXN', 'CURLOPT_MAXFILESIZE',
           'CURL_VERSION_LARGEFILE', 'CURLOPT_POSTFIELDS',
           'curl_ftpccc', 'CURLINFO_FTP_ENTRY_PATH',
           'CURLE_HTTP_PORT_FAILED', 'CURLE_FTP_COULDNT_SET_TYPE',
           'CURLE_URL_MALFORMAT_USER', 'CURLM_OUT_OF_MEMORY',
           'CURLOPT_PROXYPORT', 'CURL_NETRC_LAST',
           'curl_sockopt_callback', 'CURLE_SSL_CACERT_BADFILE',
           'CURLOPT_POSTFIELDSIZE_LARGE', 'curl_closepolicy',
           'CURLE_LDAP_SEARCH_FAILED', 'CURLOPT_SSLKEY',
           'CURLE_REMOTE_DISK_FULL', 'CURLE_SHARE_IN_USE',
           'CURL_FORMADD_OK', 'CURLE_FTP_SSL_FAILED',
           'CURLOPT_HTTPGET', 'CURLE_TFTP_PERM', 'CURLOPT_POST301',
           'CURLSHE_IN_USE', 'curl_ftpauth', 'CURLFORM_FILE',
           'CURLOPT_SSL_VERIFYHOST', 'CURLINFO_PRETRANSFER_TIME',
           'CURLOPT_REFERER', 'CURLOPT_INFILE',
           'CURLE_USE_SSL_FAILED', 'CURLFORM_PTRCONTENTS',
           'CURLINFO_DOUBLE', 'CURLSHE_BAD_OPTION',
           'CURLINFO_EFFECTIVE_URL', 'CURLCLOSEPOLICY_LEAST_TRAFFIC',
           'CURLOPT_APPEND', 'CURLFORM_OBSOLETE',
           'CURLMOPT_LASTENTRY', 'CURLE_BAD_FUNCTION_ARGUMENT',
           'CURLPROTO_TFTP', 'CURLOPT_MAXCONNECTS',
           'CURLE_OPERATION_TIMEDOUT', 'CURLOPT_ERRORBUFFER',
           'CURLOPT_SSLKEYPASSWD', 'CURLSSH_AUTH_KEYBOARD',
           'CURLOPT_SSLKEYTYPE', 'CURLINFO_SSL_DATA_IN',
           'CURLOPT_SSH_AUTH_TYPES', 'CURLINFO_HTTP_CODE',
           'CURLFTPSSL_NONE', 'CURLCLOSEPOLICY_LEAST_RECENTLY_USED',
           'CURLVERSION_NOW', 'CURLOPT_WRITEDATA',
           'CURLOPT_REDIR_PROTOCOLS', 'CURLFTPSSL_CCC_LAST',
           'CURLE_ABORTED_BY_CALLBACK', 'CURLOPT_KEYPASSWD',
           'CURL_FORMADD_OPTION_TWICE', 'CURL_SSLVERSION_SSLv3',
           'CURL_SSLVERSION_SSLv2', 'curl_multi_setopt',
           'CURLOPT_UNRESTRICTED_AUTH', 'CURLSSH_AUTH_NONE',
           'CURLE_PEER_FAILED_VERIFICATION', 'CURLCLOSEPOLICY_OLDEST',
           'CURLE_FTP_COULDNT_SET_ASCII', 'CURLOPT_NOBODY',
           'CURLOPT_SEEKDATA', 'CURLM_CALL_MULTI_PERFORM',
           'CURLOPT_CONNECT_ONLY', 'CURLIOE_FAILRESTART',
           'CURLPROTO_FTPS', 'CURLE_RANGE_ERROR',
           'CURLOPT_LOW_SPEED_TIME', 'CURLOPT_FTP_USE_EPRT',
           'CURLINFO_NONE', 'CURLOPT_FILETIME', 'CURLE_CONV_FAILED',
           'CURLE_COULDNT_CONNECT', 'CURLOPT_IOCTLFUNCTION',
           'CURL_LOCK_ACCESS_SINGLE', 'CURLE_FTP_BAD_DOWNLOAD_RESUME',
           'CURLE_OUT_OF_MEMORY', 'CURLFORM_FILENAME',
           'CURLSSH_AUTH_ANY', 'CURLSH', 'CURLFTPSSL_CCC_NONE',
           'curl_ssl_ctx_callback', 'CURL_TIMECOND_NONE',
           'CURLE_TFTP_NOTFOUND', 'CURLE_FILESIZE_EXCEEDED',
           'CURLOPT_HEADERFUNCTION', 'CURLIOE_LAST',
           'CURLE_TFTP_DISKFULL', 'CURLSSH_AUTH_PASSWORD',
           'CURLSHOPT_NONE', 'CURLOPT_PRIVATE', 'CURLOPT_AUTOREFERER',
           'curl_httppost', 'CURLOPT_PROGRESSDATA',
           'CURLOPT_FTP_CREATE_MISSING_DIRS', 'CURLOPT_HTTPPOST',
           'CURLE_FTP_COULDNT_STOR_FILE', 'CURLMsg',
           'CURLFTPSSL_LAST', 'CURL_LOCK_ACCESS_NONE',
           'CURLOPT_SSH_HOST_PUBLIC_KEY_MD5', 'CURL_IPRESOLVE_V6',
           'CURL_IPRESOLVE_V4', 'CURLE_TFTP_ILLEGAL',
           'CURLOPT_SSL_VERIFYPEER', 'CURLOPT_SOCKOPTDATA',
           'CURLE_HTTP_RANGE_ERROR', 'CURLINFO_END',
           'CURL_VERSION_IDN', 'CURLE_SSL_ENGINE_SETFAILED',
           'CURLOPT_STDERR', 'CURLOPT_FRESH_CONNECT',
           'CURL_FORMADD_MEMORY', 'curl_malloc_callback',
           'CURLE_UPLOAD_FAILED', 'curl_ftpssl',
           'CURLOPT_WRITEHEADER', 'CURLINFO_NAMELOOKUP_TIME',
           'CURLE_FTP_WEIRD_227_FORMAT', 'CURLOPT_READDATA',
           '__off_t', 'CURLPAUSE_ALL', 'CURLE_REMOTE_FILE_EXISTS',
           'CURL_SOCKET_TIMEOUT', 'curl_ftpmethod',
           'CURL_GLOBAL_WIN32', 'CURLIOCMD_RESTARTREAD',
           'CURL_POLL_REMOVE', 'CURLE_FTP_USER_PASSWORD_INCORRECT',
           'CURLOPT_VERBOSE', 'curliocmd', 'CURLSHE_OK',
           'CURLE_SSL_ENGINE_INITFAILED',
           'CURLOPT_PROXY_TRANSFER_MODE', 'CURLE_TOO_MANY_REDIRECTS',
           'CURLMoption', 'CURLE_OBSOLETE32', 'CURLPROXY_SOCKS4',
           'CURL_CSELECT_ERR', 'CURLE_COULDNT_RESOLVE_PROXY',
           'CURLOPTTYPE_FUNCTIONPOINT', 'CURLOPT_COOKIE',
           'CURLOPT_OPENSOCKETFUNCTION', 'CURLUSESSL_NONE',
           'CURLPAUSE_RECV', 'CURLFORM_BUFFER',
           'CURLOPT_READFUNCTION', 'curl_version_info_data',
           'CURLFTPSSL_CCC_PASSIVE', 'CURLOPT_HTTPAUTH',
           'CURLOPT_FOLLOWLOCATION', 'CURLFORM_NAMELENGTH',
           'CURLAUTH_ANYSAFE', 'curl_progress_callback',
           'CURLOPT_HEADER', 'CURL_LOCK_DATA_CONNECT',
           'CURLFORM_COPYCONTENTS', 'CURLE_TFTP_UNKNOWNID',
           'CURLOPT_LOW_SPEED_LIMIT', 'curlioerr',
           'CURLINFO_CONTENT_TYPE', 'CURLINFO_HEADER_OUT',
           'CURLOPTTYPE_OFF_T', 'CURLM_BAD_HANDLE',
           'CURLOPT_PROXYUSERPWD', 'CURLE_FTP_COULDNT_GET_SIZE',
           'CURLOPT_ENCODING', 'CURLOPT_HTTP_VERSION',
           'CURLOPT_TIMEVALUE', 'curlsocktype', 'CURLOPT_POSTQUOTE',
           'CURL_CSELECT_OUT', 'CURL_ERROR_SIZE', 'CURLOPT_USERPWD',
           'CURLOPT_OPENSOCKETDATA', 'CURLSHE_LAST',
           'CURLE_SSL_CIPHER', 'CURLE_FAILED_INIT',
           'curl_lock_function', 'CURLMSG',
           'CURLOPT_PROGRESSFUNCTION', 'CURLINFO_LONG',
           'CURLFORM_OBSOLETE2', 'CURLOPT_HTTP200ALIASES',
           'CURLVERSION_SECOND', 'CURLOPT_COPYPOSTFIELDS',
           'CURLINFO_SPEED_UPLOAD', 'CURL_NETRC_OPTION',
           'CURLINFO_DATA_OUT', 'CURLOPT_CONNECTTIMEOUT_MS',
           'CURL_FORMAT_OFF_T', 'CURLINFO_CONTENT_LENGTH_UPLOAD',
           'curl_conv_callback', 'CURLFORM_COPYNAME',
           'CURLPROTO_HTTP', 'CURLOPT_QUOTE', 'CURLPROTO_FILE',
           'CURL_VERSION_KERBEROS4', 'CURLMSG_NONE', 'sockaddr',
           'curl_calloc_callback', 'CURL_GLOBAL_NOTHING',
           'CURLOPT_WRITEFUNCTION', 'CURLE_FTP_WEIRD_SERVER_REPLY',
           'CURLMOPT_TIMERDATA', 'CURLFTPSSL_TRY',
           'curl_easy_getinfo', 'CURLOPT_PROXYTYPE',
           'CURLOPT_MAX_SEND_SPEED_LARGE',
           'CURL_VERSION_GSSNEGOTIATE', 'CURLSSH_AUTH_DEFAULT',
           'CURLE_QUOTE_ERROR', 'CURLE_COULDNT_RESOLVE_HOST',
           'CURLM_BAD_SOCKET', 'CURL_TIMECOND_LASTMOD',
           'CURLUSESSL_TRY', 'CURLINFO_SIZE_UPLOAD',
           'CURLUSESSL_LAST', 'curl_infotype', 'CURLE_OBSOLETE4',
           'CURLE_TFTP_NOSUCHUSER', 'CURLE_HTTP_NOT_FOUND',
           'curl_slist', 'CURL_VERSION_SSL', 'CURLformoption',
           'CURLM_INTERNAL_ERROR', 'CURL_GLOBAL_ALL',
           'CURLFORM_FILECONTENT', 'CURL_NETRC_OPTIONAL',
           'CURLOPT_CUSTOMREQUEST', 'CURLFORM_BUFFERLENGTH',
           'CURL_VERSION_SPNEGO', 'CURLPROXY_SOCKS5_HOSTNAME',
           'curl_read_callback', 'CURLPROTO_LDAPS',
           'CURL_LOCK_DATA_SSL_SESSION', 'CURL_LAST',
           'CURLFTPMETHOD_SINGLECWD']
