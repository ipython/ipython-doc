IPython kernel options
======================

These options can be used in :file:`ipython_kernel_config.py`

IPKernelApp.auto_create : Bool
    Default: `False`

    Whether to create profile dir if it doesn't exist

IPKernelApp.code_to_run : Unicode
    Default: `''`

    Execute the given command string.

IPKernelApp.connection_file : Unicode
    Default: `''`

    JSON file in which to store connection info [default: kernel-<pid>.json]
    
    This file will contain the IP, ports, and authentication key needed to connect
    clients to this kernel. By default, this file will be created in the security dir
    of the current profile, but can be specified by absolute path.


IPKernelApp.control_port : Integer
    Default: `0`

    set the control (ROUTER) port [default: random]

IPKernelApp.copy_config_files : Bool
    Default: `False`

    Whether to install the default config files into the profile dir.
    If a new profile is being created, and IPython contains config files for that
    profile, then they will be staged into the new directory.  Otherwise,
    default config files will be automatically generated.


IPKernelApp.displayhook_class : DottedObjectName
    Default: `'IPython.kernel.zmq.displayhook.ZMQDisplayHook'`

    The importstring for the DisplayHook factory

IPKernelApp.exec_PYTHONSTARTUP : Bool
    Default: `True`

    Run the file referenced by the PYTHONSTARTUP environment
    variable at IPython startup.

IPKernelApp.exec_files : List
    Default: `[]`

    List of files to run at IPython startup.

IPKernelApp.exec_lines : List
    Default: `[]`

    lines of code to run at IPython startup.

IPKernelApp.extensions : List
    Default: `[]`

    A list of dotted module names of IPython extensions to load.

IPKernelApp.extra_config_file : Unicode
    Default: `u''`

    Path to an extra config file to load.
    
    If specified, load this config file in addition to any other IPython config.


IPKernelApp.extra_extension : Unicode
    Default: `''`

    dotted module name of an IPython extension to load.

IPKernelApp.file_to_run : Unicode
    Default: `''`

    A file to be run

IPKernelApp.gui : 'glut'|'gtk'|'gtk3'|'osx'|'pyglet'|'qt'|'qt5'|'tk'|'wx'
    Enable GUI event loop integration with any of ('glut', 'gtk', 'gtk3', 'osx', 'pyglet', 'qt', 'qt5', 'tk', 'wx').

IPKernelApp.hb_port : Integer
    Default: `0`

    set the heartbeat port [default: random]

IPKernelApp.hide_initial_ns : Bool
    Default: `True`

    Should variables loaded at startup (by startup files, exec_lines, etc.)
    be hidden from tools like %who?

IPKernelApp.interrupt : Integer
    Default: `0`

    ONLY USED ON WINDOWS
    Interrupt this process when the parent is signaled.


IPKernelApp.iopub_port : Integer
    Default: `0`

    set the iopub (PUB) port [default: random]

IPKernelApp.ip : Unicode
    Default: `u''`

    Set the kernel's IP address [default localhost].
    If the IP address is something other than localhost, then
    Consoles on other machines will be able to connect
    to the Kernel, so be careful!

IPKernelApp.ipython_dir : Unicode
    Default: `u''`

    
    The name of the IPython directory. This directory is used for logging
    configuration (through profiles), history storage, etc. The default
    is usually $HOME/.ipython. This option can also be specified through
    the environment variable IPYTHONDIR.


IPKernelApp.kernel_class : Type
    Default: `<class 'IPython.kernel.zmq.ipkernel.IPythonKernel'>`

    The Kernel subclass to be used.
    
    This should allow easy re-use of the IPKernelApp entry point
    to configure and launch kernels other than IPython's own.


IPKernelApp.log_datefmt : Unicode
    Default: `'%Y-%m-%d %H:%M:%S'`

    The date format used by logging formatters for %(asctime)s

IPKernelApp.log_format : Unicode
    Default: `'[%(name)s]%(highlevel)s %(message)s'`

    The Logging format template

IPKernelApp.log_level : 0|10|20|30|40|50|'DEBUG'|'INFO'|'WARN'|'ERROR'|'CRITICAL'
    Default: `30`

    Set the log level by value or name.

IPKernelApp.matplotlib : 'auto'|'gtk'|'gtk3'|'inline'|'nbagg'|'notebook'|'osx'|'qt'|'qt4'|'qt5'|'tk'|'wx'
    Configure matplotlib for interactive use with
    the default matplotlib backend.

IPKernelApp.module_to_run : Unicode
    Default: `''`

    Run the module as a script.

IPKernelApp.no_stderr : Bool
    Default: `False`

    redirect stderr to the null device

IPKernelApp.no_stdout : Bool
    Default: `False`

    redirect stdout to the null device

