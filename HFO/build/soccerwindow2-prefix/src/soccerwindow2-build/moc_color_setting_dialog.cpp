/****************************************************************************
** Meta object code from reading C++ file 'color_setting_dialog.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../soccerwindow2/src/qt4/color_setting_dialog.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'color_setting_dialog.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_ColorSettingDialog[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: signature, parameters, type, tag, flags
      20,   19,   19,   19, 0x05,

 // slots: signature, parameters, type, tag, flags
      35,   19,   19,   19, 0x08,
      54,   19,   19,   19, 0x08,
      73,   68,   19,   19, 0x08,
     103,   19,   19,   19, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_ColorSettingDialog[] = {
    "ColorSettingDialog\0\0colorChanged()\0"
    "setDefaultColors()\0selectEntry()\0item\0"
    "selectEntry(QListWidgetItem*)\0reject()\0"
};

void ColorSettingDialog::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        ColorSettingDialog *_t = static_cast<ColorSettingDialog *>(_o);
        switch (_id) {
        case 0: _t->colorChanged(); break;
        case 1: _t->setDefaultColors(); break;
        case 2: _t->selectEntry(); break;
        case 3: _t->selectEntry((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 4: _t->reject(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData ColorSettingDialog::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject ColorSettingDialog::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_ColorSettingDialog,
      qt_meta_data_ColorSettingDialog, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &ColorSettingDialog::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *ColorSettingDialog::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *ColorSettingDialog::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_ColorSettingDialog))
        return static_cast<void*>(const_cast< ColorSettingDialog*>(this));
    return QDialog::qt_metacast(_clname);
}

int ColorSettingDialog::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    return _id;
}

// SIGNAL 0
void ColorSettingDialog::colorChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}
QT_END_MOC_NAMESPACE
