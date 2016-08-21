%define 	module		phaul
%define 	egg_name	phaul
Summary:	p.haul
Name:		p.haul
Version:	0.0.0
Release:	0.1
License:	GPL v2
Group:		Libraries/Python
Source0:	https://github.com/xemul/%{name}/archive/master/p.haul.tar.gz
# Source0-md5:	4bb71ab95a787fb4b2ec0ad3b51c8c31
URL:		https://github.com/xemul/p.haul
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	criu
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Process HAULer -- a tool to live-migrate containers and processes

The live-migration idea is quite simple. To live migrate a task one
needs to:
- stop it and save its state into image file(s)
- make images available on the remote host
- recreate task on it from the images

This is what p.haul does. It heavily uses CRIU to do state dump and
restore. Task's stopped time is decreased using the CRIU's pre-dump
action.

%prep
%setup -qc
mv p.haul-*/* .

%build
%py_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

# not installed by setup.py, do ourselves
install -d $RPM_BUILD_ROOT%{_sbindir}
install -p p.haul p.haul-service p.haul-ssh p.haul-wrap $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_sbindir}/p.haul
%attr(755,root,root) %{_sbindir}/p.haul-service
%attr(755,root,root) %{_sbindir}/p.haul-ssh
%attr(755,root,root) %{_sbindir}/p.haul-wrap
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-*-py*.egg-info
