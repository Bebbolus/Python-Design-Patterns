class FlyBehavior( object ):
    """
        This class is intented as an interface for implementation
        The concrete need to implement the performFly() method
    """
    def fly( self ):
        raise NotImplementedError( "Should have implemented this" )
