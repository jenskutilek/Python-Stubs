class NSIndexPath:
    def indexPathByAddingIndex_(self, value) -> NSIndexPath: ...
    def __len__(self) -> int: ...
    def __getitem__(self, value) -> int: ...

class NSMenuItem: ...

class NSPoint:
    @property
    def x(self) -> float: ...
    @property
    def y(self) -> float: ...

class NSRect:
    @property
    def origin(self) -> NSPoint: ...
    @property
    def size(self) -> NSSize: ...
    # def x(self) -> float: ...
    # def y(self) -> float: ...

class NSSize:
    @property
    def height(self) -> float: ...
    @property
    def width(self) -> float: ...

