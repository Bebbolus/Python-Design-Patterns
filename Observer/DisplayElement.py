from Observer import Observer
class DisplayElement( Observer ):
    """
        This class is intented as an interface for implementation
    """
    def display( self ):
        raise NotImplementedError( "Should have implemented this" )

