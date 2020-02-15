# Generated from pkg-config-1.1.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	gem_name	gobject-introspection

Summary:	Ruby binding of gobject-introspection
Name:		rubygem-%{gem_name}

Version:	3.4.1
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	rubygems
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(glib2)
BuildRequires:  rubygem-glib2-devel
BuildRequires:  ruby-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
Ruby binding of gobject-introspection.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%package    devel                                                                                                                                          
Summary:    Development files for %{name}
Group:      Development/Ruby

%description    devel
Development files for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{gem_dir} %{buildroot}%{gem_extdir_mri}

cp -a .%{gem_dir}/* \
    %{buildroot}/%{gem_dir}/

cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so,*.h} \
    %{buildroot}/%{gem_extdir_mri}/


%files
%{gem_instdir}/lib/*.rb
%{gem_instdir}/lib/%{gem_name}/*.rb
%{gem_spec}
%{gem_cache}
%{gem_extdir_mri}/gobject_introspection.so
%{gem_extdir_mri}/gem.build_complete
%{gem_instdir}/test/*.rb
%{gem_instdir}/*.rb
%{gem_instdir}/*.gemspec
%{gem_instdir}/Rakefile

%{gem_instdir}/ext/%{gem_name}/.sitearchdir.time
%{gem_instdir}/ext/%{gem_name}/Makefile
%{gem_instdir}/ext/%{gem_name}/depend
%{gem_instdir}/ext/%{gem_name}/extconf.rb
%{gem_instdir}/ext/%{gem_name}/gobject_introspection.def
%{gem_instdir}/ext/%{gem_name}/*.so

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/[A-Z]*
%files devel
%{gem_extdir_mri}/*.h
%{gem_extdir_mri}/*.h
%{gem_instdir}/ext/%{gem_name}/*.c
%{gem_instdir}/ext/%{gem_name}/*.h
%exclude %{gem_instdir}/ext/%{gem_name}/*.o
%{gem_instdir}/ext/%{gem_name}/ruby-gobject-introspection.pc

%changelog

