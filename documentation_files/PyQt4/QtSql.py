class pyqtSignal():
 def connect(self, targetSignal): pass
 def emit(self, *args): pass
from QtCore import *

class QSql():
    """"""
    # Enum QSql.NumericalPrecisionPolicy
    LowPrecisionInt32 = 0
    LowPrecisionInt64 = 0
    LowPrecisionDouble = 0
    HighPrecision = 0

    # Enum QSql.TableType
    Tables = 0
    SystemTables = 0
    Views = 0
    AllTables = 0

    # Enum QSql.ParamTypeFlag
    In = 0
    Out = 0
    InOut = 0
    Binary = 0

    # Enum QSql.Location
    BeforeFirstRow = 0
    AfterLastRow = 0

    class ParamType():
        """"""
        def __init__(self):
            '''QSql.ParamType QSql.ParamType.__init__()'''
            return QSql.ParamType()
        def __init__(self):
            '''int QSql.ParamType.__init__()'''
            return int()
        def __init__(self):
            '''void QSql.ParamType.__init__()'''
        def __bool__(self):
            '''int QSql.ParamType.__bool__()'''
            return int()
        def __ne__(self, f):
            '''bool QSql.ParamType.__ne__(QSql.ParamType f)'''
            return bool()
        def __eq__(self, f):
            '''bool QSql.ParamType.__eq__(QSql.ParamType f)'''
            return bool()
        def __invert__(self):
            '''QSql.ParamType QSql.ParamType.__invert__()'''
            return QSql.ParamType()
        def __and__(self, mask):
            '''QSql.ParamType QSql.ParamType.__and__(int mask)'''
            return QSql.ParamType()
        def __xor__(self, f):
            '''QSql.ParamType QSql.ParamType.__xor__(QSql.ParamType f)'''
            return QSql.ParamType()
        def __xor__(self, f):
            '''QSql.ParamType QSql.ParamType.__xor__(int f)'''
            return QSql.ParamType()
        def __or__(self, f):
            '''QSql.ParamType QSql.ParamType.__or__(QSql.ParamType f)'''
            return QSql.ParamType()
        def __or__(self, f):
            '''QSql.ParamType QSql.ParamType.__or__(int f)'''
            return QSql.ParamType()
        def __int__(self):
            '''int QSql.ParamType.__int__()'''
            return int()
        def __ixor__(self, f):
            '''QSql.ParamType QSql.ParamType.__ixor__(QSql.ParamType f)'''
            return QSql.ParamType()
        def __ior__(self, f):
            '''QSql.ParamType QSql.ParamType.__ior__(QSql.ParamType f)'''
            return QSql.ParamType()
        def __iand__(self, mask):
            '''QSql.ParamType QSql.ParamType.__iand__(int mask)'''
            return QSql.ParamType()


class QSqlDriverCreatorBase():
    """"""
    def __init__(self):
        '''void QSqlDriverCreatorBase.__init__()'''
    def __init__(self):
        '''QSqlDriverCreatorBase QSqlDriverCreatorBase.__init__()'''
        return QSqlDriverCreatorBase()
    def createObject(self):
        '''abstract QSqlDriver QSqlDriverCreatorBase.createObject()'''
        return QSqlDriver()


