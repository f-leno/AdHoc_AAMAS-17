/****************************************************************************
** Meta object code from reading C++ file 'debug_message_window.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../soccerwindow2/src/qt4/debug_message_window.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'debug_message_window.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_DebugMessageWindow[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      22,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: signature, parameters, type, tag, flags
      20,   19,   19,   19, 0x05,
      39,   33,   19,   19, 0x05,

 // slots: signature, parameters, type, tag, flags
      62,   56,   19,   19, 0x08,
      92,   84,   19,   19, 0x08,
     121,   84,   19,   19, 0x08,
     151,   84,   19,   19, 0x08,
     181,   84,   19,   19, 0x08,
     216,   84,   19,   19, 0x08,
     251,   84,   19,   19, 0x08,
     284,   84,   19,   19, 0x08,
     315,   84,   19,   19, 0x08,
     347,   84,   19,   19, 0x08,
     380,   84,   19,   19, 0x08,
     412,   19,   19,   19, 0x08,
     436,   19,   19,   19, 0x08,
     448,   19,   19,   19, 0x08,
     465,   19,   19,   19, 0x08,
     482,   19,   19,   19, 0x08,
     505,  500,   19,   19, 0x08,
     531,  525,   19,   19, 0x08,
     553,   19,   19,   19, 0x0a,
     564,   19,   19,   19, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_DebugMessageWindow[] = {
    "DebugMessageWindow\0\0configured()\0cycle\0"
    "selectCycle(int)\0index\0changeCurrentTab(int)\0"
    "checked\0toggleShowDebugViewAll(bool)\0"
    "toggleShowDebugViewSelf(bool)\0"
    "toggleShowDebugViewBall(bool)\0"
    "toggleShowDebugViewTeammates(bool)\0"
    "toggleShowDebugViewOpponents(bool)\0"
    "toggleShowDebugViewComment(bool)\0"
    "toggleShowDebugViewShape(bool)\0"
    "toggleShowDebugViewTarget(bool)\0"
    "toggleShowDebugViewMessage(bool)\0"
    "toggleShowDebugLogObjects(bool)\0"
    "showDebugLogDirDialog()\0syncCycle()\0"
    "decrementCycle()\0incrementCycle()\0"
    "findExistString()\0expr\0findString(QString)\0"
    "level\0toggleDebugLevel(int)\0clearAll()\0"
    "updateMessage()\0"
};

void DebugMessageWindow::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        DebugMessageWindow *_t = static_cast<DebugMessageWindow *>(_o);
        switch (_id) {
        case 0: _t->configured(); break;
        case 1: _t->selectCycle((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->changeCurrentTab((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 3: _t->toggleShowDebugViewAll((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->toggleShowDebugViewSelf((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 5: _t->toggleShowDebugViewBall((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 6: _t->toggleShowDebugViewTeammates((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 7: _t->toggleShowDebugViewOpponents((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 8: _t->toggleShowDebugViewComment((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 9: _t->toggleShowDebugViewShape((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 10: _t->toggleShowDebugViewTarget((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 11: _t->toggleShowDebugViewMessage((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 12: _t->toggleShowDebugLogObjects((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 13: _t->showDebugLogDirDialog(); break;
        case 14: _t->syncCycle(); break;
        case 15: _t->decrementCycle(); break;
        case 16: _t->incrementCycle(); break;
        case 17: _t->findExistString(); break;
        case 18: _t->findString((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 19: _t->toggleDebugLevel((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 20: _t->clearAll(); break;
        case 21: _t->updateMessage(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData DebugMessageWindow::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject DebugMessageWindow::staticMetaObject = {
    { &QMainWindow::staticMetaObject, qt_meta_stringdata_DebugMessageWindow,
      qt_meta_data_DebugMessageWindow, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &DebugMessageWindow::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *DebugMessageWindow::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *DebugMessageWindow::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_DebugMessageWindow))
        return static_cast<void*>(const_cast< DebugMessageWindow*>(this));
    return QMainWindow::qt_metacast(_clname);
}

int DebugMessageWindow::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 22)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 22;
    }
    return _id;
}

// SIGNAL 0
void DebugMessageWindow::configured()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}

// SIGNAL 1
void DebugMessageWindow::selectCycle(int _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}
QT_END_MOC_NAMESPACE
