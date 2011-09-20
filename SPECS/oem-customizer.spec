%define name    oem-customizer
%define version 0.1 
%define release 1

Name:           %{name} 
Summary:        Just a tool to tarball the custom directory tree in Mandriva OEM
Version:        %{version} 
Release:        %{release} 
Source0:        %{name}-%{version}.tar.bz2
URL:            http://github.com/jonatasteixeira/mandriva-oem-customizer

Group:          Applications
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:        GPLv2+
Buildarch:      noarch

BuildRequires:  python
Requires:       pygtk2.0

%description
Just a simple tool to help the cration directory tree to customize the
installation of a Mandriva OEM

%prep 
%setup -q

%install
echo %{buildroot}
rm -rf %{buildroot}

%makeinstall

install -d -m 0755 %{buildroot}%{_sbindir}
install -d -m 0755 %{buildroot}%{_datadir}
install -d -m 0755 %{buildroot}%{_datadir}/%{name}

cp -rf tmp/%{name} 	%{buildroot}%{_sbindir}/%{name}

%post

%clean 
rm -rf %{buildroot}

%files 
%defattr(0755,root,root) 
%{_sbindir}/%{name}
%{_datadir}/%{name}/*

