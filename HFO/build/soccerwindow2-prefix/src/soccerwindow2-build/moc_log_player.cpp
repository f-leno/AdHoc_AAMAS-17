/****************************************************************************
** Meta object code from reading C++ file 'log_player.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../soccerwindow2/src/qt4/log_player.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'log_player.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_LogPlayer[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      18,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: signature, parameters, type, tag, flags
      11,   10,   10,   10, 0x05,

 // slots: signature, parameters, type, tag, flags
      21,   10,   10,   10, 0x08,
      35,   10,   10,   10, 0x0a,
      46,   10,   10,   10, 0x0a,
      60,   10,   10,   10, 0x0a,
      73,   10,   10,   10, 0x0a,
      80,   10,   10,   10, 0x0a,
      91,   10,   10,   10, 0x0a,
     105,   10,   10,   10, 0x0a,
     121,   10,   10,   10, 0x0a,
     137,   10,   10,   10, 0x0a,
     149,   10,   10,   10, 0x0a,
     160,   10,   10,   10, 0x0a,
     173,   10,   10,   10, 0x0a,
     192,  186,   10,   10, 0x0a,
     213,  207,   10,   10, 0x0a,
     228,   10,   10,   10, 0x0a,
     239,   10,   10,   10, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_LogPlayer[] = {
    "LogPlayer\0\0updated()\0handleTimer()\0"
    "stepBack()\0stepForward()\0playOrStop()\0"
    "stop()\0playBack()\0playForward()\0"
    "goToPrevScore()\0goToNextScore()\0"
    "goToFirst()\0goToLast()\0decelerate()\0"
    "accelerate()\0index\0goToIndex(int)\0"
    "cycle\0goToCycle(int)\0showLive()\0"
    "setLiveMode()\0"
};

void LogPlayer::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        LogPlayer *_t = static_cast<LogPlayer *>(_o);
        switch (_id) {
        case 0: _t->updated(); break;
        case 1: _t->handleTimer(); break;
        case 2: _t->stepBack(); break;
        case 3: _t->stepForward(); break;
        case 4: _t->playOrStop(); break;
        case 5: _t->stop(); break;
        case 6: _t->playBack(); break;
        case 7: _t->playForward(); break;
        case 8: _t->goToPrevScore(); break;
        case 9: _t->goToNextScore(); break;
        case 10: _t->goToFirst(); break;
        case 11: _t->goToLast(); break;
        case 12: _t->decelerate(); break;
        case 13: _t->accelerate(); break;
        case 14: _t->goToIndex((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 15: _t->goToCycle((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 16: _t->showLive(); break;
        case 17: _t->setLiveMode(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData LogPlayer::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject LogPlayer::staticMetaObject = {
    { &QObject::staticMetaObject, qt_meta_stringdata_LogPlayer,
      qt_meta_data_LogPlayer, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &LogPlayer::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *LogPlayer::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *LogPlayer::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_LogPlayer))
        return static_cast<void*>(const_cast< LogPlayer*>(this));
    return QObject::qt_metacast(_clname);
}

int LogPlayer::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 18)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 18;
    }
    return _id;
}

// SIGNAL 0
void LogPlayer::updated()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}
QT_END_MOC_NAMESPACE
