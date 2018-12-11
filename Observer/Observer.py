class Observer( object ):
    """
        This class is intented as an interface for implementation
    """
    def update( self ):
        raise NotImplementedError( "Should have implemented this" )