IPKernelApp.outstream_class : DottedObjectName
    Default: `'IPython.kernel.zmq.iostream.OutStream'`

    The importstring for the OutStream factory

IPKernelApp.overwrite : Bool
    Default: `False`

    Whether to overwrite existing config files when copying

IPKernelApp.parent_handle : Integer
    Default: `0`

    kill this process if its parent dies.  On Windows, the argument
    specifies the HANDLE of the parent process, otherwise it is simply boolean.


IPKernelApp.profile : Unicode
    Default: `u'default'`

    The IPython profile to use.

IPKernelApp.pylab : 'auto'|'gtk'|'gtk3'|'inline'|'nbagg'|'notebook'|'osx'|'qt'|'qt4'|'qt5'|'tk'|'wx'
    Pre-load matplotlib and numpy for interactive use,
    selecting a particular matplotlib backend and loop integration.


IPKernelApp.pylab_import_all : Bool
    Default: `True`

    If true, IPython will populate the user namespace with numpy, pylab, etc.
    and an ``import *`` is done from numpy and pylab, when using pylab mode.
    
    When False, pylab mode should not import any names into the user namespace.


IPKernelApp.reraise_ipython_extension_failures : Bool
    Default: `False`

    Reraise exceptions encountered loading IPython extensions?

IPKernelApp.shell_port : Integer
    Default: `0`

    set the shell (ROUTER) port [default: random]

IPKernelApp.stdin_port : Integer
    Default: `0`

    set the stdin (ROUTER) port [default: random]

IPKernelApp.transport : 'tcp'|'ipc'
    Default: `'tcp'`

    No description

IPKernelApp.verbose_crash : Bool
    Default: `False`

    Create a massive crash report when IPython encounters what may be an
    internal error.  The default is to append a short message to the
    usual traceback

IPythonKernel._darwin_app_nap : Bool
    Default: `True`

    Whether to use appnope for compatiblity with OS X App Nap.
    
    Only affects OS X >= 10.9.


IPythonKernel._execute_sleep : Float
    Default: `0.0005`

    No description

IPythonKernel._poll_interval : Float
    Default: `0.05`

    No description

ZMQInteractiveShell.ast_node_interactivity : 'all'|'last'|'last_expr'|'none'
    Default: `'last_expr'`

    
    'all', 'last', 'last_expr' or 'none', specifying which nodes should be
    run interactively (displaying output from expressions).

ZMQInteractiveShell.ast_transformers : List
    Default: `[]`

    
    A list of ast.NodeTransformer subclass instances, which will be applied
    to user input before code is run.


ZMQInteractiveShell.autocall : 0|1|2
    Default: `0`

    
    Make IPython automatically call any callable object even if you didn't
    type explicit parentheses. For example, 'str 43' becomes 'str(43)'
    automatically. The value can be '0' to disable the feature, '1' for
    'smart' autocall, where it is not applied if there are no more
    arguments on the line, and '2' for 'full' autocall, where all callable
    objects are automatically called (even if no arguments are present).


ZMQInteractiveShell.automagic : CBool
    Default: `True`

    
    Enable magic commands to be called without the leading %.


ZMQInteractiveShell.banner1 : Unicode
    Default: `'Python 2.7.9 |Continuum Analytics, Inc.| (default, Dec 15 20...`

    The part of the banner to be printed before the profile

ZMQInteractiveShell.banner2 : Unicode
    Default: `''`

    The part of the banner to be printed after the profile

ZMQInteractiveShell.cache_size : Integer
    Default: `1000`

    
    Set the size of the output cache.  The default is 1000, you can
    change it permanently in your config file.  Setting it to 0 completely
    disables the caching system, and the minimum value accepted is 20 (if
    you provide a value less than 20, it is reset to 0 and a warning is
    issued).  This limit is defined because otherwise you'll spend more
    time re-flushing a too small cache than working


ZMQInteractiveShell.color_info : CBool
    Default: `True`

    
    Use colors for displaying information about objects. Because this
    information is passed through a pager (like 'less'), and some pagers
    get confused with color codes, this capability can be turned off.


ZMQInteractiveShell.colors : 'NoColor'|'LightBG'|'Linux'
    Default: `'LightBG'`

    Set the color scheme (NoColor, Linux, or LightBG).

ZMQInteractiveShell.debug : CBool
    Default: `False`

    No description

ZMQInteractiveShell.deep_reload : CBool
    Default: `False`

    
    Enable deep (recursive) reloading by default. IPython can use the
    deep_reload module which reloads changes in modules recursively (it
    replaces the reload() function, so you don't need to change anything to
    use it). deep_reload() forces a full reload of modules whose code may
    have changed, which the default reload() function does not.  When
    deep_reload is off, IPython will use the normal reload(), but
    deep_reload will still be available as dreload().


