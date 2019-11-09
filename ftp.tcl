#############################################################################
# Generated by PAGE version 4.17
# in conjunction with Tcl version 8.6
# Nov 08, 2019 08:53:11 PM IST  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #5b9ed8
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d8955b
set vTcl(analog_color_p) #5b5fd8
set vTcl(analog_color_m) #5bd8d4
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
}

#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {Product Sans} -size 14 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font11
vTcl:font:add_font \
    "-family {Product Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font12
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top39
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top39
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top39 {base} {
    if {$base == ""} {
        set base .top39
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#fef7ff} 
    wm focusmodel $top passive
    wm geometry $top 799x764+451+150
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "FTP"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    label $top.lab40 \
        -background {#CDDC39} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#f7f7f7} \
        -text {File Transfer Protocol} 
    vTcl:DefineAlias "$top.lab40" "Label1" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent41 \
        -background white -disabledforeground {#a3a3a3} -font font10 \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$top.ent41" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab42 \
        -background {#fef7ff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#000000} \
        -text {Enter the name of the file} 
    vTcl:DefineAlias "$top.lab42" "Label2" vTcl:WidgetProc "Toplevel1" 1
    button $top.but43 \
        -activebackground {#5bd8d4} -activeforeground {#000000} \
        -background {#F0F4C3} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font12,object) -foreground {#000000} \
        -highlightbackground {#5b9ed8} -highlightcolor black -pady 0 \
        -text Transfer 
    vTcl:DefineAlias "$top.but43" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but44 \
        -activebackground {#5bd8d4} -activeforeground {#000000} \
        -background {#F0F4C3} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font12,object) -foreground {#000000} \
        -highlightbackground {#5b9ed8} -highlightcolor black -pady 0 \
        -text {Go Back} 
    vTcl:DefineAlias "$top.but44" "Button1_1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab40 \
        -in $top -x 0 -y 0 -width 802 -relwidth 0 -height 76 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent41 \
        -in $top -x 190 -y 220 -width 414 -relwidth 0 -height 54 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab42 \
        -in $top -x 20 -y 150 -width 752 -relwidth 0 -height 56 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but43 \
        -in $top -x 350 -y 300 -width 115 -relwidth 0 -height 33 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but44 \
        -in $top -x 490 -y 300 -width 115 -height 33 -anchor nw \
        -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top39 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

