%{?scl:%scl_package nodejs-lodash._basetostring}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-lodash._basetostring

%global npm_name lodash._basetostring
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-lodash._basetostring
Version:	3.0.1
Release:	1%{?dist}
Summary:	The modern build of lodash’s internal `baseToString` as a module.
Url:		https://lodash.com/
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
%endif

%description
The modern build of lodash’s internal `baseToString` as a module.

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/lodash._basetostring

%doc README.md LICENSE

%changelog
* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 3.0.1-1
- Initial build
