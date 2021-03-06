#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xpra
Version  : 4.0.4
Release  : 12
URL      : https://files.pythonhosted.org/packages/13/e7/384922d08d22cc73f63e061107e4ff1bad1c2183f1c00b22fb942fd4a303/xpra-4.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/13/e7/384922d08d22cc73f63e061107e4ff1bad1c2183f1c00b22fb942fd4a303/xpra-4.0.4.tar.gz
Summary  : runs X clients, typically on a remote host, and directs their display to the local machine without losing any state.
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+ LGPL-3.0 MPL-2.0-no-copyleft-exception
Requires: xpra-bin = %{version}-%{release}
Requires: xpra-config = %{version}-%{release}
Requires: xpra-data = %{version}-%{release}
Requires: xpra-license = %{version}-%{release}
Requires: xpra-man = %{version}-%{release}
Requires: xpra-python = %{version}-%{release}
Requires: xpra-python3 = %{version}-%{release}
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : pkgconfig(gdk-3.0)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(py3cairo)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xtst)
BuildRequires : pycairo-dev
BuildRequires : pygobject
BuildRequires : python3-dev

%description
FAQ for xpra
============
http://xpra.org/
For more up to date information.
What is xpra?
-------------

%package bin
Summary: bin components for the xpra package.
Group: Binaries
Requires: xpra-data = %{version}-%{release}
Requires: xpra-config = %{version}-%{release}
Requires: xpra-license = %{version}-%{release}

%description bin
bin components for the xpra package.


%package config
Summary: config components for the xpra package.
Group: Default

%description config
config components for the xpra package.


%package data
Summary: data components for the xpra package.
Group: Data

%description data
data components for the xpra package.


%package license
Summary: license components for the xpra package.
Group: Default

%description license
license components for the xpra package.


%package man
Summary: man components for the xpra package.
Group: Default

%description man
man components for the xpra package.


%package python
Summary: python components for the xpra package.
Group: Default
Requires: xpra-python3 = %{version}-%{release}

%description python
python components for the xpra package.


%package python3
Summary: python3 components for the xpra package.
Group: Default
Requires: python3-core

%description python3
python3 components for the xpra package.


%prep
%setup -q -n xpra-4.0.4
cd %{_builddir}/xpra-4.0.4

%build
## build_prepend content
export CPPFLAGS="${CPPFLAGS} -I/usr/include"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603410591
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build  %{?_smp_mflags}

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xpra
cp %{_builddir}/xpra-4.0.4/COPYING %{buildroot}/usr/share/package-licenses/xpra/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/xpra-4.0.4/html5/LICENSE %{buildroot}/usr/share/package-licenses/xpra/9744cedce099f727b327cd9913a1fdc58a7f5599
cp %{_builddir}/xpra-4.0.4/html5/js/lib/broadway/LICENSE %{buildroot}/usr/share/package-licenses/xpra/90b47d629f432a2f522f4611d02cad7e19173464
cp %{_builddir}/xpra-4.0.4/xpra/gtk_common/gtk2_notifier-LICENSE.txt %{buildroot}/usr/share/package-licenses/xpra/f45ee1c765646813b442ca58de72e20a64a7ddba
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/sysusers.d/xpra.conf

%files
%defattr(-,root,root,-)
/usr/lib/cups/backend/xpraforwarder
/usr/lib/xpra/auth_dialog
/usr/lib/xpra/gnome-open
/usr/lib/xpra/gvfs-open
/usr/lib/xpra/xdg-open

%files bin
%defattr(-,root,root,-)
/usr/bin/xpra
/usr/bin/xpra_Xdummy
/usr/bin/xpra_launcher
/usr/bin/xpra_signal_listener
/usr/bin/xpra_udev_product_version

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/xpra.conf
/usr/lib/udev/rules.d/71-xpra-virtual-pointer.rules