ZMQInteractiveShell.disable_failing_post_execute : CBool
    Default: `False`

    Don't call post-execute functions that have failed in the past.

ZMQInteractiveShell.display_page : Bool
    Default: `False`

    If True, anything that would be passed to the pager
    will be displayed as regular output instead.

ZMQInteractiveShell.history_length : Integer
    Default: `10000`

    No description

ZMQInteractiveShell.ipython_dir : Unicode
    Default: `''`

    No description

ZMQInteractiveShell.logappend : Unicode
    Default: `''`

    
    Start logging to the given file in append mode.
    Use `logfile` to specify a log file to **overwrite** logs to.


ZMQInteractiveShell.logfile : Unicode
    Default: `''`

    
    The name of the logfile to use.


ZMQInteractiveShell.logstart : CBool
    Default: `False`

    
    Start logging to the default log file in overwrite mode.
    Use `logappend` to specify a log file to **append** logs to.


ZMQInteractiveShell.multiline_history : CBool
    Default: `True`

    Save multi-line entries as one entry in readline history

ZMQInteractiveShell.object_info_string_level : 0|1|2
    Default: `0`

    No description

ZMQInteractiveShell.pdb : CBool
    Default: `False`

    
    Automatically call the pdb debugger after every exception.


ZMQInteractiveShell.prompt_in1 : Unicode
    Default: `'In [\\#]: '`

    Deprecated, use PromptManager.in_template

ZMQInteractiveShell.prompt_in2 : Unicode
    Default: `'   .\\D.: '`

    Deprecated, use PromptManager.in2_template

ZMQInteractiveShell.prompt_out : Unicode
    Default: `'Out[\\#]: '`

    Deprecated, use PromptManager.out_template

ZMQInteractiveShell.prompts_pad_left : CBool
    Default: `True`

    Deprecated, use PromptManager.justify

ZMQInteractiveShell.quiet : CBool
    Default: `False`

    No description

ZMQInteractiveShell.readline_parse_and_bind : List
    Default: `['tab: complete', '"\\C-l": clear-screen', 'set show-all-if-a...`

    No description

ZMQInteractiveShell.readline_remove_delims : Unicode
    Default: `'-/~'`

    No description

ZMQInteractiveShell.separate_in : SeparateUnicode
    Default: `'\\n'`

    No description

ZMQInteractiveShell.separate_out : SeparateUnicode
    Default: `''`

    No description

ZMQInteractiveShell.separate_out2 : SeparateUnicode
    Default: `''`

    No description

ZMQInteractiveShell.show_rewritten_input : CBool
    Default: `True`

    Show rewritten input, e.g. for autocall.

ZMQInteractiveShell.wildcards_case_sensitive : CBool
    Default: `True`

    No description

ZMQInteractiveShell.xmode : 'Context'|'Plain'|'Verbose'
    Default: `'Context'`

    No description

ProfileDir.location : Unicode
    Default: `u''`

    Set the profile location directly. This overrides the logic used by the
    `profile` option.

Session.buffer_threshold : Integer
    Default: `1024`

    Threshold (in bytes) beyond which an object's buffer should be extracted to avoid pickling.

Session.copy_threshold : Integer
    Default: `65536`

    Threshold (in bytes) beyond which a buffer should be sent without copying.

Session.debug : Bool
    Default: `False`

    Debug output in the Session

Session.digest_history_size : Integer
    Default: `65536`

    The maximum number of digests to remember.
    
    The digest history will be culled when it exceeds this value.


Session.item_threshold : Integer
    Default: `64`

    The maximum number of items for a container to be introspected for custom serialization.
    Containers larger than this are pickled outright.


Session.key : CBytes
    Default: `''`

    execution key, for signing messages.

Session.keyfile : Unicode
    Default: `''`

    path to file containing execution key.

Session.metadata : Dict
    Default: `{}`

    Metadata dictionary, which serves as the default top-level metadata dict for each message.

Session.packer : DottedObjectName
    Default: `'json'`

    The name of the packer for serializing messages.
    Should be one of 'json', 'pickle', or an import name
    for a custom callable serializer.

Session.session : CUnicode
    Default: `u''`

    The UUID identifying this session.

Session.signature_scheme : Unicode
    Default: `'hmac-sha256'`

    The digest scheme used to construct the message signatures.
    Must have the form 'hmac-HASH'.

Session.unpacker : DottedObjectName
    Default: `'json'`

    The name of the unpacker for unserializing messages.
    Only used with custom functions for `packer`.

Session.username : Unicode
    Default: `u'minrk'`

    Username for the Session. Default is your system username.