class QSqlDatabase():
    """"""
    def __init__(self):
        '''void QSqlDatabase.__init__()'''
    def __init__(self, other):
        '''void QSqlDatabase.__init__(QSqlDatabase other)'''
    def __init__(self, type):
        '''void QSqlDatabase.__init__(QString type)'''
    def __init__(self, driver):
        '''void QSqlDatabase.__init__(QSqlDriver driver)'''
    def numericalPrecisionPolicy(self):
        '''QSql.NumericalPrecisionPolicy QSqlDatabase.numericalPrecisionPolicy()'''
        return QSql.NumericalPrecisionPolicy()
    def setNumericalPrecisionPolicy(self, precisionPolicy):
        '''void QSqlDatabase.setNumericalPrecisionPolicy(QSql.NumericalPrecisionPolicy precisionPolicy)'''
    def isDriverAvailable(self, name):
        '''static bool QSqlDatabase.isDriverAvailable(QString name)'''
        return bool()
    def registerSqlDriver(self, name, creator):
        '''static void QSqlDatabase.registerSqlDriver(QString name, QSqlDriverCreatorBase creator)'''
    def connectionNames(self):
        '''static QStringList QSqlDatabase.connectionNames()'''
        return QStringList()
    def drivers(self):
        '''static QStringList QSqlDatabase.drivers()'''
        return QStringList()
    def contains(self, connectionName = None):
        '''static bool QSqlDatabase.contains(QString connectionName = QLatin1String(QSqlDatabase.defaultConnection))'''
        return bool()
    def removeDatabase(self, connectionName):
        '''static void QSqlDatabase.removeDatabase(QString connectionName)'''
    def database(self, connectionName = None, open = True):
        '''static QSqlDatabase QSqlDatabase.database(QString connectionName = QLatin1String(QSqlDatabase.defaultConnection), bool open = True)'''
        return QSqlDatabase()
    def cloneDatabase(self, other, connectionName):
        '''static QSqlDatabase QSqlDatabase.cloneDatabase(QSqlDatabase other, QString connectionName)'''
        return QSqlDatabase()
    def addDatabase(self, type, connectionName = None):
        '''static QSqlDatabase QSqlDatabase.addDatabase(QString type, QString connectionName = QLatin1String(QSqlDatabase.defaultConnection))'''
        return QSqlDatabase()
    def addDatabase(self, driver, connectionName = None):
        '''static QSqlDatabase QSqlDatabase.addDatabase(QSqlDriver driver, QString connectionName = QLatin1String(QSqlDatabase.defaultConnection))'''
        return QSqlDatabase()
    def driver(self):
        '''QSqlDriver QSqlDatabase.driver()'''
        return QSqlDriver()
    def connectionName(self):
        '''QString QSqlDatabase.connectionName()'''
        return QString()
    def connectOptions(self):
        '''QString QSqlDatabase.connectOptions()'''
        return QString()
    def port(self):
        '''int QSqlDatabase.port()'''
        return int()
    def driverName(self):
        '''QString QSqlDatabase.driverName()'''
        return QString()
    def hostName(self):
        '''QString QSqlDatabase.hostName()'''
        return QString()
    def password(self):
        '''QString QSqlDatabase.password()'''
        return QString()
    def userName(self):
        '''QString QSqlDatabase.userName()'''
        return QString()
    def databaseName(self):
        '''QString QSqlDatabase.databaseName()'''
        return QString()
    def setConnectOptions(self, options = QString()):
        '''void QSqlDatabase.setConnectOptions(QString options = QString())'''
    def setPort(self, p):
        '''void QSqlDatabase.setPort(int p)'''
    def setHostName(self, host):
        '''void QSqlDatabase.setHostName(QString host)'''
    def setPassword(self, password):
        '''void QSqlDatabase.setPassword(QString password)'''
    def setUserName(self, name):
        '''void QSqlDatabase.setUserName(QString name)'''
    def setDatabaseName(self, name):
        '''void QSqlDatabase.setDatabaseName(QString name)'''
    def rollback(self):
        '''bool QSqlDatabase.rollback()'''
        return bool()
    def commit(self):
        '''bool QSqlDatabase.commit()'''
        return bool()
    def transaction(self):
        '''bool QSqlDatabase.transaction()'''
        return bool()
    def isValid(self):
        '''bool QSqlDatabase.isValid()'''
        return bool()
    def lastError(self):
        '''QSqlError QSqlDatabase.lastError()'''
        return QSqlError()
    def exec_(self, query = QString()):
        '''QSqlQuery QSqlDatabase.exec_(QString query = QString())'''
        return QSqlQuery()
    def record(self, tablename):
        '''QSqlRecord QSqlDatabase.record(QString tablename)'''
        return QSqlRecord()
    def primaryIndex(self, tablename):
        '''QSqlIndex QSqlDatabase.primaryIndex(QString tablename)'''
        return QSqlIndex()
    def tables(self, type = None):
        '''QStringList QSqlDatabase.tables(QSql.TableType type = QSql.Tables)'''
        return QStringList()
    def isOpenError(self):
        '''bool QSqlDatabase.isOpenError()'''
        return bool()
    def isOpen(self):
        '''bool QSqlDatabase.isOpen()'''
        return bool()
    def close(self):
        '''void QSqlDatabase.close()'''
    def open(self):
        '''bool QSqlDatabase.open()'''
        return bool()
    def open(self, user, password):
        '''bool QSqlDatabase.open(QString user, QString password)'''
        return bool()


