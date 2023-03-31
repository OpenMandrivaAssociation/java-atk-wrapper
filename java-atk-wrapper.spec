%define _disable_lto 1

%global major_version 0.30
%global minor_version 4

Name:       java-atk-wrapper
Version:    %{major_version}.%{minor_version}
Release:    4.3
Summary:    Java ATK Wrapper

#Group
License:    LGPLv2+
URL:        http://git.gnome.org/browse/java-atk-wrapper
Source0:    http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{major_version}/%{name}-%{version}.tar.bz2
# this is a fedora-specific file
# needed to explain how to use java-atk-wrapper with different java runtimes
Source1:    README.fedora

BuildRequires:  java-devel

BuildRequires:  atk-devel
BuildRequires:  GConf2-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  x11-tools

Requires:   java
Requires:   x11-tools

%description
Java ATK Wrapper is a implementation of ATK by using JNI technic. It
converts Java Swing events into ATK events, and send these events to
ATK-Bridge.

JAW is part of the Bonobo deprecation project. It will replaces the
former java-access-bridge.
By talking to ATK-Bridge, it keeps itself from being affected by the
change of underlying communication mechanism.

%prep
%setup -q

%build
%configure2_5x
make %{?_smp_mflags}
cp %{SOURCE1} .

%install
# java-atk-wrapper's make install is broken by design
# it installs to the current JDK_HOME. We want to install it to a central
# location and then allow all/any JRE's/JDK's to use it.
# make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p %{buildroot}%{_libdir}/%{name}

mv wrapper/java-atk-wrapper.jar %{buildroot}%{_libdir}/%{name}/
mv jni/src/.libs/libatk-wrapper.so.0.0.18 %{buildroot}%{_libdir}/%{name}/
ln -s %{_libdir}/%{name}/libatk-wrapper.so.0.0.18 \
    %{buildroot}%{_libdir}/%{name}/libatk-wrapper.so.0


%files
%doc AUTHORS
%doc COPYING.LESSER
%doc NEWS
%doc README
%doc README.fedora
%{_libdir}/%{name}/
