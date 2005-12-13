#!/usr/bin/env python


"""A Skeleton HTML page template, that provides basic structure and utility methods.

Autogenerated by CHEETAH: The Python-Powered Template Engine
 CHEETAH VERSION: 1.0
 Generation time: Mon Dec 12 21:31:24 2005
   Source file: src/Templates/SkeletonPage.tmpl
   Source file last modified: Mon Oct  7 11:37:30 2002
"""

__CHEETAH_genTime__ = 'Mon Dec 12 21:31:24 2005'
__CHEETAH_src__ = 'src/Templates/SkeletonPage.tmpl'
__CHEETAH_version__ = '1.0'

##################################################
## DEPENDENCIES

import sys
import os
import os.path
from os.path import getmtime, exists
import time
import types
import __builtin__
from Cheetah.Template import Template
from Cheetah.DummyTransaction import DummyTransaction
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from Cheetah.Templates._SkeletonPage import _SkeletonPage

##################################################
## MODULE CONSTANTS

try:
    True, False
except NameError:
    True, False = (1==1), (1==0)
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time

##################################################
## CLASSES

class SkeletonPage(_SkeletonPage):
    """
    
    Autogenerated by CHEETAH: The Python-Powered Template Engine
    """

    ##################################################
    ## GENERATED METHODS


    def __init__(self, *args, **KWs):
        """
        
        """

        _SkeletonPage.__init__(self, *args, **KWs)
        if not self._CHEETAH_instanceInitialized:
            if not hasattr(self, '_initCheetahAttributes'):
                Template.assignRequiredMethodsToClass(self.__class__)
            cheetahKWArgs = {}
            allowedKWs = 'searchList filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahAttributes(**cheetahKWArgs)
        

    def writeHeadTag(self,
            trans=None,
            VFFSL=valueFromFrameOrSearchList,
            VFN=valueForName):


        """
        Generated from #block writeHeadTag at line 22, col 1.
        """

        if not trans and not callable(self.transaction): trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            __dummyTrans = True
        else: __dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH_searchList
        __filter = self._CHEETAH_currentFilter
        
        ########################################
        ## START - generated method body
        
        write('<head>\n<title>')
        __v = VFFSL(SL,"title",True)
        if __v is not None: write(__filter(__v, rawExpr='$title')) # from line 24, col 8.
        write('</title>\n')
        __v = VFFSL(SL,"metaTags",True)
        if __v is not None: write(__filter(__v, rawExpr='$metaTags')) # from line 25, col 1.
        write(' \n')
        __v = VFFSL(SL,"stylesheetTags",True)
        if __v is not None: write(__filter(__v, rawExpr='$stylesheetTags')) # from line 26, col 1.
        write(' \n')
        __v = VFFSL(SL,"javascriptTags",True)
        if __v is not None: write(__filter(__v, rawExpr='$javascriptTags')) # from line 27, col 1.
        write('\n</head>\n')
        
        ########################################
        ## END - generated method body
        
        return __dummyTrans and trans.response().getvalue() or ""
        

    def writeBody(self,
            trans=None,
            VFFSL=valueFromFrameOrSearchList,
            VFN=valueForName):


        """
        Generated from #block writeBody at line 36, col 1.
        """

        if not trans and not callable(self.transaction): trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            __dummyTrans = True
        else: __dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH_searchList
        __filter = self._CHEETAH_currentFilter
        
        ########################################
        ## START - generated method body
        
        write('This skeleton page has no flesh. Its body needs to be implemented.\n')
        
        ########################################
        ## END - generated method body
        
        return __dummyTrans and trans.response().getvalue() or ""
        

    def respond(self,
            trans=None,
            VFFSL=valueFromFrameOrSearchList,
            VFN=valueForName):


        """
        This is the main method generated by Cheetah
        """

        if not trans and not callable(self.transaction): trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            __dummyTrans = True
        else: __dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH_searchList
        __filter = self._CHEETAH_currentFilter
        
        ########################################
        ## START - generated method body
        
        ## START CACHE REGION: at line, col (6, 1) in the source.
        RECACHE = False
        region = self._CHEETAH_cacheRegions.get('header')
        if not region:
            region = CacheRegion()
            self._CHEETAH_cacheRegions['header'] = region
            RECACHE = True
        cache = region.getCache('header')
        if RECACHE or not cache.getData():
            orig_trans = trans
            trans = cacheCollector = DummyTransaction()
            write = cacheCollector.response().write
            __v = VFFSL(SL,"docType",True)
            if __v is not None: write(__filter(__v, rawExpr='$docType')) # from line 7, col 1.
            write('\n')
            __v = VFFSL(SL,"htmlTag",True)
            if __v is not None: write(__filter(__v, rawExpr='$htmlTag')) # from line 8, col 1.
            write('''
<!-- This document was autogenerated by Cheetah(http://CheetahTemplate.org). 
Do not edit it directly!

Copyright ''')
            __v = VFFSL(SL,"currentYr",True)
            if __v is not None: write(__filter(__v, rawExpr='$currentYr')) # from line 12, col 11.
            write(' - ')
            __v = VFFSL(SL,"siteCopyrightName",True)
            if __v is not None: write(__filter(__v, rawExpr='$siteCopyrightName')) # from line 12, col 24.
            write(' - All Rights Reserved.\nFeel free to copy any javascript or html you like on this site,\nprovided you remove all links and/or references to ')
            __v = VFFSL(SL,"siteDomainName",True)
            if __v is not None: write(__filter(__v, rawExpr='$siteDomainName')) # from line 14, col 52.
            write('''
However, please do not copy any content or images without permission.

''')
            __v = VFFSL(SL,"siteCredits",True)
            if __v is not None: write(__filter(__v, rawExpr='$siteCredits')) # from line 17, col 1.
            write('''

-->


''')
            self.writeHeadTag(trans=trans)
            write('\n')
            trans = orig_trans
            write = trans.response().write
            cache.setData(cacheCollector.response().getvalue())
            del cacheCollector
        write(cache.getData())
        ## END CACHE REGION
        
        write('\n')
        __v = VFFSL(SL,"bodyTag",True)
        if __v is not None: write(__filter(__v, rawExpr='$bodyTag')) # from line 34, col 1.
        write('\n\n')
        self.writeBody(trans=trans)
        write('''
</body>
</html>



''')
        
        ########################################
        ## END - generated method body
        
        return __dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## GENERATED ATTRIBUTES


    _CHEETAH_instanceInitialized = False

    def __str__(self): return self.respond()

    _mainCheetahMethod_for_SkeletonPage= 'respond'


# CHEETAH was developed by Tavis Rudd, Mike Orr, Ian Bicking and Chuck Esterbrook;
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=SkeletonPage()).run()