class QSqlDriver(QObject):
    """"""
    # Enum QSqlDriver.IdentifierType
    FieldName = 0
    TableName = 0

    # Enum QSqlDriver.StatementType
    WhereStatement = 0
    SelectStatement = 0
    UpdateStatement = 0
    InsertStatement = 0
    DeleteStatement = 0

    # Enum QSqlDriver.DriverFeature
    Transactions = 0
    QuerySize = 0
    BLOB = 0
    Unicode = 0
    PreparedQueries = 0
    NamedPlaceholders = 0
    PositionalPlaceholders = 0
    LastInsertId = 0
    BatchOperations = 0
    SimpleLocking = 0
    LowPrecisionNumbers = 0
    EventNotifications = 0
    FinishQuery = 0
    MultipleResultSets = 0

    def __init__(self, parent = None):
        '''void QSqlDriver.__init__(QObject parent = None)'''
    def numericalPrecisionPolicy(self):
        '''QSql.NumericalPrecisionPolicy QSqlDriver.numericalPrecisionPolicy()'''
        return QSql.NumericalPrecisionPolicy()
    def setNumericalPrecisionPolicy(self, precisionPolicy):
        '''void QSqlDriver.setNumericalPrecisionPolicy(QSql.NumericalPrecisionPolicy precisionPolicy)'''
    def stripDelimiters(self, identifier, type):
        '''QString QSqlDriver.stripDelimiters(QString identifier, QSqlDriver.IdentifierType type)'''
        return QString()
    def isIdentifierEscaped(self, identifier, type):
        '''bool QSqlDriver.isIdentifierEscaped(QString identifier, QSqlDriver.IdentifierType type)'''
        return bool()
    def stripDelimitersImplementation(self, identifier, type):
        '''QString QSqlDriver.stripDelimitersImplementation(QString identifier, QSqlDriver.IdentifierType type)'''
        return QString()
    def isIdentifierEscapedImplementation(self, identifier, type):
        '''bool QSqlDriver.isIdentifierEscapedImplementation(QString identifier, QSqlDriver.IdentifierType type)'''
        return bool()
    def subscribedToNotificationsImplementation(self):
        '''QStringList QSqlDriver.subscribedToNotificationsImplementation()'''
        return QStringList()
    def unsubscribeFromNotificationImplementation(self, name):
        '''bool QSqlDriver.unsubscribeFromNotificationImplementation(QString name)'''
        return bool()
    def subscribeToNotificationImplementation(self, name):
        '''bool QSqlDriver.subscribeToNotificationImplementation(QString name)'''
        return bool()
    notification = pyqtSignal() # void notification(const QStringamp;) - signal
    def subscribedToNotifications(self):
        '''QStringList QSqlDriver.subscribedToNotifications()'''
        return QStringList()
    def unsubscribeFromNotification(self, name):
        '''bool QSqlDriver.unsubscribeFromNotification(QString name)'''
        return bool()
    def subscribeToNotification(self, name):
        '''bool QSqlDriver.subscribeToNotification(QString name)'''
        return bool()
    def setLastError(self, e):
        '''void QSqlDriver.setLastError(QSqlError e)'''
    def setOpenError(self, e):
        '''void QSqlDriver.setOpenError(bool e)'''
    def setOpen(self, o):
        '''void QSqlDriver.setOpen(bool o)'''
    def open(self, db, user = QString(), password = QString(), host = QString(), port = None, options = QString()):
        '''abstract bool QSqlDriver.open(QString db, QString user = QString(), QString password = QString(), QString host = QString(), int port = -1, QString options = QString())'''
        return bool()
    def createResult(self):
        '''abstract QSqlResult QSqlDriver.createResult()'''
        return QSqlResult()
    def close(self):
        '''abstract void QSqlDriver.close()'''
    def hasFeature(self, f):
        '''abstract bool QSqlDriver.hasFeature(QSqlDriver.DriverFeature f)'''
        return bool()
    def handle(self):
        '''QVariant QSqlDriver.handle()'''
        return QVariant()
    def lastError(self):
        '''QSqlError QSqlDriver.lastError()'''
        return QSqlError()
    def sqlStatement(self, type, tableName, rec, preparedStatement):
        '''QString QSqlDriver.sqlStatement(QSqlDriver.StatementType type, QString tableName, QSqlRecord rec, bool preparedStatement)'''
        return QString()
    def escapeIdentifier(self, identifier, type):
        '''QString QSqlDriver.escapeIdentifier(QString identifier, QSqlDriver.IdentifierType type)'''
        return QString()
    def formatValue(self, field, trimStrings = False):
        '''QString QSqlDriver.formatValue(QSqlField field, bool trimStrings = False)'''
        return QString()
    def record(self, tableName):
        '''QSqlRecord QSqlDriver.record(QString tableName)'''
        return QSqlRecord()
    def primaryIndex(self, tableName):
        '''QSqlIndex QSqlDriver.primaryIndex(QString tableName)'''
        return QSqlIndex()
    def tables(self, tableType):
        '''QStringList QSqlDriver.tables(QSql.TableType tableType)'''
        return QStringList()
    def rollbackTransaction(self):
        '''bool QSqlDriver.rollbackTransaction()'''
        return bool()
    def commitTransaction(self):
        '''bool QSqlDriver.commitTransaction()'''
        return bool()
    def beginTransaction(self):
        '''bool QSqlDriver.beginTransaction()'''
        return bool()
    def isOpenError(self):
        '''bool QSqlDriver.isOpenError()'''
        return bool()
    def isOpen(self):
        '''bool QSqlDriver.isOpen()'''
        return bool()


class QSqlError():
    """"""
    # Enum QSqlError.ErrorType
    NoError = 0
    ConnectionError = 0
    StatementError = 0
    TransactionError = 0
    UnknownError = 0

    def __init__(self, driverText = QString(), databaseText = QString(), type = None, number = None):
        '''void QSqlError.__init__(QString driverText = QString(), QString databaseText = QString(), QSqlError.ErrorType type = QSqlError.NoError, int number = -1)'''
    def __init__(self, other):
        '''void QSqlError.__init__(QSqlError other)'''
    def isValid(self):
        '''bool QSqlError.isValid()'''
        return bool()
    def text(self):
        '''QString QSqlError.text()'''
        return QString()
    def setNumber(self, number):
        '''void QSqlError.setNumber(int number)'''
    def number(self):
        '''int QSqlError.number()'''
        return int()
    def setType(self, type):
        '''void QSqlError.setType(QSqlError.ErrorType type)'''
    def type(self):
        '''QSqlError.ErrorType QSqlError.type()'''
        return QSqlError.ErrorType()
    def setDatabaseText(self, databaseText):
        '''void QSqlError.setDatabaseText(QString databaseText)'''
    def databaseText(self):
        '''QString QSqlError.databaseText()'''
        return QString()
    def setDriverText(self, driverText):
        '''void QSqlError.setDriverText(QString driverText)'''
    def driverText(self):
        '''QString QSqlError.driverText()'''
        return QString()


