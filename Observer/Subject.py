class Subject ( object ):
    """
        This class is intented as an interface for implementation
    """
    def registerObserver( self ):
        raise NotImplementedError( "Should have implemented this" )
    
    def removeObserver( self ):
        raise NotImplementedError( "Should have implemented this" )

    def notifyObserver( self ):
        raise NotImplementedError( "Should have implemented this" )