%files data
%defattr(-,root,root,-)
/usr/share/applications/xpra-gui.desktop
/usr/share/applications/xpra-launcher.desktop
/usr/share/applications/xpra-shadow.desktop
/usr/share/applications/xpra.desktop
/usr/share/icons/xpra-mdns.png
/usr/share/icons/xpra-shadow.png
/usr/share/icons/xpra.png
/usr/share/metainfo/xpra.appdata.xml
/usr/share/mime-packages/application-x-xpraconfig.xml
/usr/share/xpra/COPYING
/usr/share/xpra/README
/usr/share/xpra/bell.wav
/usr/share/xpra/content-categories/10_default.conf
/usr/share/xpra/content-type/10_role.conf
/usr/share/xpra/content-type/30_title.conf
/usr/share/xpra/content-type/50_class.conf
/usr/share/xpra/content-type/70_commands.conf
/usr/share/xpra/http-headers/00_nocache.txt
/usr/share/xpra/http-headers/10_content_security_policy.txt
/usr/share/xpra/icons/audio.png
/usr/share/xpra/icons/authentication.png
/usr/share/xpra/icons/bandwidth_limit.png
/usr/share/xpra/icons/bell.png
/usr/share/xpra/icons/browse.png
/usr/share/xpra/icons/browser.png
/usr/share/xpra/icons/bugs.png
/usr/share/xpra/icons/clipboard.png
/usr/share/xpra/icons/close.png
/usr/share/xpra/icons/compressed.png
/usr/share/xpra/icons/connect.png
/usr/share/xpra/icons/disconnected.png
/usr/share/xpra/icons/download.png
/usr/share/xpra/icons/encoding.png
/usr/share/xpra/icons/features.png
/usr/share/xpra/icons/fluxbox.png
/usr/share/xpra/icons/forward.png
/usr/share/xpra/icons/freebsd.png
/usr/share/xpra/icons/gnome-session.png
/usr/share/xpra/icons/gnome.png
/usr/share/xpra/icons/information.png
/usr/share/xpra/icons/kde.png
/usr/share/xpra/icons/keyboard.png
/usr/share/xpra/icons/linux.png
/usr/share/xpra/icons/list.png
/usr/share/xpra/icons/lxde.png
/usr/share/xpra/icons/macos.png
/usr/share/xpra/icons/matchbox.png
/usr/share/xpra/icons/mdns.png
/usr/share/xpra/icons/microphone.png
/usr/share/xpra/icons/minimize.png
/usr/share/xpra/icons/open.png
/usr/share/xpra/icons/openbox.png
/usr/share/xpra/icons/openbsd.png
/usr/share/xpra/icons/opengl.png
/usr/share/xpra/icons/package.png
/usr/share/xpra/icons/picture.png
/usr/share/xpra/icons/printer.png
/usr/share/xpra/icons/quit.png
/usr/share/xpra/icons/raise.png
/usr/share/xpra/icons/reinitialize.png
/usr/share/xpra/icons/retry.png
/usr/share/xpra/icons/sawfish.png
/usr/share/xpra/icons/scaling.png
/usr/share/xpra/icons/screenshot.png
/usr/share/xpra/icons/server-connected.png
/usr/share/xpra/icons/server-notconnected.png
/usr/share/xpra/icons/server.png
/usr/share/xpra/icons/shutdown.png
/usr/share/xpra/icons/slider.png
/usr/share/xpra/icons/speaker-off.png
/usr/share/xpra/icons/speaker.png
/usr/share/xpra/icons/speed.png
/usr/share/xpra/icons/sqlite.png
/usr/share/xpra/icons/start.png
/usr/share/xpra/icons/statistics.png
/usr/share/xpra/icons/ticked-small.png
/usr/share/xpra/icons/timer.png
/usr/share/xpra/icons/toolbox.png
/usr/share/xpra/icons/transfer.png
/usr/share/xpra/icons/transparent.png
/usr/share/xpra/icons/unticked-small.png
/usr/share/xpra/icons/update.png
/usr/share/xpra/icons/upload.png
/usr/share/xpra/icons/user.png
/usr/share/xpra/icons/video.png
/usr/share/xpra/icons/webcam.png
/usr/share/xpra/icons/win32.png
/usr/share/xpra/icons/windowmaker.png
/usr/share/xpra/icons/windows.png
/usr/share/xpra/icons/xpra.png
/usr/share/xpra/icons/xterm.png
/usr/share/xpra/www/LICENSE
/usr/share/xpra/www/LICENSE.gz
/usr/share/xpra/www/connect.html
/usr/share/xpra/www/connect.html.gz
/usr/share/xpra/www/css/bootstrap.css
/usr/share/xpra/www/css/bootstrap.css.gz
/usr/share/xpra/www/css/bootstrap.css.map
/usr/share/xpra/www/css/bootstrap.css.map.gz
/usr/share/xpra/www/css/client.css
/usr/share/xpra/www/css/client.css.gz
/usr/share/xpra/www/css/icon.css
/usr/share/xpra/www/css/icon.css.gz
/usr/share/xpra/www/css/menu-skin.css
/usr/share/xpra/www/css/menu-skin.css.gz
/usr/share/xpra/www/css/menu.css
/usr/share/xpra/www/css/menu.css.gz
/usr/share/xpra/www/css/signin.css
/usr/share/xpra/www/css/signin.css.gz
/usr/share/xpra/www/css/spinner.css
/usr/share/xpra/www/css/spinner.css.gz
/usr/share/xpra/www/default-settings.txt
/usr/share/xpra/www/default-settings.txt.gz
/usr/share/xpra/www/favicon.ico
/usr/share/xpra/www/favicon.ico.gz
/usr/share/xpra/www/favicon.png
/usr/share/xpra/www/icons/close.png
/usr/share/xpra/www/icons/default_cursor.png
/usr/share/xpra/www/icons/empty.png
/usr/share/xpra/www/icons/fullscreen.png
/usr/share/xpra/www/icons/materialicons-regular.ttf
/usr/share/xpra/www/icons/materialicons-regular.ttf.gz
/usr/share/xpra/www/icons/materialicons-regular.woff
/usr/share/xpra/www/icons/materialicons-regular.woff.gz
/usr/share/xpra/www/icons/materialicons-regular.woff2
/usr/share/xpra/www/icons/materialicons-regular.woff2.gz
/usr/share/xpra/www/icons/maximize.png
/usr/share/xpra/www/icons/minimize.png
/usr/share/xpra/www/icons/noicon.png
/usr/share/xpra/www/icons/speaker-buffering.png
/usr/share/xpra/www/icons/speaker-off.png
/usr/share/xpra/www/icons/speaker.png
/usr/share/xpra/www/icons/unfullscreen.png
/usr/share/xpra/www/icons/xpra-logo.png
/usr/share/xpra/www/index.html
/usr/share/xpra/www/index.html.gz
/usr/share/xpra/www/js/Client.js
/usr/share/xpra/www/js/Client.js.gz
/usr/share/xpra/www/js/Keycodes.js
/usr/share/xpra/www/js/Keycodes.js.gz
/usr/share/xpra/www/js/MediaSourceUtil.js
/usr/share/xpra/www/js/MediaSourceUtil.js.gz
/usr/share/xpra/www/js/Menu-custom.js
/usr/share/xpra/www/js/Menu-custom.js.gz
/usr/share/xpra/www/js/Menu.js
/usr/share/xpra/www/js/Menu.js.gz
/usr/share/xpra/www/js/Notifications.js
/usr/share/xpra/www/js/Notifications.js.gz
/usr/share/xpra/www/js/Protocol.js
/usr/share/xpra/www/js/Protocol.js.gz
/usr/share/xpra/www/js/Utilities.js
/usr/share/xpra/www/js/Utilities.js.gz
/usr/share/xpra/www/js/Window.js
/usr/share/xpra/www/js/Window.js.gz
/usr/share/xpra/www/js/lib/FileSaver.js
/usr/share/xpra/www/js/lib/FileSaver.js.gz
/usr/share/xpra/www/js/lib/aurora/aac.js
/usr/share/xpra/www/js/lib/aurora/aac.js.gz
/usr/share/xpra/www/js/lib/aurora/aac.js.map
/usr/share/xpra/www/js/lib/aurora/aac.js.map.gz
/usr/share/xpra/www/js/lib/aurora/aurora-xpra.js
/usr/share/xpra/www/js/lib/aurora/aurora-xpra.js.gz
/usr/share/xpra/www/js/lib/aurora/aurora.js
/usr/share/xpra/www/js/lib/aurora/aurora.js.gz
/usr/share/xpra/www/js/lib/aurora/flac.js
/usr/share/xpra/www/js/lib/aurora/flac.js.gz
/usr/share/xpra/www/js/lib/aurora/flac.js.map
/usr/share/xpra/www/js/lib/aurora/flac.js.map.gz
/usr/share/xpra/www/js/lib/aurora/mp3.js
/usr/share/xpra/www/js/lib/aurora/mp3.js.gz
/usr/share/xpra/www/js/lib/aurora/mp3.js.map
/usr/share/xpra/www/js/lib/aurora/mp3.js.map.gz
/usr/share/xpra/www/js/lib/bencode.js
/usr/share/xpra/www/js/lib/bencode.js.gz
/usr/share/xpra/www/js/lib/broadway/AUTHORS
/usr/share/xpra/www/js/lib/broadway/AUTHORS.gz
/usr/share/xpra/www/js/lib/broadway/Decoder.js
/usr/share/xpra/www/js/lib/broadway/Decoder.js.gz
/usr/share/xpra/www/js/lib/broadway/LICENSE
/usr/share/xpra/www/js/lib/broadway/LICENSE.gz
/usr/share/xpra/www/js/lib/brotli_decode.js
/usr/share/xpra/www/js/lib/brotli_decode.js.gz
/usr/share/xpra/www/js/lib/es6-shim.js
/usr/share/xpra/www/js/lib/es6-shim.js.gz
/usr/share/xpra/www/js/lib/forge.js
/usr/share/xpra/www/js/lib/forge.js.gz
/usr/share/xpra/www/js/lib/jquery-ui.js
/usr/share/xpra/www/js/lib/jquery-ui.js.gz
/usr/share/xpra/www/js/lib/jquery.ba-throttle-debounce.js
/usr/share/xpra/www/js/lib/jquery.ba-throttle-debounce.js.gz
/usr/share/xpra/www/js/lib/jquery.js
/usr/share/xpra/www/js/lib/jquery.js.gz
/usr/share/xpra/www/js/lib/jsmpeg.js
/usr/share/xpra/www/js/lib/jsmpeg.js.gz
/usr/share/xpra/www/js/lib/jszip.js
/usr/share/xpra/www/js/lib/jszip.js.gz
/usr/share/xpra/www/js/lib/lz4.js
/usr/share/xpra/www/js/lib/lz4.js.gz
/usr/share/xpra/www/js/lib/wsworker_check.js
/usr/share/xpra/www/js/lib/wsworker_check.js.gz
/usr/share/xpra/www/js/lib/zlib.js
/usr/share/xpra/www/js/lib/zlib.js.gz
/usr/share/xpra/www/js/lib/zlib.pretty.js.map
/usr/share/xpra/www/js/lib/zlib.pretty.js.map.gz

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xpra/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/xpra/90b47d629f432a2f522f4611d02cad7e19173464
/usr/share/package-licenses/xpra/9744cedce099f727b327cd9913a1fdc58a7f5599
/usr/share/package-licenses/xpra/f45ee1c765646813b442ca58de72e20a64a7ddba

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xpra.1
/usr/share/man/man1/xpra_launcher.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