class QSqlField():
    """"""
    # Enum QSqlField.RequiredStatus
    Unknown = 0
    Optional = 0
    Required = 0

    def __init__(self, fieldName = QString(), type = None):
        '''void QSqlField.__init__(QString fieldName = QString(), Type type = QVariant.Invalid)'''
    def __init__(self, other):
        '''void QSqlField.__init__(QSqlField other)'''
    def isValid(self):
        '''bool QSqlField.isValid()'''
        return bool()
    def isGenerated(self):
        '''bool QSqlField.isGenerated()'''
        return bool()
    def typeID(self):
        '''int QSqlField.typeID()'''
        return int()
    def defaultValue(self):
        '''QVariant QSqlField.defaultValue()'''
        return QVariant()
    def precision(self):
        '''int QSqlField.precision()'''
        return int()
    def length(self):
        '''int QSqlField.length()'''
        return int()
    def requiredStatus(self):
        '''QSqlField.RequiredStatus QSqlField.requiredStatus()'''
        return QSqlField.RequiredStatus()
    def setAutoValue(self, autoVal):
        '''void QSqlField.setAutoValue(bool autoVal)'''
    def setGenerated(self, gen):
        '''void QSqlField.setGenerated(bool gen)'''
    def setSqlType(self, type):
        '''void QSqlField.setSqlType(int type)'''
    def setDefaultValue(self, value):
        '''void QSqlField.setDefaultValue(QVariant value)'''
    def setPrecision(self, precision):
        '''void QSqlField.setPrecision(int precision)'''
    def setLength(self, fieldLength):
        '''void QSqlField.setLength(int fieldLength)'''
    def setRequired(self, required):
        '''void QSqlField.setRequired(bool required)'''
    def setRequiredStatus(self, status):
        '''void QSqlField.setRequiredStatus(QSqlField.RequiredStatus status)'''
    def setType(self, type):
        '''void QSqlField.setType(Type type)'''
    def isAutoValue(self):
        '''bool QSqlField.isAutoValue()'''
        return bool()
    def type(self):
        '''Type QSqlField.type()'''
        return Type()
    def clear(self):
        '''void QSqlField.clear()'''
    def isReadOnly(self):
        '''bool QSqlField.isReadOnly()'''
        return bool()
    def setReadOnly(self, readOnly):
        '''void QSqlField.setReadOnly(bool readOnly)'''
    def isNull(self):
        '''bool QSqlField.isNull()'''
        return bool()
    def name(self):
        '''QString QSqlField.name()'''
        return QString()
    def setName(self, name):
        '''void QSqlField.setName(QString name)'''
    def value(self):
        '''QVariant QSqlField.value()'''
        return QVariant()
    def setValue(self, value):
        '''void QSqlField.setValue(QVariant value)'''
    def __ne__(self, other):
        '''bool QSqlField.__ne__(QSqlField other)'''
        return bool()
    def __eq__(self, other):
        '''bool QSqlField.__eq__(QSqlField other)'''
        return bool()


class QSqlRecord():
    """"""
    def __init__(self):
        '''void QSqlRecord.__init__()'''
    def __init__(self, other):
        '''void QSqlRecord.__init__(QSqlRecord other)'''
    def __len__(self):
        '''None QSqlRecord.__len__()'''
        return None()
    def count(self):
        '''int QSqlRecord.count()'''
        return int()
    def clearValues(self):
        '''void QSqlRecord.clearValues()'''
    def clear(self):
        '''void QSqlRecord.clear()'''
    def contains(self, name):
        '''bool QSqlRecord.contains(QString name)'''
        return bool()
    def isEmpty(self):
        '''bool QSqlRecord.isEmpty()'''
        return bool()
    def remove(self, pos):
        '''void QSqlRecord.remove(int pos)'''
    def insert(self, pos, field):
        '''void QSqlRecord.insert(int pos, QSqlField field)'''
    def replace(self, pos, field):
        '''void QSqlRecord.replace(int pos, QSqlField field)'''
    def append(self, field):
        '''void QSqlRecord.append(QSqlField field)'''
    def setGenerated(self, name, generated):
        '''void QSqlRecord.setGenerated(QString name, bool generated)'''
    def setGenerated(self, i, generated):
        '''void QSqlRecord.setGenerated(int i, bool generated)'''
    def isGenerated(self, i):
        '''bool QSqlRecord.isGenerated(int i)'''
        return bool()
    def isGenerated(self, name):
        '''bool QSqlRecord.isGenerated(QString name)'''
        return bool()
    def field(self, i):
        '''QSqlField QSqlRecord.field(int i)'''
        return QSqlField()
    def field(self, name):
        '''QSqlField QSqlRecord.field(QString name)'''
        return QSqlField()
    def fieldName(self, i):
        '''QString QSqlRecord.fieldName(int i)'''
        return QString()
    def indexOf(self, name):
        '''int QSqlRecord.indexOf(QString name)'''
        return int()
    def isNull(self, i):
        '''bool QSqlRecord.isNull(int i)'''
        return bool()
    def isNull(self, name):
        '''bool QSqlRecord.isNull(QString name)'''
        return bool()
    def setNull(self, i):
        '''void QSqlRecord.setNull(int i)'''
    def setNull(self, name):
        '''void QSqlRecord.setNull(QString name)'''
    def setValue(self, i, val):
        '''void QSqlRecord.setValue(int i, QVariant val)'''
    def setValue(self, name, val):
        '''void QSqlRecord.setValue(QString name, QVariant val)'''
    def value(self, i):
        '''QVariant QSqlRecord.value(int i)'''
        return QVariant()
    def value(self, name):
        '''QVariant QSqlRecord.value(QString name)'''
        return QVariant()
    def __ne__(self, other):
        '''bool QSqlRecord.__ne__(QSqlRecord other)'''
        return bool()
    def __eq__(self, other):
        '''bool QSqlRecord.__eq__(QSqlRecord other)'''
        return bool()


