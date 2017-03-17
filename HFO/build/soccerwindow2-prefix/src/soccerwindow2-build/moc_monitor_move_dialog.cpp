/****************************************************************************
** Meta object code from reading C++ file 'monitor_move_dialog.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../soccerwindow2/src/qt4/monitor_move_dialog.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'monitor_move_dialog.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_MonitorMoveDialog[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      11,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: signature, parameters, type, tag, flags
      19,   18,   18,   18, 0x05,

 // slots: signature, parameters, type, tag, flags
      30,   18,   18,   18, 0x08,
      48,   18,   18,   18, 0x08,
      55,   18,   18,   18, 0x08,
      65,   62,   18,   18, 0x08,
      87,   62,   18,   18, 0x08,
     112,   62,   18,   18, 0x08,
     132,   62,   18,   18, 0x08,
     159,  153,   18,   18, 0x08,
     180,  153,   18,   18, 0x08,
     202,   18,   18,   18, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_MonitorMoveDialog[] = {
    "MonitorMoveDialog\0\0executed()\0"
    "readFieldStatus()\0open()\0save()\0on\0"
    "toggleBallCheck(bool)\0toggleBallVelCheck(bool)\0"
    "toggleLeftAll(bool)\0toggleRightAll(bool)\0"
    "index\0toggleLeftCheck(int)\0"
    "toggleRightCheck(int)\0sendCommand()\0"
};

void MonitorMoveDialog::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        MonitorMoveDialog *_t = static_cast<MonitorMoveDialog *>(_o);
        switch (_id) {
        case 0: _t->executed(); break;
        case 1: _t->readFieldStatus(); break;
        case 2: _t->open(); break;
        case 3: _t->save(); break;
        case 4: _t->toggleBallCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 5: _t->toggleBallVelCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 6: _t->toggleLeftAll((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 7: _t->toggleRightAll((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 8: _t->toggleLeftCheck((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 9: _t->toggleRightCheck((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 10: _t->sendCommand(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData MonitorMoveDialog::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject MonitorMoveDialog::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_MonitorMoveDialog,
      qt_meta_data_MonitorMoveDialog, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &MonitorMoveDialog::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *MonitorMoveDialog::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *MonitorMoveDialog::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_MonitorMoveDialog))
        return static_cast<void*>(const_cast< MonitorMoveDialog*>(this));
    return QDialog::qt_metacast(_clname);
}

int MonitorMoveDialog::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 11)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 11;
    }
    return _id;
}

// SIGNAL 0
void MonitorMoveDialog::executed()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}
QT_END_MOC_NAMESPACE
