import React from 'react';
import type {Props} from '@theme/Root';

import '../css/custom.css';

export default function Root({children}: Props): JSX.Element {
  return <>{children}</>;
}