class QSqlIndex(QSqlRecord):
    """"""
    def __init__(self, cursorName = QString(), name = QString()):
        '''void QSqlIndex.__init__(QString cursorName = QString(), QString name = QString())'''
    def __init__(self, other):
        '''void QSqlIndex.__init__(QSqlIndex other)'''
    def setDescending(self, i, desc):
        '''void QSqlIndex.setDescending(int i, bool desc)'''
    def isDescending(self, i):
        '''bool QSqlIndex.isDescending(int i)'''
        return bool()
    def append(self, field):
        '''void QSqlIndex.append(QSqlField field)'''
    def append(self, field, desc):
        '''void QSqlIndex.append(QSqlField field, bool desc)'''
    def name(self):
        '''QString QSqlIndex.name()'''
        return QString()
    def setName(self, name):
        '''void QSqlIndex.setName(QString name)'''
    def cursorName(self):
        '''QString QSqlIndex.cursorName()'''
        return QString()
    def setCursorName(self, cursorName):
        '''void QSqlIndex.setCursorName(QString cursorName)'''


class QSqlQuery():
    """"""
    # Enum QSqlQuery.BatchExecutionMode
    ValuesAsRows = 0
    ValuesAsColumns = 0

    def __init__(self, r):
        '''void QSqlQuery.__init__(QSqlResult r)'''
    def __init__(self, query = QString(), db = QSqlDatabase()):
        '''void QSqlQuery.__init__(QString query = QString(), QSqlDatabase db = QSqlDatabase())'''
    def __init__(self, db):
        '''void QSqlQuery.__init__(QSqlDatabase db)'''
    def __init__(self, other):
        '''void QSqlQuery.__init__(QSqlQuery other)'''
    def nextResult(self):
        '''bool QSqlQuery.nextResult()'''
        return bool()
    def finish(self):
        '''void QSqlQuery.finish()'''
    def numericalPrecisionPolicy(self):
        '''QSql.NumericalPrecisionPolicy QSqlQuery.numericalPrecisionPolicy()'''
        return QSql.NumericalPrecisionPolicy()
    def setNumericalPrecisionPolicy(self, precisionPolicy):
        '''void QSqlQuery.setNumericalPrecisionPolicy(QSql.NumericalPrecisionPolicy precisionPolicy)'''
    def lastInsertId(self):
        '''QVariant QSqlQuery.lastInsertId()'''
        return QVariant()
    def executedQuery(self):
        '''QString QSqlQuery.executedQuery()'''
        return QString()
    def boundValues(self):
        '''dict-of-QString-QVariant QSqlQuery.boundValues()'''
        return dict-of-QString-QVariant()
    def boundValue(self, placeholder):
        '''QVariant QSqlQuery.boundValue(QString placeholder)'''
        return QVariant()
    def boundValue(self, pos):
        '''QVariant QSqlQuery.boundValue(int pos)'''
        return QVariant()
    def addBindValue(self, val, type = None):
        '''void QSqlQuery.addBindValue(QVariant val, QSql.ParamType type = QSql.In)'''
    def bindValue(self, placeholder, val, type = None):
        '''void QSqlQuery.bindValue(QString placeholder, QVariant val, QSql.ParamType type = QSql.In)'''
    def bindValue(self, pos, val, type = None):
        '''void QSqlQuery.bindValue(int pos, QVariant val, QSql.ParamType type = QSql.In)'''
    def prepare(self, query):
        '''bool QSqlQuery.prepare(QString query)'''
        return bool()
    def execBatch(self, mode = None):
        '''bool QSqlQuery.execBatch(QSqlQuery.BatchExecutionMode mode = QSqlQuery.ValuesAsRows)'''
        return bool()
    def clear(self):
        '''void QSqlQuery.clear()'''
    def last(self):
        '''bool QSqlQuery.last()'''
        return bool()
    def first(self):
        '''bool QSqlQuery.first()'''
        return bool()
    def previous(self):
        '''bool QSqlQuery.previous()'''
        return bool()
    def next(self):
        '''bool QSqlQuery.next()'''
        return bool()
    def seek(self, index, relative = False):
        '''bool QSqlQuery.seek(int index, bool relative = False)'''
        return bool()
    def value(self, i):
        '''QVariant QSqlQuery.value(int i)'''
        return QVariant()
    def exec_(self, query):
        '''bool QSqlQuery.exec_(QString query)'''
        return bool()
    def exec_(self):
        '''bool QSqlQuery.exec_()'''
        return bool()
    def setForwardOnly(self, forward):
        '''void QSqlQuery.setForwardOnly(bool forward)'''
    def record(self):
        '''QSqlRecord QSqlQuery.record()'''
        return QSqlRecord()
    def isForwardOnly(self):
        '''bool QSqlQuery.isForwardOnly()'''
        return bool()
    def result(self):
        '''QSqlResult QSqlQuery.result()'''
        return QSqlResult()
    def driver(self):
        '''QSqlDriver QSqlQuery.driver()'''
        return QSqlDriver()
    def size(self):
        '''int QSqlQuery.size()'''
        return int()
    def isSelect(self):
        '''bool QSqlQuery.isSelect()'''
        return bool()
    def lastError(self):
        '''QSqlError QSqlQuery.lastError()'''
        return QSqlError()
    def numRowsAffected(self):
        '''int QSqlQuery.numRowsAffected()'''
        return int()
    def lastQuery(self):
        '''QString QSqlQuery.lastQuery()'''
        return QString()
    def at(self):
        '''int QSqlQuery.at()'''
        return int()
    def isNull(self, field):
        '''bool QSqlQuery.isNull(int field)'''
        return bool()
    def isActive(self):
        '''bool QSqlQuery.isActive()'''
        return bool()
    def isValid(self):
        '''bool QSqlQuery.isValid()'''
        return bool()


