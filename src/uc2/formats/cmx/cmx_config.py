# -*- coding: utf-8 -*-
#
#  Copyright (C) 2019 by Ihor E. Novikov
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License
#  as published by the Free Software Foundation, either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from uc2.utils.config import XmlConfigParser


class CMX_Config(XmlConfigParser):
    system_encoding = 'utf16'
    fallback_encoding = 'cp1250'
    rifx = False
    pack = False
    v16bit = True
    v1 = True
    save_preview = True
    preview_size = (96, 96)
    skip_empty = True