class QSqlQueryModel(QAbstractTableModel):
    """"""
    def __init__(self, parent = None):
        '''void QSqlQueryModel.__init__(QObject parent = None)'''
    def setLastError(self, error):
        '''void QSqlQueryModel.setLastError(QSqlError error)'''
    def indexInQuery(self, item):
        '''QModelIndex QSqlQueryModel.indexInQuery(QModelIndex item)'''
        return QModelIndex()
    def queryChange(self):
        '''void QSqlQueryModel.queryChange()'''
    def canFetchMore(self, parent = QModelIndex()):
        '''bool QSqlQueryModel.canFetchMore(QModelIndex parent = QModelIndex())'''
        return bool()
    def fetchMore(self, parent = QModelIndex()):
        '''void QSqlQueryModel.fetchMore(QModelIndex parent = QModelIndex())'''
    def lastError(self):
        '''QSqlError QSqlQueryModel.lastError()'''
        return QSqlError()
    def clear(self):
        '''void QSqlQueryModel.clear()'''
    def query(self):
        '''QSqlQuery QSqlQueryModel.query()'''
        return QSqlQuery()
    def setQuery(self, query):
        '''void QSqlQueryModel.setQuery(QSqlQuery query)'''
    def setQuery(self, query, db = QSqlDatabase()):
        '''void QSqlQueryModel.setQuery(QString query, QSqlDatabase db = QSqlDatabase())'''
    def removeColumns(self, column, count, parent = QModelIndex()):
        '''bool QSqlQueryModel.removeColumns(int column, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def insertColumns(self, column, count, parent = QModelIndex()):
        '''bool QSqlQueryModel.insertColumns(int column, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def setHeaderData(self, section, orientation, value, role = None):
        '''bool QSqlQueryModel.setHeaderData(int section, Qt.Orientation orientation, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def headerData(self, section, orientation, role = None):
        '''QVariant QSqlQueryModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
        return QVariant()
    def data(self, item, role = None):
        '''QVariant QSqlQueryModel.data(QModelIndex item, int role = Qt.DisplayRole)'''
        return QVariant()
    def record(self, row):
        '''QSqlRecord QSqlQueryModel.record(int row)'''
        return QSqlRecord()
    def record(self):
        '''QSqlRecord QSqlQueryModel.record()'''
        return QSqlRecord()
    def columnCount(self, parent = QModelIndex()):
        '''int QSqlQueryModel.columnCount(QModelIndex parent = QModelIndex())'''
        return int()
    def rowCount(self, parent = QModelIndex()):
        '''int QSqlQueryModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()


class QSqlRelationalDelegate(QItemDelegate):
    """"""
    def __init__(self, parent = None):
        '''void QSqlRelationalDelegate.__init__(QObject parent = None)'''
    def setModelData(self, editor, model, index):
        '''void QSqlRelationalDelegate.setModelData(QWidget editor, QAbstractItemModel model, QModelIndex index)'''
    def setEditorData(self, editor, index):
        '''void QSqlRelationalDelegate.setEditorData(QWidget editor, QModelIndex index)'''
    def createEditor(self, parent, option, index):
        '''QWidget QSqlRelationalDelegate.createEditor(QWidget parent, QStyleOptionViewItem option, QModelIndex index)'''
        return QWidget()


class QSqlRelation():
    """"""
    def __init__(self):
        '''void QSqlRelation.__init__()'''
    def __init__(self, aTableName, indexCol, displayCol):
        '''void QSqlRelation.__init__(QString aTableName, QString indexCol, QString displayCol)'''
    def __init__(self):
        '''QSqlRelation QSqlRelation.__init__()'''
        return QSqlRelation()
    def isValid(self):
        '''bool QSqlRelation.isValid()'''
        return bool()
    def displayColumn(self):
        '''QString QSqlRelation.displayColumn()'''
        return QString()
    def indexColumn(self):
        '''QString QSqlRelation.indexColumn()'''
        return QString()
    def tableName(self):
        '''QString QSqlRelation.tableName()'''
        return QString()


class QSqlTableModel(QSqlQueryModel):
    """"""
    # Enum QSqlTableModel.EditStrategy
    OnFieldChange = 0
    OnRowChange = 0
    OnManualSubmit = 0

    def __init__(self, parent = None, db = QSqlDatabase()):
        '''void QSqlTableModel.__init__(QObject parent = None, QSqlDatabase db = QSqlDatabase())'''
    def indexInQuery(self, item):
        '''QModelIndex QSqlTableModel.indexInQuery(QModelIndex item)'''
        return QModelIndex()
    def setQuery(self, query):
        '''void QSqlTableModel.setQuery(QSqlQuery query)'''
    def setPrimaryKey(self, key):
        '''void QSqlTableModel.setPrimaryKey(QSqlIndex key)'''
    def selectStatement(self):
        '''QString QSqlTableModel.selectStatement()'''
        return QString()
    def orderByClause(self):
        '''QString QSqlTableModel.orderByClause()'''
        return QString()
    def deleteRowFromTable(self, row):
        '''bool QSqlTableModel.deleteRowFromTable(int row)'''
        return bool()
    def insertRowIntoTable(self, values):
        '''bool QSqlTableModel.insertRowIntoTable(QSqlRecord values)'''
        return bool()
    def updateRowInTable(self, row, values):
        '''bool QSqlTableModel.updateRowInTable(int row, QSqlRecord values)'''
        return bool()
    beforeDelete = pyqtSignal() # void beforeDelete(int) - signal
    beforeUpdate = pyqtSignal() # void beforeUpdate(int,QSqlRecordamp;) - signal
    beforeInsert = pyqtSignal() # void beforeInsert(QSqlRecordamp;) - signal
    primeInsert = pyqtSignal() # void primeInsert(int,QSqlRecordamp;) - signal
    def revertAll(self):
        '''void QSqlTableModel.revertAll()'''
    def submitAll(self):
        '''bool QSqlTableModel.submitAll()'''
        return bool()
    def revert(self):
        '''void QSqlTableModel.revert()'''
    def submit(self):
        '''bool QSqlTableModel.submit()'''
        return bool()
    def revertRow(self, row):
        '''void QSqlTableModel.revertRow(int row)'''
    def setRecord(self, row, record):
        '''bool QSqlTableModel.setRecord(int row, QSqlRecord record)'''
        return bool()
    def insertRecord(self, row, record):
        '''bool QSqlTableModel.insertRecord(int row, QSqlRecord record)'''
        return bool()
    def insertRows(self, row, count, parent = QModelIndex()):
        '''bool QSqlTableModel.insertRows(int row, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def removeRows(self, row, count, parent = QModelIndex()):
        '''bool QSqlTableModel.removeRows(int row, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def removeColumns(self, column, count, parent = QModelIndex()):
        '''bool QSqlTableModel.removeColumns(int column, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def rowCount(self, parent = QModelIndex()):
        '''int QSqlTableModel.rowCount(QModelIndex parent = QModelIndex())'''
        return int()
    def setFilter(self, filter):
        '''void QSqlTableModel.setFilter(QString filter)'''
    def filter(self):
        '''QString QSqlTableModel.filter()'''
        return QString()
    def setSort(self, column, order):
        '''void QSqlTableModel.setSort(int column, Qt.SortOrder order)'''
    def sort(self, column, order):
        '''void QSqlTableModel.sort(int column, Qt.SortOrder order)'''
    def fieldIndex(self, fieldName):
        '''int QSqlTableModel.fieldIndex(QString fieldName)'''
        return int()
    def database(self):
        '''QSqlDatabase QSqlTableModel.database()'''
        return QSqlDatabase()
    def primaryKey(self):
        '''QSqlIndex QSqlTableModel.primaryKey()'''
        return QSqlIndex()
    def editStrategy(self):
        '''QSqlTableModel.EditStrategy QSqlTableModel.editStrategy()'''
        return QSqlTableModel.EditStrategy()
    def setEditStrategy(self, strategy):
        '''void QSqlTableModel.setEditStrategy(QSqlTableModel.EditStrategy strategy)'''
    def clear(self):
        '''void QSqlTableModel.clear()'''
    def isDirty(self, index):
        '''bool QSqlTableModel.isDirty(QModelIndex index)'''
        return bool()
    def headerData(self, section, orientation, role = None):
        '''QVariant QSqlTableModel.headerData(int section, Qt.Orientation orientation, int role = Qt.DisplayRole)'''
        return QVariant()
    def setData(self, index, value, role = None):
        '''bool QSqlTableModel.setData(QModelIndex index, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def data(self, index, role = None):
        '''QVariant QSqlTableModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
        return QVariant()
    def flags(self, index):
        '''Qt.ItemFlags QSqlTableModel.flags(QModelIndex index)'''
        return Qt.ItemFlags()
    def tableName(self):
        '''QString QSqlTableModel.tableName()'''
        return QString()
    def setTable(self, tableName):
        '''void QSqlTableModel.setTable(QString tableName)'''
    def select(self):
        '''bool QSqlTableModel.select()'''
        return bool()


class QSqlRelationalTableModel(QSqlTableModel):
    """"""
    # Enum QSqlRelationalTableModel.JoinMode
    InnerJoin = 0
    LeftJoin = 0

    def __init__(self, parent = None, db = QSqlDatabase()):
        '''void QSqlRelationalTableModel.__init__(QObject parent = None, QSqlDatabase db = QSqlDatabase())'''
    def setJoinMode(self, joinMode):
        '''void QSqlRelationalTableModel.setJoinMode(QSqlRelationalTableModel.JoinMode joinMode)'''
    def insertRowIntoTable(self, values):
        '''bool QSqlRelationalTableModel.insertRowIntoTable(QSqlRecord values)'''
        return bool()
    def orderByClause(self):
        '''QString QSqlRelationalTableModel.orderByClause()'''
        return QString()
    def updateRowInTable(self, row, values):
        '''bool QSqlRelationalTableModel.updateRowInTable(int row, QSqlRecord values)'''
        return bool()
    def selectStatement(self):
        '''QString QSqlRelationalTableModel.selectStatement()'''
        return QString()
    def removeColumns(self, column, count, parent = QModelIndex()):
        '''bool QSqlRelationalTableModel.removeColumns(int column, int count, QModelIndex parent = QModelIndex())'''
        return bool()
    def revertRow(self, row):
        '''void QSqlRelationalTableModel.revertRow(int row)'''
    def relationModel(self, column):
        '''QSqlTableModel QSqlRelationalTableModel.relationModel(int column)'''
        return QSqlTableModel()
    def relation(self, column):
        '''QSqlRelation QSqlRelationalTableModel.relation(int column)'''
        return QSqlRelation()
    def setRelation(self, column, relation):
        '''void QSqlRelationalTableModel.setRelation(int column, QSqlRelation relation)'''
    def setTable(self, tableName):
        '''void QSqlRelationalTableModel.setTable(QString tableName)'''
    def select(self):
        '''bool QSqlRelationalTableModel.select()'''
        return bool()
    def clear(self):
        '''void QSqlRelationalTableModel.clear()'''
    def setData(self, index, value, role = None):
        '''bool QSqlRelationalTableModel.setData(QModelIndex index, QVariant value, int role = Qt.EditRole)'''
        return bool()
    def data(self, index, role = None):
        '''QVariant QSqlRelationalTableModel.data(QModelIndex index, int role = Qt.DisplayRole)'''
        return QVariant()


class QSqlResult():
    """"""
    # Enum QSqlResult.BindingSyntax
    PositionalBinding = 0
    NamedBinding = 0

    def __init__(self, db):
        '''void QSqlResult.__init__(QSqlDriver db)'''
    def lastInsertId(self):
        '''QVariant QSqlResult.lastInsertId()'''
        return QVariant()
    def record(self):
        '''QSqlRecord QSqlResult.record()'''
        return QSqlRecord()
    def numRowsAffected(self):
        '''abstract int QSqlResult.numRowsAffected()'''
        return int()
    def size(self):
        '''abstract int QSqlResult.size()'''
        return int()
    def fetchLast(self):
        '''abstract bool QSqlResult.fetchLast()'''
        return bool()
    def fetchFirst(self):
        '''abstract bool QSqlResult.fetchFirst()'''
        return bool()
    def fetchPrevious(self):
        '''bool QSqlResult.fetchPrevious()'''
        return bool()
    def fetchNext(self):
        '''bool QSqlResult.fetchNext()'''
        return bool()
    def fetch(self, i):
        '''abstract bool QSqlResult.fetch(int i)'''
        return bool()
    def reset(self, sqlquery):
        '''abstract bool QSqlResult.reset(QString sqlquery)'''
        return bool()
    def isNull(self, i):
        '''abstract bool QSqlResult.isNull(int i)'''
        return bool()
    def data(self, i):
        '''abstract QVariant QSqlResult.data(int i)'''
        return QVariant()
    def bindingSyntax(self):
        '''QSqlResult.BindingSyntax QSqlResult.bindingSyntax()'''
        return QSqlResult.BindingSyntax()
    def hasOutValues(self):
        '''bool QSqlResult.hasOutValues()'''
        return bool()
    def clear(self):
        '''void QSqlResult.clear()'''
    def boundValueName(self, pos):
        '''QString QSqlResult.boundValueName(int pos)'''
        return QString()
    def executedQuery(self):
        '''QString QSqlResult.executedQuery()'''
        return QString()
    def boundValues(self):
        '''list-of-QVariant QSqlResult.boundValues()'''
        return [QVariant()]
    def boundValueCount(self):
        '''int QSqlResult.boundValueCount()'''
        return int()
    def bindValueType(self, placeholder):
        '''QSql.ParamType QSqlResult.bindValueType(QString placeholder)'''
        return QSql.ParamType()
    def bindValueType(self, pos):
        '''QSql.ParamType QSqlResult.bindValueType(int pos)'''
        return QSql.ParamType()
    def boundValue(self, placeholder):
        '''QVariant QSqlResult.boundValue(QString placeholder)'''
        return QVariant()
    def boundValue(self, pos):
        '''QVariant QSqlResult.boundValue(int pos)'''
        return QVariant()
    def addBindValue(self, val, type):
        '''void QSqlResult.addBindValue(QVariant val, QSql.ParamType type)'''
    def bindValue(self, pos, val, type):
        '''void QSqlResult.bindValue(int pos, QVariant val, QSql.ParamType type)'''
    def bindValue(self, placeholder, val, type):
        '''void QSqlResult.bindValue(QString placeholder, QVariant val, QSql.ParamType type)'''
    def savePrepare(self, sqlquery):
        '''bool QSqlResult.savePrepare(QString sqlquery)'''
        return bool()
    def prepare(self, query):
        '''bool QSqlResult.prepare(QString query)'''
        return bool()
    def exec_(self):
        '''bool QSqlResult.exec_()'''
        return bool()
    def setForwardOnly(self, forward):
        '''void QSqlResult.setForwardOnly(bool forward)'''
    def setSelect(self, s):
        '''void QSqlResult.setSelect(bool s)'''
    def setQuery(self, query):
        '''void QSqlResult.setQuery(QString query)'''
    def setLastError(self, e):
        '''void QSqlResult.setLastError(QSqlError e)'''
    def setActive(self, a):
        '''void QSqlResult.setActive(bool a)'''
    def setAt(self, at):
        '''void QSqlResult.setAt(int at)'''
    def driver(self):
        '''QSqlDriver QSqlResult.driver()'''
        return QSqlDriver()
    def isForwardOnly(self):
        '''bool QSqlResult.isForwardOnly()'''
        return bool()
    def isSelect(self):
        '''bool QSqlResult.isSelect()'''
        return bool()
    def isActive(self):
        '''bool QSqlResult.isActive()'''
        return bool()
    def isValid(self):
        '''bool QSqlResult.isValid()'''
        return bool()
    def lastError(self):
        '''QSqlError QSqlResult.lastError()'''
        return QSqlError()
    def lastQuery(self):
        '''QString QSqlResult.lastQuery()'''
        return QString()
    def at(self):
        '''int QSqlResult.at()'''
        return int()
    def handle(self):
        '''QVariant QSqlResult.handle()'''
        return QVariant()


